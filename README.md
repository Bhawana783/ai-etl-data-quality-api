AI ETL Data Quality API
📌 Overview

This project is a Python-based ETL and data quality API built using FastAPI, Pandas, and SQLAlchemy.
It demonstrates how to ingest CSV data, clean and validate it, store both raw and processed data in a database, and expose data quality insights via an API.

The project also showcases AI-assisted development, where tools like GitHub Copilot and ChatGPT were used to accelerate ETL logic, SQL handling, and bug fixing.

🎯 What This Project Demonstrates

Backend API development using FastAPI

ETL (Extract, Transform, Load) pipeline design

Data cleaning and validation using Pandas

Relational database usage with SQLAlchemy (SQLite)

Data quality checks and reporting

AI-assisted coding and optimization

🧱 Tech Stack

Python

FastAPI

Pandas

SQLAlchemy

SQLite

Pytest

GitHub Copilot / ChatGPT

📁 Project Structure
ai-etl-data-quality-api/
│
├── app/
│   ├── main.py            # FastAPI app & routes
│   ├── database.py        # Database configuration
│   ├── models.py          # SQLAlchemy models
│   ├── ingestion.py       # ETL logic (raw + cleaned data)
│   ├── quality_checks.py  # Data quality checks
│   └── schemas.py         # Pydantic response schemas
│
├── tests/
│   └── test_quality_checks.py
│
├── AI_WORKFLOW.md         # AI-assisted development proof
├── README.md
└── requirements.txt

📊 Expected CSV Format

The uploaded CSV file must contain the following columns:

name, age, salary


Example:

name,age,salary
Alice,25,50000
Bob,30,60000

⚙️ How the ETL Pipeline Works

Extract

CSV file is uploaded via the /upload API

Data is read into a Pandas DataFrame

Transform

Remove null values

Remove duplicate rows

Convert age to integer

Load

Raw data is stored in the raw_data table

Cleaned data is stored in the cleaned_data table

Validate

Data quality checks are run on the cleaned dataset

✅ Data Quality Checks

The API performs three data quality checks:

Missing values count

Duplicate rows count

Invalid ages (age < 0)

The results are returned as a structured JSON response.

🚀 API Usage
Start the Server
pip install -r requirements.txt
uvicorn app.main:app --reload

Open API Docs
http://127.0.0.1:8000/docs

Upload CSV

Endpoint: POST /upload

Upload a .csv file using Swagger UI or Postman

Sample Response
{
  "missing_values": 0,
  "duplicate_rows": 1,
  "invalid_ages": 0
}

🧪 Running Tests
pytest

🤖 AI-Assisted Development

Details of AI usage are documented in AI_WORKFLOW.md, including:

Copilot-generated ETL code

Fixing Pandas SettingWithCopyWarning

Improving SQLAlchemy data persistence logic

This demonstrates responsible and effective use of AI tools in software development.