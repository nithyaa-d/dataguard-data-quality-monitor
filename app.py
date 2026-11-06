
import pandas as pd
import streamlit as st

from src.dataguard.cleaning import clean_dataframe
from src.dataguard.profiler import profile_dataframe
from src.dataguard.reporting import (
    build_validation_report,
    summarize_results,
)
from src.dataguard.rules import load_rules
from src.dataguard.validators import validate_dataframe


st.set_page_config(
    page_title="DataGuard | Data Quality Monitor",
    page_icon="🛡️",
    layout="wide",
)

st.title("🛡️ DataGuard")
st.caption(
    "A configurable data quality monitoring and validation platform"
)

# Sidebar
st.sidebar.header("DataGuard Controls")

uploaded_file = st.sidebar.file_uploader(
    "Upload a CSV dataset",
    type=["csv"],
)

st.sidebar.divider()
st.sidebar.subheader("Cleaning options")

trim_whitespace = st.sidebar.checkbox(
    "Trim whitespace",
    value=True,
)

standardize_empty = st.sidebar.checkbox(
    "Standardize empty strings",
    value=True,
)

drop_duplicates = st.sidebar.checkbox(
    "Remove exact duplicate rows",
    value=False,
)

if uploaded_file is None:
    st.info("Upload a CSV file from the sidebar to start analysing your data.")

    st.subheader("What DataGuard can do")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 📊 Profiling")
        st.write("Understand dataset structure, missing values and statistics.")

    with col2:
        st.markdown("### 🔍 Validation")
        st.write("Identify duplicates, invalid formats and unexpected values.")

    with col3:
        st.markdown("### 🧹 Cleaning")
        st.write("Apply controlled cleaning operations and export the results.")

    st.stop()


# Load CSV
try:
    df = pd.read_csv(uploaded_file)
except Exception as exc:
    st.error(f"Could not read the uploaded CSV: {exc}")
    st.stop()


# Load rules and analyse data
try:
    rules = load_rules()
    profile = profile_dataframe(df)
    results = validate_dataframe(df, rules)
    summary = summarize_results(results)
except Exception as exc:
    st.error(f"Analysis failed: {exc}")
    st.stop()


# Overview
st.divider()
st.header("Dataset Overview")

metric1, metric2, metric3, metric4 = st.columns(4)

metric1.metric("Total rows", f"{profile['row_count']:,}")
metric2.metric("Total columns", profile["column_count"])
metric3.metric(
    "Missing values",
    f"{profile['total_missing_values']:,}",
)
metric4.metric(
    "Rule-pass score",
    f"{summary['quality_score']}%",
)

st.caption(
    "Rule-pass score = percentage of validation checks passed. "
    "It is not the percentage of clean records."
)

st.divider()

# Validation summary
st.header("Validation Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total checks", summary["total_checks"])
col2.metric("Passed", summary["passed_checks"])
col3.metric("Failed errors", summary["error_count"])
col4.metric("Failed warnings", summary["warning_count"])

# Tabs
overview_tab, profile_tab, validation_tab, cleaning_tab = st.tabs(
    [
        "Dataset Preview",
        "Data Profiling",
        "Validation Results",
        "Data Cleaning",
    ]
)


with overview_tab:
    st.subheader("Uploaded Dataset")
    st.dataframe(df.head(100), use_container_width=True)

    st.caption(
        f"Showing up to 100 of {len(df):,} records."
    )


with profile_tab:
    st.subheader("Column-level Profile")

    profile_df = pd.DataFrame(profile["columns"])

    st.dataframe(
        profile_df,
        use_container_width=True,
        hide_index=True,
    )

    numeric_profiles = [
        column
        for column in profile["columns"]
        if "statistics" in column
    ]

    if numeric_profiles:
        st.subheader("Numeric Statistics")

        for column in numeric_profiles:
            st.write(f"**{column['name']}**")
            st.json(column["statistics"])


with validation_tab:
    st.subheader("Validation Checks")

    report_df = build_validation_report(results)

    status_filter = st.selectbox(
        "Filter results",
        ["All", "Passed", "Failed"],
    )

    if status_filter == "Passed":
        displayed_report = report_df[
            report_df["passed"] == True
        ]
    elif status_filter == "Failed":
        displayed_report = report_df[
            report_df["passed"] == False
        ]
    else:
        displayed_report = report_df

    st.dataframe(
        displayed_report,
        use_container_width=True,
        hide_index=True,
    )

    st.download_button(
        "Download Validation Report",
        data=report_df.to_csv(index=False).encode("utf-8"),
        file_name="dataguard_validation_report.csv",
        mime="text/csv",
    )


with cleaning_tab:
    st.subheader("Clean Dataset")

    cleaned_df, cleaning_summary = clean_dataframe(
        df,
        trim_whitespace=trim_whitespace,
        standardize_empty_strings=standardize_empty,
        drop_duplicate_rows=drop_duplicates,
    )

    st.write("Cleaning summary")

    st.json(cleaning_summary)

    st.subheader("Cleaned Dataset Preview")
    st.dataframe(
        cleaned_df.head(100),
        use_container_width=True,
    )

    st.download_button(
        "Download Cleaned CSV",
        data=cleaned_df.to_csv(index=False).encode("utf-8"),
        file_name="dataguard_cleaned_data.csv",
        mime="text/csv",
    )


st.divider()
st.caption("DataGuard | Built with Python, Pandas and Streamlit")
