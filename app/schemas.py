from pydantic import BaseModel

class QualityReport(BaseModel):
    missing_values: int
    duplicate_rows: int
    invalid_ages: int
