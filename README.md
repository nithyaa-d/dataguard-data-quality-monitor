# DataGuard | Data Quality Monitor

**A Python-based data quality monitoring and validation application built with Pandas, YAML, and Streamlit.**

DataGuard helps identify data quality issues, profile datasets, validate business rules, and perform basic data cleaning through an interactive dashboard.

---

## Project Overview

Reliable data is the foundation of effective analytics and decision-making. DataGuard provides a reusable validation engine and an interactive interface to help users assess dataset quality, identify inconsistencies, and generate validation reports.

The project demonstrates practical data engineering concepts, including modular Python development, configurable validation rules, automated testing, and continuous integration.

## Features

| Feature | Description |
|:---|:---|
| Dataset Profiling | Analyze dimensions, data types, missing values, duplicates, unique values, and numerical statistics. |
| Configurable Rules | Define validation rules through YAML configuration. |
| Validation Engine | Detect missing fields, duplicate values, invalid emails, dates, numeric values, and unexpected categories. |
| Interactive Dashboard | Upload CSV files and explore results using Streamlit. |
| Data Cleaning | Trim whitespace, standardize empty strings, and optionally remove duplicate rows. |
| Reporting | Generate downloadable validation reports and cleaned datasets. |
| Automated Testing | Validate application logic using pytest and coverage reporting. |
| CI/CD | Run automated tests through GitHub Actions. |

## Technology Stack

| Category | Tools |
|:---|:---|
| Programming | Python 3.12 |
| Data Processing | Pandas |
| Dashboard | Streamlit |
| Configuration | YAML, PyYAML |
| Testing | Pytest, pytest-cov |
| Version Control | Git, GitHub |
| CI/CD | GitHub Actions |

## Architecture

DataGuard follows a modular architecture that separates the core data quality engine from the user interface.

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

## Application Workflow

1. Upload a CSV dataset.
2. Profile the dataset and inspect its structure.
3. Load validation rules from the YAML configuration.
4. Execute quality checks using the validation engine.
5. Review validation results, failures, and severity levels.
6. Apply supported data cleaning operations.
7. Download the validation report and cleaned dataset.

## Getting Started

### Prerequisites

- Python 3.12 or later
- Git

### 1. Clone the repository

```bash
git clone https://github.com/nithyaa-d/dataguard-data-quality-monitor.git
cd dataguard-data-quality-monitor
```

### 2. Create and activate a virtual environment

**Windows (CMD)**

```cmd
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Launch the application

```bash
streamlit run app.py
```

The dashboard will open in your default browser.

## Testing & Code Coverage

Run the test suite:

```bash
pytest -v
```

Generate a coverage report:

```bash
pytest --cov=src.dataguard --cov-report=term-missing
```

### Test Results

| Metric | Result |
|:---|---:|
| Total tests | 27 |
| Passed | 27 |
| Failed | 0 |
| Code coverage | 94% |

Tests cover the profiling, validation, cleaning, reporting, and YAML rule-loading modules.

## Continuous Integration

GitHub Actions automates testing whenever code is pushed or a pull request is opened against the `main` or `master` branch.

The workflow:

- Checks out the repository.
- Sets up Python 3.12.
- Installs dependencies.
- Executes the test suite with coverage reporting.

## Sample Dataset

The repository includes a sample customer dataset at:

`tests/sample_data/customers.csv`

The dataset contains intentional quality issues to demonstrate validation capabilities:

- Missing values.
- Duplicate customer identifiers.
- Invalid email addresses.
- Invalid dates.
- Negative revenue values.
- Unexpected country and status values.

## Future Enhancements

- Excel and Parquet file support.
- Additional configurable validation rules.
- Database connectivity and scheduled validation.
- Historical data quality tracking.
- Enhanced reporting and visualizations.
- Cloud deployment and data pipeline integration.

---

## Author

**Nithya Doresha**

Data Engineer | Analytics Engineer | Data Analyst

[LinkedIn](https://www.linkedin.com/in/nithyad2608/) · [GitHub](https://github.com/nithyaa-d)

---

*Developed to demonstrate practical data engineering, data quality management, Python development, testing, and automation.*
