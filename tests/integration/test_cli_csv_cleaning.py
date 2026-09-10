"""Integration tests for CLI CSV cleaning."""

import csv
from pathlib import Path

import pytest

from research_csv_cleaner import cli_application


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as csv_file:
        return list(csv.DictReader(csv_file))


@pytest.mark.integration
def test_cli_writes_resulting_csv_with_all_input_rows_and_reports_invalid_row_count(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    input_path = tmp_path / "input.csv"
    output_path = tmp_path / "cleaned.csv"
    write_csv(
        input_path,
        ["sample", "measurement"],
        [
            {"sample": "a", "measurement": "1.25"},
            {"sample": "b", "measurement": ""},
            {"sample": "c", "measurement": "NaN"},
            {"sample": "d", "measurement": "5"},
        ],
    )

    exit_code = cli_application.main([str(input_path), str(output_path), "measurement"])

    assert exit_code == 0
    assert read_csv(output_path) == [
        {"sample": "a", "measurement": "1.25", "validation_errors": ""},
        {"sample": "b", "measurement": "", "validation_errors": "measurement is empty"},
        {"sample": "c", "measurement": "NaN", "validation_errors": "measurement is NaN"},
        {"sample": "d", "measurement": "5", "validation_errors": ""},
    ]
    assert "2" in capsys.readouterr().out


@pytest.mark.integration
def test_cli_missing_required_column_reports_error_and_does_not_create_output_file(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    input_path = tmp_path / "input.csv"
    output_path = tmp_path / "cleaned.csv"
    write_csv(
        input_path,
        ["sample", "notes"],
        [{"sample": "a", "notes": "missing measurement column"}],
    )

    exit_code = cli_application.main([str(input_path), str(output_path), "measurement"])

    assert exit_code != 0
    assert not output_path.exists()
    error_output = capsys.readouterr().err
    assert "measurement" in error_output
    assert "missing" in error_output.lower()
