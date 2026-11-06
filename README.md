\# 🛡️ DataGuard — Data Quality Monitor



A configurable data quality monitoring and validation application built with \*\*Python, Pandas, PyYAML, and Streamlit\*\*.



DataGuard helps users inspect datasets, identify data quality issues, validate records against configurable business rules, and apply safe cleaning operations through an interactive dashboard.



\## 🚀 Key Features



\### 1. Dataset Profiling

\- Total rows and columns

\- Missing-value analysis

\- Duplicate-row detection

\- Column-level data types

\- Unique-value counts

\- Missing-value percentages

\- Numeric statistics including minimum, maximum, and mean



\### 2. Configurable Data Validation

Define data quality rules using YAML configuration.



Supported validation checks:

\- Required columns and missing values

\- Duplicate values in specified columns

\- Email format validation

\- Date format validation

\- Numeric data validation

\- Non-negative numeric values

\- Allowed-value validation



Validation results include severity levels, failed counts, pass/fail status, and descriptive messages.



\### 3. Interactive Dashboard

Built using Streamlit, with dedicated sections for:

\- Dataset Preview

\- Data Profiling

\- Validation Results

\- Data Cleaning



\### 4. Data Cleaning

Apply configurable cleaning operations:

\- Trim leading and trailing whitespace

\- Standardize empty strings as missing values

\- Optionally remove completely duplicated rows



The original DataFrame is preserved. Missing values are not automatically deleted or filled.



\### 5. Reporting and Export

\- Validation summary

\- Rule-pass score

\- Downloadable validation report

\- Downloadable cleaned CSV



\*\*Note:\*\* The rule-pass score represents the percentage of validation checks passed. It is not a measure of the percentage of clean records.



\---



\## 🧰 Technology Stack



| Technology | Purpose |

|---|---|

| Python 3.12 | Core application |

| Pandas | Data processing and analysis |

| Streamlit | Interactive dashboard |

| PyYAML | YAML-based rule configuration |

| Pytest | Automated testing |

| pytest-cov | Test coverage |

| GitHub Actions | Continuous integration |



\---



\## 🏗️ Project Architecture



```text

dataguard-data-quality-monitor/

│

├── .github/

│   └── workflows/

│       └── tests.yml

│

├── config/

│   └── quality\_rules.yaml

│

├── docs/

│   └── architecture.md

│

├── src/

│   └── dataguard/

│       ├── \_\_init\_\_.py

│       ├── cleaning.py

│       ├── profiler.py

│       ├── reporting.py

│       ├── rules.py

│       └── validators.py

│

├── tests/

│   ├── sample\_data/

│   │   └── customers.csv

│   ├── test\_cleaning.py

│   ├── test\_profiler.py

│   ├── test\_reporting.py

│   ├── test\_rules.py

│   └── test\_validators.py

│

├── app.py

├── requirements.txt

├── README.md

└── LICENSE

```



\### Application Workflow



```text

&#x20;      CSV Upload

&#x20;          |

&#x20;          v

&#x20;   Dataset Profiling

&#x20;          |

&#x20;          v

&#x20;   Load YAML Rules

&#x20;          |

&#x20;          v

&#x20;  Data Validation Engine

&#x20;          |

&#x20;          v

&#x20;   Validation Results

&#x20;          |

&#x20;          v

&#x20;     Data Cleaning

&#x20;          |

&#x20;          v

&#x20;  Reports and CSV Export

```



The validation and profiling logic is separated from the Streamlit interface, allowing the core functionality to be reused independently.



\---



\## ⚙️ Installation and Setup



\### Prerequisites

\- Python 3.12

\- Git



\### 1. Clone the repository



```bash

git clone <YOUR\_GITHUB\_REPOSITORY\_URL>

cd dataguard-data-quality-monitor

```



\### 2. Create a virtual environment



\*\*Windows CMD:\*\*



```cmd

python -m venv .venv

.venv\\Scripts\\activate

```



\### 3. Install dependencies



```bash

python -m pip install --upgrade pip

pip install -r requirements.txt

```



\### 4. Run the application



```bash

streamlit run app.py

```



Streamlit will provide a local URL, usually:



```text

http://localhost:8501

```



Upload a CSV file to start profiling and validating your dataset.



\---



\## 🧪 Testing



DataGuard includes automated unit tests for its core modules.



Run the complete test suite:



```bash

pytest -v

```



Run tests with coverage:



```bash

pytest --cov=src.dataguard --cov-report=term-missing

```



\### Current Test Results



| Metric | Result |

|---|---:|

| Total automated tests | 27 |

| Tests passed | 27 |

| Tests failed | 0 |

| Overall code coverage | 94% |



Coverage is measured across the `src.dataguard` package.



\### Continuous Integration



GitHub Actions is configured to:

\- Set up Python 3.12

\- Install project dependencies

\- Run automated tests

\- Generate a coverage report



The workflow runs on pushes and pull requests targeting the `main` or `master` branches.



\---



\## 📊 Sample Dataset



A sample customer dataset is included at:



`tests/sample\_data/customers.csv`



It contains 100 records and intentionally introduced data quality issues, including:

\- Missing values

\- Duplicate customer identifiers

\- Invalid email addresses

\- Invalid dates

\- Unexpected categorical values

\- Negative revenue values



This dataset can be used to explore the profiling, validation, and cleaning functionality.



\---



\## 🔮 Future Enhancements



Potential extensions include:

\- Additional configurable validation rules

\- Support for Excel and database sources

\- Historical data quality tracking

\- Scheduled validation runs

\- Database integration

\- Cloud deployment

\- Advanced data quality visualizations



\---



\## 👩‍💻 Author



\*\*Nithya Doresha\*\*



Data Engineer | Analytics Engineer | Data Analyst



\- \[LinkedIn](https://www.linkedin.com/in/nithyad2608/)

\- \[GitHub](https://github.com/nithyaa-d)



\---



\*Built as a hands-on project to demonstrate Python-based data profiling, configurable validation, data cleaning, automated testing, and continuous integration.\*

