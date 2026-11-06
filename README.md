# DataGuard — Data Quality Monitor

A configurable data quality monitoring and validation application built with **Python, Pandas, YAML, and Streamlit**. DataGuard helps identify data issues, profile datasets, validate business rules, and perform basic data cleaning through an interactive dashboard.

## Overview

Data quality is essential for reliable analytics and decision-making. DataGuard provides a reusable validation engine and an interactive interface to help users understand dataset quality, detect inconsistencies, and generate validation reports.

The project demonstrates practical data engineering concepts, including modular Python development, configurable validation rules, automated testing, and CI/CD.

## Key Features

- **Dataset Profiling:** Analyze row counts, column types, missing values, duplicate records, unique values, and numerical statistics.
- **Configurable Validation:** Define data quality rules using YAML without changing the validation engine.
- **Validation Engine:** Check required columns, missing values, uniqueness, email formats, dates, numeric types, non-negative values, and allowed categories.
- **Interactive Dashboard:** Upload CSV files and explore profiling and validation results through Streamlit.
- **Data Cleaning:** Trim whitespace, standardize empty strings, and optionally remove duplicate rows.
- **Validation Reporting:** Generate downloadable validation reports and cleaned datasets.
- **Automated Testing:** Unit tests with pytest and code coverage reporting.
- **Continuous Integration:** GitHub Actions workflow to run tests automatically on pushes and pull requests.

## Technology Stack

| Area | Technologies |
|---|---|
| Programming | Python 3.12 |
| Data Processing | Pandas |
| Dashboard | Streamlit |
| Configuration | YAML, PyYAML |
| Testing | Pytest, pytest-cov |
| Version Control | Git, GitHub |
| CI/CD | GitHub Actions |

## Architecture

The application follows a modular structure, keeping the data quality engine independent of the Streamlit interface.

```text
dataguard-data-quality-monitor/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── config/
│   └── quality_rules.yaml
│
├── docs/
│   └── architecture.md
│
├── src/
│   └── dataguard/
│       ├── __init__.py
│       ├── cleaning.py
│       ├── profiler.py
│       ├── reporting.py
│       ├── rules.py
│       └── validators.py
│
├── tests/
│   ├── sample_data/
│   │   └── customers.csv
│   ├── test_cleaning.py
│   ├── test_profiler.py
│   ├── test_reporting.py
│   ├── test_rules.py
│   └── test_validators.py
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

## How It Works

1. Upload a CSV dataset through the Streamlit interface.
2. Profile the dataset to understand its structure and quality.
3. Load configurable validation rules from the YAML file.
4. Execute validation checks using the reusable Python validation engine.
5. Review failed checks, severity levels, and data quality metrics.
6. Apply supported cleaning operations.
7. Download the validation report and cleaned dataset.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/nithyaa-d/dataguard-data-quality-monitor.git
cd dataguard-data-quality-monitor
```

### 2. Create a virtual environment

**Windows:**

```cmd
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## Running Tests

Run the complete test suite:

```bash
pytest -v
```

Run tests with coverage:

```bash
pytest --cov=src.dataguard --cov-report=term-missing
```

### Current Test Results

| Metric | Result |
|---|---:|
| Total tests | 27 |
| Passed | 27 |
| Failed | 0 |
| Overall code coverage | 94% |

The test suite covers profiling, validation, cleaning, reporting, and YAML rule loading.

## Continuous Integration

DataGuard uses GitHub Actions to automate testing.

The workflow runs when code is pushed or a pull request is created against the `main` or `master` branch.

It performs the following steps:

- Checks out the repository.
- Sets up Python 3.12.
- Installs project dependencies.
- Executes the test suite with coverage reporting.

## Sample Dataset

A sample customer dataset is included in `tests/sample_data/customers.csv`.

It contains intentional data quality issues, including:

- Missing values.
- Duplicate customer identifiers.
- Invalid email formats.
- Invalid dates.
- Negative revenue values.
- Unexpected country and status values.

This dataset helps demonstrate how DataGuard identifies and reports data quality issues.

## Future Enhancements

- Support for additional file formats such as Excel and Parquet.
- More configurable validation rules.
- Database connectivity and scheduled validation.
- Historical data quality tracking.
- Enhanced reporting and visualization.
- Cloud deployment and integration with data pipelines.

## Author

**Nithya Doresha**

Data Engineer | Analytics Engineer | Data Analyst

- **LinkedIn:** [linkedin.com/in/nithyad2608](https://www.linkedin.com/in/nithyad2608/)
- **GitHub:** [github.com/nithyaa-d](https://github.com/nithyaa-d)

---

*Built to demonstrate practical data engineering, data quality, Python development, testing, and automation skills.*
