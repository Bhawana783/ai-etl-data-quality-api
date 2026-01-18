from fastapi import FastAPI, UploadFile, File, Depends, HTTPException
import pandas as pd
from sqlalchemy.orm import Session

from .database import Base, engine, SessionLocal
from .ingestion import ingest_data
from .quality_checks import run_quality_checks
from .schemas import QualityReport

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI ETL Data Quality API")

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/upload", response_model=QualityReport)
async def upload_csv(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    # Check file type
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are allowed.")

    try:
        # Read CSV into pandas DataFrame
        df = pd.read_csv(file.file)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error reading CSV: {e}")

    # Ingest data (raw + cleaned) and get cleaned DataFrame
    try:
        df_clean = ingest_data(df, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error ingesting data: {e}")

    # Run data quality checks on CLEANED data
    quality_report = run_quality_checks(df_clean)

    return quality_report
