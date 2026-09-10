"""Streamlit interface entry point for Research CSV Cleaner."""

import csv
from io import StringIO

import streamlit as st
from streamlit.runtime.uploaded_file_manager import UploadedFile

from research_csv_cleaner.cli_application import VALIDATION_ERRORS_COLUMN, clean_rows


def read_uploaded_csv(uploaded_file: UploadedFile) -> tuple[list[str], list[dict[str, str | None]]]:
    """Read CSV headers and rows from a Streamlit uploaded file."""
    text = uploaded_file.getvalue().decode("utf-8")
    reader = csv.DictReader(StringIO(text))
    return list(reader.fieldnames or []), list(reader)


def resulting_csv_text(
    rows: list[dict[str, str | None]],
    fieldnames: list[str],
) -> str:
    """Serialize validated rows for Streamlit CSV download."""
    output = StringIO()
    output_fieldnames = list(fieldnames)
    if VALIDATION_ERRORS_COLUMN not in output_fieldnames:
        output_fieldnames.append(VALIDATION_ERRORS_COLUMN)

    writer = csv.DictWriter(output, fieldnames=output_fieldnames)
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue()


def main() -> None:
    """Run the local Streamlit interface shell."""
    st.set_page_config(page_title="Research CSV Cleaner")
    st.title("Research CSV Cleaner")
    uploaded_file = st.file_uploader("Upload CSV file", type="csv")
    if uploaded_file is None:
        return

    fieldnames, rows = read_uploaded_csv(uploaded_file)
    selected_column = st.selectbox("Numeric column", fieldnames)
    validated_rows, validation_error_row_count = clean_rows(rows, selected_column)
    st.dataframe(validated_rows)
    st.metric("Rows containing validation errors", validation_error_row_count)
    st.download_button(
        "Download resulting CSV",
        data=resulting_csv_text(validated_rows, fieldnames),
        file_name="validated.csv",
        mime="text/csv",
    )


if __name__ == "__main__":
    main()
