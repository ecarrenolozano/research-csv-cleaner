"""BDD validation steps for active CR-0001 CSV validation behavior."""

import csv
from pathlib import Path
from typing import Any

import pytest
from pytest_bdd import given, scenario, then, when
from streamlit.testing.v1 import AppTest

from research_csv_cleaner import cli_application, streamlit_interface

STREAMLIT_APP_PATH = (
    Path(__file__).parents[3]
    / "src"
    / "research_csv_cleaner"
    / "streamlit_interface.py"
)
CSV_UPLOAD = b"sample,measurement,notes\na,1.25,ok\nb,,empty\nc,NaN,bad\n"


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


def run_streamlit_validation(context: dict[str, Any]) -> None:
    app = AppTest.from_file(STREAMLIT_APP_PATH).run()
    app.file_uploader[0].set_value(("input.csv", CSV_UPLOAD, "text/csv")).run()
    app.selectbox[0].set_value(context["required_column"]).run()
    context["streamlit_app"] = app


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
    "US-0006 CSV input is read for validation",
)
def test_csv_input_is_read_for_validation() -> None:
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


@scenario(
    "../features/research_csv_cleaning.feature",
    "US-0010 resulting CSV is written",
)
def test_resulting_csv_is_written() -> None:
    pass


@scenario(
    "../features/research_csv_cleaning.feature",
    "US-0011 resulting CSV is downloaded",
)
def test_resulting_csv_is_downloaded() -> None:
    pass


@scenario(
    "../features/research_csv_cleaning.feature",
    "US-0012 validation-error row count is reported",
)
def test_validation_error_row_count_is_reported() -> None:
    pass


@scenario(
    "../features/research_csv_cleaning.feature",
    "US-0013 validation-error row count is displayed",
)
def test_validation_error_row_count_is_displayed() -> None:
    pass


@scenario(
    "../features/research_csv_cleaning.feature",
    "US-0014 CSV file is uploaded",
)
def test_csv_file_is_uploaded() -> None:
    pass


@scenario(
    "../features/research_csv_cleaning.feature",
    "US-0015 numeric column is selected",
)
def test_numeric_column_is_selected() -> None:
    pass


@scenario(
    "../features/research_csv_cleaning.feature",
    "US-0016 validated data is previewed",
)
def test_validated_data_is_previewed() -> None:
    pass


@scenario(
    "../features/research_csv_cleaning.feature",
    "US-0017 existing CLI still runs",
)
def test_existing_cli_still_runs() -> None:
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


@given("a CSV file is available for validation")
def csv_file_is_available_for_validation(context: dict[str, Any]) -> None:
    write_csv(
        context["input_path"],
        ["sample", context["required_column"]],
        [{"sample": "valid-one", context["required_column"]: "1.25"}],
    )


@given("the CLI has detected rows with validation errors")
def cli_has_detected_rows_with_validation_errors(context: dict[str, Any]) -> None:
    create_mixed_input(context)


@given("a CSV file does not contain the selected numeric column")
def csv_file_does_not_contain_selected_numeric_column(context: dict[str, Any]) -> None:
    write_csv(
        context["input_path"],
        ["sample", "notes"],
        [{"sample": "missing-column", "notes": "measurement unavailable"}],
    )


@given("validation has completed in the Streamlit interface")
def validation_has_completed_in_streamlit_interface(context: dict[str, Any]) -> None:
    run_streamlit_validation(context)


@given("the Streamlit interface is open")
def streamlit_interface_is_open(context: dict[str, Any]) -> None:
    context["streamlit_app"] = AppTest.from_file(STREAMLIT_APP_PATH).run()


@given("a CSV file is uploaded in the Streamlit interface")
def csv_file_is_uploaded_in_streamlit_interface(context: dict[str, Any]) -> None:
    app = AppTest.from_file(STREAMLIT_APP_PATH).run()
    app.file_uploader[0].set_value(("input.csv", CSV_UPLOAD, "text/csv")).run()
    context["streamlit_app"] = app


@given("a researcher provides the existing CLI inputs")
def researcher_provides_existing_cli_inputs(context: dict[str, Any]) -> None:
    create_mixed_input(context)


@when("the researcher validates the file")
def researcher_validates_the_file(
    context: dict[str, Any],
    capsys: pytest.CaptureFixture[str],
) -> None:
    context["exit_code"] = run_tool(context)
    context["captured"] = capsys.readouterr()


@when("the validation run completes")
def validation_run_completes(
    context: dict[str, Any],
    capsys: pytest.CaptureFixture[str],
) -> None:
    researcher_validates_the_file(context, capsys)


@when("the researcher downloads the resulting CSV")
def researcher_downloads_the_resulting_csv(context: dict[str, Any]) -> None:
    assert context["streamlit_app"].download_button


@when("the validated data is available")
def validated_data_is_available(context: dict[str, Any]) -> None:
    assert context["streamlit_app"].dataframe


@when("the researcher uploads a CSV file")
def researcher_uploads_csv_file(context: dict[str, Any]) -> None:
    app = context["streamlit_app"]
    app.file_uploader[0].set_value(("input.csv", CSV_UPLOAD, "text/csv")).run()
    context["streamlit_app"] = app


@when("the researcher selects a numeric column")
def researcher_selects_numeric_column(context: dict[str, Any]) -> None:
    app = context["streamlit_app"]
    app.selectbox[0].set_value(context["required_column"]).run()
    context["streamlit_app"] = app


@when("the researcher runs the CLI")
def researcher_runs_the_cli(
    context: dict[str, Any],
    capsys: pytest.CaptureFixture[str],
) -> None:
    researcher_validates_the_file(context, capsys)


@then("the tool reads the CSV file for validation")
def tool_reads_csv_file_for_validation(context: dict[str, Any]) -> None:
    rows = read_csv(context["output_path"])

    assert context["exit_code"] == 0
    assert rows == [
        {
            "sample": "valid-one",
            context["required_column"]: "1.25",
            "validation_errors": "",
        },
    ]


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


@then("the tool writes a resulting CSV file")
def tool_writes_resulting_csv_file(context: dict[str, Any]) -> None:
    rows = read_csv(context["output_path"])

    assert context["exit_code"] == 0
    assert context["output_path"].is_file()
    assert rows == [
        {
            "sample": "valid-one",
            context["required_column"]: "1.25",
            "validation_errors": "",
        },
    ]


@then("the interface provides the resulting CSV for download")
def interface_provides_resulting_csv_for_download(context: dict[str, Any]) -> None:
    app = context["streamlit_app"]
    resulting_csv = streamlit_interface.resulting_csv_text(
        [
            {"sample": "a", "measurement": "1.25", "notes": "ok", "validation_errors": ""},
            {
                "sample": "b",
                "measurement": "",
                "notes": "empty",
                "validation_errors": "measurement is empty",
            },
            {
                "sample": "c",
                "measurement": "NaN",
                "notes": "bad",
                "validation_errors": "measurement is NaN",
            },
        ],
        ["sample", "measurement", "notes"],
    )

    assert len(app.download_button) == 1
    assert app.download_button[0].label == "Download resulting CSV"
    assert resulting_csv.splitlines() == [
        "sample,measurement,notes,validation_errors",
        "a,1.25,ok,",
        "b,,empty,measurement is empty",
        "c,NaN,bad,measurement is NaN",
    ]


@then("the CLI reports the number of rows containing validation errors")
def cli_reports_validation_error_row_count(context: dict[str, Any]) -> None:
    assert context["exit_code"] == 0
    assert "Rows containing validation errors: 4" in context["captured"].out


@then("the interface displays the number of rows containing validation errors")
def interface_displays_validation_error_row_count(context: dict[str, Any]) -> None:
    app = context["streamlit_app"]

    assert len(app.metric) == 1
    assert app.metric[0].label == "Rows containing validation errors"
    assert app.metric[0].value == "2"


@then("the interface accepts the CSV file for validation")
def interface_accepts_csv_file_for_validation(context: dict[str, Any]) -> None:
    app = context["streamlit_app"]

    assert len(app.selectbox) == 1
    assert context["required_column"] in app.selectbox[0].options


@then("the interface uses that selected column for validation")
def interface_uses_selected_column_for_validation(context: dict[str, Any]) -> None:
    app = context["streamlit_app"]
    preview = app.dataframe[0].value

    assert len(app.dataframe) == 1
    assert list(preview["validation_errors"]) == [
        "",
        "measurement is empty",
        "measurement is NaN",
    ]


@then("the interface previews the validated data")
def interface_previews_validated_data(context: dict[str, Any]) -> None:
    app = context["streamlit_app"]
    preview = app.dataframe[0].value

    assert len(app.dataframe) == 1
    assert list(preview["sample"]) == ["a", "b", "c"]
    assert "validation_errors" in preview.columns


@then("the CLI validates the CSV and produces the resulting CSV")
def cli_validates_csv_and_produces_resulting_csv(context: dict[str, Any]) -> None:
    rows = read_csv(context["output_path"])

    assert context["exit_code"] == 0
    assert context["output_path"].is_file()
    assert len(rows) == 6
    assert "Rows containing validation errors:" in context["captured"].out
