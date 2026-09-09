"""BDD validation steps for local research CSV cleaning."""

import csv
from pathlib import Path
from typing import Any

import pytest
from pytest_bdd import given, scenario, then, when

from research_csv_cleaner import cli_application


@pytest.fixture
def context(tmp_path: Path) -> dict[str, Any]:
    return {
        "input_path": tmp_path / "input.csv",
        "output_path": tmp_path / "cleaned.csv",
        "required_column": "measurement",
    }


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as csv_file:
        return list(csv.DictReader(csv_file))


def run_tool(context: dict[str, Any]) -> int:
    return cli_application.main(
        [
            str(context["input_path"]),
            str(context["output_path"]),
            context["required_column"],
        ],
    )


def create_mixed_input(context: dict[str, Any]) -> None:
    write_csv(
        context["input_path"],
        ["sample", context["required_column"]],
        [
            {"sample": "valid-one", context["required_column"]: "1.25"},
            {"sample": "missing", context["required_column"]: ""},
            {"sample": "text", context["required_column"]: "not-a-number"},
            {"sample": "nan", context["required_column"]: "NaN"},
            {"sample": "infinite", context["required_column"]: "inf"},
            {"sample": "valid-two", context["required_column"]: "5"},
        ],
    )


@scenario("../features/research_csv_cleaning.feature", "CSV input is read")
def test_csv_input_is_read() -> None:
    pass


@scenario(
    "../features/research_csv_cleaning.feature",
    "Required numeric column validation is applied",
)
def test_required_numeric_column_validation_is_applied() -> None:
    pass


@scenario("../features/research_csv_cleaning.feature", "Required numeric column is missing")
def test_required_numeric_column_is_missing() -> None:
    pass


@scenario("../features/research_csv_cleaning.feature", "Invalid rows are removed")
def test_invalid_rows_are_removed() -> None:
    pass


@scenario(
    "../features/research_csv_cleaning.feature",
    "Supported invalid numeric values are removed",
)
def test_supported_invalid_numeric_values_are_removed() -> None:
    pass


@scenario("../features/research_csv_cleaning.feature", "Cleaned CSV is written")
def test_cleaned_csv_is_written() -> None:
    pass


@scenario("../features/research_csv_cleaning.feature", "Removed row count is reported")
def test_removed_row_count_is_reported() -> None:
    pass


@given("a local CSV file exists")
def local_csv_file_exists(context: dict[str, Any]) -> None:
    write_csv(
        context["input_path"],
        ["sample", context["required_column"]],
        [{"sample": "a", context["required_column"]: "1"}],
    )


@given("a local CSV file contains the configured required numeric column")
def local_csv_file_contains_required_column(context: dict[str, Any]) -> None:
    create_mixed_input(context)


@given("a local CSV file does not contain the configured required numeric column")
def local_csv_file_does_not_contain_required_column(context: dict[str, Any]) -> None:
    write_csv(
        context["input_path"],
        ["sample", "notes"],
        [{"sample": "a", "notes": "missing measurement column"}],
    )


@given("a local CSV file contains rows with invalid values in the required numeric column")
def local_csv_file_contains_invalid_required_column_values(context: dict[str, Any]) -> None:
    create_mixed_input(context)


@given(
    "a local CSV file contains rows where the required numeric column has missing values, "
    "empty values, values that cannot be parsed as floating-point numbers, NaN values, "
    "or infinite values"
)
def local_csv_file_contains_supported_invalid_numeric_values(context: dict[str, Any]) -> None:
    create_mixed_input(context)


@given("the tool has finished cleaning the input CSV")
def tool_has_finished_cleaning(context: dict[str, Any], capsys: pytest.CaptureFixture[str]) -> None:
    create_mixed_input(context)
    context["exit_code"] = run_tool(context)
    context["captured"] = capsys.readouterr()


@given("the tool has removed rows during cleaning")
def tool_has_removed_rows(context: dict[str, Any], capsys: pytest.CaptureFixture[str]) -> None:
    create_mixed_input(context)
    context["exit_code"] = run_tool(context)
    context["captured"] = capsys.readouterr()


@when("the researcher runs the tool with that file as input")
@when("the researcher runs the tool")
def researcher_runs_the_tool(
    context: dict[str, Any],
    capsys: pytest.CaptureFixture[str],
) -> None:
    context["exit_code"] = run_tool(context)
    context["captured"] = capsys.readouterr()


@when("the cleaning run completes")
def cleaning_run_completes(context: dict[str, Any]) -> None:
    assert context["exit_code"] == 0


@then("the tool reads the CSV file for cleaning")
def tool_reads_the_csv_file(context: dict[str, Any]) -> None:
    assert context["exit_code"] == 0
    assert context["output_path"].exists()


@then(
    "the tool treats missing values, empty values, values that cannot be parsed as "
    "floating-point numbers, NaN values, and infinite values as invalid"
)
def tool_treats_supported_values_as_invalid(context: dict[str, Any]) -> None:
    rows = read_csv(context["output_path"])
    assert [row["sample"] for row in rows] == ["valid-one", "valid-two"]


@then("the tool fails with a clear error message")
def tool_fails_with_clear_error_message(context: dict[str, Any]) -> None:
    assert context["exit_code"] != 0
    assert context["required_column"] in context["captured"].err
    assert "missing" in context["captured"].err.lower()


@then("the tool does not create an output file")
def tool_does_not_create_output_file(context: dict[str, Any]) -> None:
    assert not context["output_path"].exists()


@then("the cleaned output excludes the rows with invalid values")
@then("the cleaned output excludes those rows")
def cleaned_output_excludes_invalid_rows(context: dict[str, Any]) -> None:
    rows = read_csv(context["output_path"])
    assert [row["sample"] for row in rows] == ["valid-one", "valid-two"]


@then("the tool writes a cleaned CSV file")
def tool_writes_cleaned_csv_file(context: dict[str, Any]) -> None:
    assert context["output_path"].exists()
    assert read_csv(context["output_path"])


@then("the tool reports the number of rows removed")
def tool_reports_number_of_rows_removed(context: dict[str, Any]) -> None:
    assert "4" in context["captured"].out
