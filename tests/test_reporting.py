
import pandas as pd

from src.dataguard.reporting import (
    build_validation_report,
    summarize_results,
)


def sample_results():
    return [
        {
            "rule": "unique_values",
            "column": "customer_id",
            "severity": "ERROR",
            "failed_count": 2,
            "passed": False,
            "message": "Duplicate values found.",
        },
        {
            "rule": "valid_email",
            "column": "email",
            "severity": "ERROR",
            "failed_count": 0,
            "passed": True,
            "message": "All email values are valid.",
        },
        {
            "rule": "allowed_values",
            "column": "country",
            "severity": "WARNING",
            "failed_count": 1,
            "passed": False,
            "message": "Unexpected values found.",
        },
    ]


def test_build_validation_report():
    report = build_validation_report(sample_results())

    assert isinstance(report, pd.DataFrame)
    assert len(report) == 3
    assert list(report.columns) == [
        "rule",
        "column",
        "severity",
        "failed_count",
        "passed",
        "message",
    ]


def test_summarize_results():
    summary = summarize_results(sample_results())

    assert summary["total_checks"] == 3
    assert summary["passed_checks"] == 1
    assert summary["failed_checks"] == 2
    assert summary["error_count"] == 1
    assert summary["warning_count"] == 1
    assert summary["quality_score"] == 33.33


def test_empty_results():
    summary = summarize_results([])

    assert summary["total_checks"] == 0
    assert summary["passed_checks"] == 0
    assert summary["failed_checks"] == 0
    assert summary["error_count"] == 0
    assert summary["warning_count"] == 0
    assert summary["quality_score"] == 100.0


def test_all_checks_passed():
    results = [
        {
            "rule": "valid_email",
            "column": "email",
            "severity": "ERROR",
            "failed_count": 0,
            "passed": True,
            "message": "All email values are valid.",
        },
        {
            "rule": "unique_values",
            "column": "customer_id",
            "severity": "ERROR",
            "failed_count": 0,
            "passed": True,
            "message": "All values are unique.",
        },
    ]

    summary = summarize_results(results)

    assert summary["passed_checks"] == 2
    assert summary["failed_checks"] == 0
    assert summary["quality_score"] == 100.0
