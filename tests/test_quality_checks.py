import pandas as pd
from app.quality_checks import run_quality_checks

def test_quality_checks():
    df = pd.DataFrame({
        "name": ["A", "A", None],
        "age": [25, -1, 30],
        "salary": [50000, 50000, None]
    })

    report = run_quality_checks(df)

    assert report["missing_values"] == 2
    assert report["duplicate_rows"] == 1
    assert report["invalid_ages"] == 1
