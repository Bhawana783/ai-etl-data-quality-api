import pandas as pd

def run_quality_checks(df: pd.DataFrame) -> dict:
    missing_values = df.isnull().sum().sum()
    duplicate_rows = df.duplicated().sum()
    invalid_ages = df[df["age"] < 0].shape[0]

    return {
        "missing_values": int(missing_values),
        "duplicate_rows": int(duplicate_rows),
        "invalid_ages": int(invalid_ages)
    }
