
import pandas as pd


def build_validation_report(results):
    """Convert validation results into a report DataFrame."""

    columns = [
        "rule",
        "column",
        "severity",
        "failed_count",
        "passed",
        "message",
    ]

    return pd.DataFrame(results, columns=columns)


def summarize_results(results):
    """Calculate validation summary metrics."""

    total_checks = len(results)
    passed_checks = sum(result["passed"] for result in results)
    failed_checks = total_checks - passed_checks

    error_count = sum(
        not result["passed"] and result["severity"] == "ERROR"
        for result in results
    )

    warning_count = sum(
        not result["passed"] and result["severity"] == "WARNING"
        for result in results
    )

    quality_score = (
        round((passed_checks / total_checks) * 100, 2)
        if total_checks
        else 100.0
    )

    return {
        "total_checks": total_checks,
        "passed_checks": passed_checks,
        "failed_checks": failed_checks,
        "error_count": error_count,
        "warning_count": warning_count,
        "quality_score": quality_score,
    }
