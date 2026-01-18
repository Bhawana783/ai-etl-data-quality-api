AI-Assisted Development Workflow

This project was developed using AI tools such as ChatGPT and GitHub Copilot to accelerate development, explore design options, and improve code quality.
All AI-generated code and suggestions were critically reviewed, tested, and refined manually before being included in the final implementation.

Purpose of AI Usage

AI tools were used as engineering assistants, not as replacements for problem-solving or decision-making.
They helped with:

Designing the ETL pipeline

Generating boilerplate and exploratory code

Identifying potential improvements and edge cases

Refactoring and improving readability

1. ETL Pipeline Design
AI Contribution

Suggested an initial Extract → Transform → Load pipeline structure

Generated early versions of CSV ingestion and Pandas cleaning logic

Proposed separating raw data and cleaned data during storage

Human Review & Refinement

Verified column assumptions and data types

Refined cleaning logic to avoid unsafe Pandas operations

Ensured the ETL flow matches real-world data engineering practices:

Raw data stored first

Cleaned data stored separately

Cleaned data reused for downstream validation

2. Data Cleaning & Pandas Refinement
AI Contribution

Suggested use of dropna() and drop_duplicates()

Generated column-level transformation code

Issue Identified

Initial AI-generated code triggered a Pandas SettingWithCopyWarning

Human Fix

Explicitly created DataFrame copies before modification

Ensured safe type casting for numeric columns

This ensured the data cleaning logic was robust and production-safe.

3. Data Quality Checks
AI Contribution

Generated baseline data quality checks:

Missing values

Duplicate rows

Human Enhancements

Added domain-specific validation:

Detection of invalid ages (age < 0)

Ensured checks are executed on cleaned data, not raw input

These refinements made the quality checks more meaningful and realistic.

4. API Design & Refactoring
AI Contribution

Generated FastAPI route templates

Suggested use of dependency injection and Pydantic schemas

Human Refinement

Refactored routes to:

Enforce response models

Improve error handling

Maintain a clean request → ETL → validation flow

Ensured API behavior aligns with production-grade backend services

5. Database & SQLAlchemy Usage
AI Contribution

Generated initial SQLAlchemy model definitions

Suggested session-based database access patterns

Human Refinement

Designed separate tables for raw and cleaned data

Ensured transactional consistency with explicit commits

Verified schema alignment with ETL pipeline outputs

6. Testing & Validation
AI Contribution

Suggested test structures and scenarios

Helped identify potential edge cases

Human Validation

Implemented meaningful assertions

Manually tested API behavior using Swagger UI

Verified database persistence and quality report accuracy

Final Notes

AI tools were used responsibly and transparently

Every AI-generated suggestion was reviewed, modified, or rejected where necessary

The final system reflects human engineering judgment supported by AI acceleration