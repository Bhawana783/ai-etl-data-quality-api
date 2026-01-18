import pandas as pd
from sqlalchemy.orm import Session
from .models import RawData, CleanedData

def ingest_data(df: pd.DataFrame, db: Session):
    # store raw data
    for _, row in df.iterrows():
        db.add(RawData(
            name=row["name"],
            age=row["age"],
            salary=row["salary"]
        ))
    db.commit()

    # clean data (FIX APPLIED)
    df_clean = df.dropna().drop_duplicates().copy()
    df_clean["age"] = df_clean["age"].astype(int)

    # store cleaned data
    for _, row in df_clean.iterrows():
        db.add(CleanedData(
            name=row["name"],
            age=row["age"],
            salary=row["salary"]
        ))
    db.commit()

    return df_clean
