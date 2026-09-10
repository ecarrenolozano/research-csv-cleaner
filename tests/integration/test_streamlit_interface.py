"""Technical smoke tests for the Streamlit interface module."""

from pathlib import Path

import pytest
from streamlit.testing.v1 import AppTest

from research_csv_cleaner import streamlit_interface

STREAMLIT_APP_PATH = (
    Path(__file__).parents[2]
    / "src"
    / "research_csv_cleaner"
    / "streamlit_interface.py"
)
CSV_UPLOAD = b"sample,measurement,notes\na,1.25,ok\nb,,empty\nc,NaN,bad\n"


def test_streamlit_interface_exposes_main_entry_point() -> None:
    assert callable(streamlit_interface.main)


@pytest.mark.integration
def test_streamlit_renders_upload_control() -> None:
    at = AppTest.from_file(STREAMLIT_APP_PATH)

    at.run()

    assert len(at.file_uploader) == 1


@pytest.mark.integration
def test_streamlit_uploaded_csv_exposes_numeric_column_selection() -> None:
    at = AppTest.from_file(STREAMLIT_APP_PATH).run()

    at.file_uploader[0].set_value(("input.csv", CSV_UPLOAD, "text/csv")).run()

    assert len(at.selectbox) == 1
    assert "measurement" in at.selectbox[0].options


@pytest.mark.integration
def test_streamlit_previews_validated_rows_and_displays_error_count() -> None:
    at = AppTest.from_file(STREAMLIT_APP_PATH).run()

    at.file_uploader[0].set_value(("input.csv", CSV_UPLOAD, "text/csv")).run()
    at.selectbox[0].set_value("measurement").run()

    assert len(at.dataframe) == 1
    preview = at.dataframe[0].value
    assert list(preview["sample"]) == ["a", "b", "c"]
    assert "validation_errors" in preview.columns
    assert list(preview["validation_errors"]) == [
        "",
        "measurement is empty",
        "measurement is NaN",
    ]
    assert len(at.metric) == 1
    assert at.metric[0].label == "Rows containing validation errors"
    assert at.metric[0].value == "2"


@pytest.mark.integration
def test_streamlit_provides_resulting_csv_download() -> None:
    at = AppTest.from_file(STREAMLIT_APP_PATH).run()

    at.file_uploader[0].set_value(("input.csv", CSV_UPLOAD, "text/csv")).run()
    at.selectbox[0].set_value("measurement").run()

    assert len(at.download_button) == 1
    assert at.download_button[0].label == "Download resulting CSV"

    resulting_csv = streamlit_interface.resulting_csv_text(
        [
            {"sample": "a", "measurement": "1.25", "validation_errors": ""},
            {"sample": "b", "measurement": "", "validation_errors": "measurement is empty"},
            {"sample": "c", "measurement": "NaN", "validation_errors": "measurement is NaN"},
        ],
        ["sample", "measurement", "notes"],
    )

    assert resulting_csv.splitlines() == [
        "sample,measurement,notes,validation_errors",
        "a,1.25,,",
        "b,,,measurement is empty",
        "c,NaN,,measurement is NaN",
    ]
