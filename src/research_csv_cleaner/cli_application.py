"""Command-line application for Research CSV Cleaner."""

import argparse
import csv
import math
import sys
from collections.abc import Mapping, Sequence
from pathlib import Path

CsvRow = dict[str, str | None]
CsvInputRow = Mapping[str, str | None]
VALIDATION_ERRORS_COLUMN = "validation_errors"


def validation_error_for_numeric_value(value: str | None, column: str) -> str | None:
    """Return a specific validation error for one selected numeric-column value."""
    if value is None:
        return f"{column} is missing"

    text = value.strip()
    if text == "":
        return f"{column} is empty"

    try:
        parsed = float(text)
    except ValueError:
        return f"{column} is not a number"

    if math.isnan(parsed):
        return f"{column} is NaN"

    if math.isinf(parsed):
        return f"{column} is infinite"

    return None


def is_valid_numeric_value(value: str | None) -> bool:
    """Return whether a CSV cell contains a finite floating-point value."""
    return validation_error_for_numeric_value(value, "value") is None


def clean_rows(rows: Sequence[CsvInputRow], required_column: str) -> tuple[list[CsvRow], int]:
    """Return annotated rows and the invalid required-column value count."""
    if rows and required_column not in rows[0]:
        raise ValueError(f"Required numeric column is missing: {required_column}")

    annotated_rows: list[CsvRow] = []
    invalid_count = 0
    for row in rows:
        error = validation_error_for_numeric_value(row.get(required_column), required_column)
        if error is not None:
            invalid_count += 1

        annotated_rows.append({**dict(row), VALIDATION_ERRORS_COLUMN: error or ""})

    return annotated_rows, invalid_count


def clean_csv(input_path: Path, output_path: Path, required_column: str) -> int:
    """Validate a CSV file and return the invalid selected-column value count."""
    with input_path.open(newline="") as input_file:
        reader = csv.DictReader(input_file)
        fieldnames = reader.fieldnames or []
        if required_column not in fieldnames:
            raise ValueError(f"Required numeric column is missing: {required_column}")

        rows = list(reader)
        clean, removed_count = clean_rows(rows, required_column)
        output_fieldnames = list(fieldnames)
        if VALIDATION_ERRORS_COLUMN not in output_fieldnames:
            output_fieldnames.append(VALIDATION_ERRORS_COLUMN)

    with output_path.open("w", newline="") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=output_fieldnames)
        writer.writeheader()
        writer.writerows(clean)

    return removed_count


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line argument parser."""
    parser = argparse.ArgumentParser(description="Validate a research CSV file.")
    parser.add_argument("input_csv", type=Path)
    parser.add_argument("output_csv", type=Path)
    parser.add_argument("required_numeric_column")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the command-line application."""
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        validation_error_row_count = clean_csv(
            args.input_csv,
            args.output_csv,
            args.required_numeric_column,
        )
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    print(f"Rows containing validation errors: {validation_error_row_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
