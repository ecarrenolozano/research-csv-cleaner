"""Command-line application for Research CSV Cleaner."""

import argparse
import csv
import math
import sys
from collections.abc import Sequence
from pathlib import Path

CsvRow = dict[str, str | None]


def is_valid_numeric_value(value: str | None) -> bool:
    """Return whether a CSV cell contains a finite floating-point value."""
    if value is None:
        return False

    text = value.strip()
    if text == "":
        return False

    try:
        parsed = float(text)
    except ValueError:
        return False

    return math.isfinite(parsed)


def clean_rows(rows: Sequence[CsvRow], required_column: str) -> tuple[list[CsvRow], int]:
    """Return rows with valid required-column values and the removal count."""
    if rows and required_column not in rows[0]:
        raise ValueError(f"Required numeric column is missing: {required_column}")

    clean = [row for row in rows if is_valid_numeric_value(row.get(required_column))]
    return clean, len(rows) - len(clean)


def clean_csv(input_path: Path, output_path: Path, required_column: str) -> int:
    """Clean a CSV file and return the number of removed rows."""
    with input_path.open(newline="") as input_file:
        reader = csv.DictReader(input_file)
        fieldnames = reader.fieldnames or []
        if required_column not in fieldnames:
            raise ValueError(f"Required numeric column is missing: {required_column}")

        rows = list(reader)
        clean, removed_count = clean_rows(rows, required_column)

    with output_path.open("w", newline="") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(clean)

    return removed_count


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line argument parser."""
    parser = argparse.ArgumentParser(description="Clean a research CSV file.")
    parser.add_argument("input_csv", type=Path)
    parser.add_argument("output_csv", type=Path)
    parser.add_argument("required_numeric_column")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the command-line application."""
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        removed_count = clean_csv(
            args.input_csv,
            args.output_csv,
            args.required_numeric_column,
        )
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    print(f"Removed rows: {removed_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
