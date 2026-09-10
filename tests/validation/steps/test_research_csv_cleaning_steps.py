"""BDD validation steps for active CR-0001 CSV validation behavior."""

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
        "output_path": tmp_path / "result.csv",
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


@scenario(
    "../features/research_csv_cleaning.feature",
    "US-0007 selected numeric column validation is applied",
)
def test_selected_numeric_column_validation_is_applied() -> None:
    pass


@scenario(
    "../features/research_csv_cleaning.feature",
    "US-0007 selected numeric column is missing",
)
def test_selected_numeric_column_is_missing() -> None:
    pass


@scenario(
    "../features/research_csv_cleaning.feature",
    "US-0008 invalid rows remain in the resulting CSV",
)
def test_invalid_rows_remain_in_resulting_csv() -> None:
    pass


@scenario(
    "../features/research_csv_cleaning.feature", "US-0009 invalid rows include validation errors"
)
def test_invalid_rows_include_validation_errors() -> None:
    pass


@scenario(
    "../features/research_csv_cleaning.feature",
    "US-0009 validation errors explain the specific invalid numeric problem",
)
def test_validation_errors_explain_specific_invalid_numeric_problem() -> None:
    pass


@scenario(
    "../features/research_csv_cleaning.feature", "US-0009 valid rows have no validation errors"
)
def test_valid_rows_have_no_validation_errors() -> None:
    pass


@given("a CSV file contains rows with invalid values in the selected numeric column")
def csv_file_contains_invalid_selected_column_values(context: dict[str, Any]) -> None:
    create_mixed_input(context)


@given(
    "a CSV file contains selected-column values that are missing, empty, "
    "unparseable as floating-point numbers, NaN, or infinite"
)
def csv_file_contains_specific_invalid_numeric_values(context: dict[str, Any]) -> None:
    create_mixed_input(context)


@given("a CSV file contains rows with valid values in the selected numeric column")
def csv_file_contains_valid_selected_column_values(context: dict[str, Any]) -> None:
    write_csv(
        context["input_path"],
        ["sample", context["required_column"]],
        [
            {"sample": "valid-one", context["required_column"]: "1.25"},
            {"sample": "valid-two", context["required_column"]: "5"},
        ],
    )


@given("a CSV file does not contain the selected numeric column")
def csv_file_does_not_contain_selected_numeric_column(context: dict[str, Any]) -> None:
    write_csv(
        context["input_path"],
        ["sample", "notes"],
        [{"sample": "missing-column", "notes": "measurement unavailable"}],
    )


@when("the researcher validates the file")
def researcher_validates_the_file(
    context: dict[str, Any],
    capsys: pytest.CaptureFixture[str],
) -> None:
    context["exit_code"] = run_tool(context)
    context["captured"] = capsys.readouterr()


@then("the resulting CSV contains every input row")
def resulting_csv_contains_every_input_row(context: dict[str, Any]) -> None:
    rows = read_csv(context["output_path"])

    assert context["exit_code"] == 0
    assert [row["sample"] for row in rows] == [
        "valid-one",
        "missing",
        "text",
        "nan",
        "infinite",
        "valid-two",
    ]


@then("the tool treats those selected-column values as invalid")
def selected_column_values_are_treated_as_invalid(context: dict[str, Any]) -> None:
    rows = read_csv(context["output_path"])
    errors_by_sample = {row["sample"]: row["validation_errors"] for row in rows}

    assert context["exit_code"] == 0
    assert errors_by_sample["missing"] == "measurement is empty"
    assert errors_by_sample["text"] == "measurement is not a number"
    assert errors_by_sample["nan"] == "measurement is NaN"
    assert errors_by_sample["infinite"] == "measurement is infinite"


@then("the tool fails with a clear missing-column error")
def tool_fails_with_clear_missing_column_error(context: dict[str, Any]) -> None:
    error_output = context["captured"].err

    assert context["exit_code"] != 0
    assert context["required_column"] in error_output
    assert "missing" in error_output.lower()


@then("the tool does not create a resulting CSV")
def tool_does_not_create_resulting_csv(context: dict[str, Any]) -> None:
    assert not context["output_path"].exists()


@then("each invalid row contains an explanation in the validation_errors column")
def invalid_rows_contain_validation_error_explanations(context: dict[str, Any]) -> None:
    rows = read_csv(context["output_path"])
    invalid_rows = [row for row in rows if row["sample"] not in {"valid-one", "valid-two"}]

    assert context["exit_code"] == 0
    assert invalid_rows
    assert all(row["validation_errors"] for row in invalid_rows)


@then(
    "each invalid row's validation_errors value explains the specific invalid numeric "
    "problem detected for that row"
)
def validation_errors_explain_specific_invalid_numeric_problem(context: dict[str, Any]) -> None:
    rows = read_csv(context["output_path"])
    errors_by_sample = {row["sample"]: row["validation_errors"] for row in rows}

    assert context["exit_code"] == 0
    assert errors_by_sample["missing"] == "measurement is empty"
    assert errors_by_sample["text"] == "measurement is not a number"
    assert errors_by_sample["nan"] == "measurement is NaN"
    assert errors_by_sample["infinite"] == "measurement is infinite"


@then("each valid row has no error explanation in the validation_errors column")
def valid_rows_have_no_validation_errors(context: dict[str, Any]) -> None:
    rows = read_csv(context["output_path"])

    assert context["exit_code"] == 0
    assert [row["validation_errors"] for row in rows] == ["", ""]
