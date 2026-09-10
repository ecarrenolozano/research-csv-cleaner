"""Unit tests for CSV cleaning rules."""

import pytest

from research_csv_cleaner.cli_application import clean_rows, is_valid_numeric_value


@pytest.mark.unit
@pytest.mark.parametrize("value", ["0", "1.25", "-3", "1e-3"])
def test_numeric_value_accepts_finite_float_strings(value: str) -> None:
    assert is_valid_numeric_value(value)


@pytest.mark.unit
@pytest.mark.parametrize(
    "value",
    [None, "", "   ", "abc", "NaN", "nan", "inf", "-inf", "Infinity"],
)
def test_numeric_value_rejects_missing_empty_unparseable_nan_and_infinity(
    value: str | None,
) -> None:
    assert not is_valid_numeric_value(value)


@pytest.mark.unit
def test_clean_rows_preserves_invalid_required_column_rows_and_counts_them() -> None:
    rows = [
        {"sample": "a", "measurement": "1.25"},
        {"sample": "b", "measurement": ""},
        {"sample": "c", "measurement": "NaN"},
        {"sample": "d", "measurement": "5"},
    ]

    clean, removed_count = clean_rows(rows, required_column="measurement")

    assert len(clean) == len(rows)
    assert [row["sample"] for row in clean] == ["a", "b", "c", "d"]
    assert removed_count == 2


@pytest.mark.unit
def test_clean_rows_adds_validation_error_explanations_for_invalid_values() -> None:
    rows = [
        {"sample": "valid", "measurement": "42"},
        {"sample": "missing", "measurement": None},
        {"sample": "empty", "measurement": ""},
        {"sample": "text", "measurement": "abc"},
        {"sample": "nan", "measurement": "NaN"},
        {"sample": "infinite", "measurement": "inf"},
    ]

    clean, invalid_count = clean_rows(rows, required_column="measurement")

    assert invalid_count == 5
    assert clean[0]["validation_errors"] == ""
    assert clean[1]["validation_errors"] == "measurement is missing"
    assert clean[2]["validation_errors"] == "measurement is empty"
    assert clean[3]["validation_errors"] == "measurement is not a number"
    assert clean[4]["validation_errors"] == "measurement is NaN"
    assert clean[5]["validation_errors"] == "measurement is infinite"


@pytest.mark.unit
def test_clean_rows_raises_clear_error_when_required_column_is_absent() -> None:
    rows = [{"sample": "a", "notes": "missing measurement column"}]

    with pytest.raises(ValueError, match="measurement"):
        clean_rows(rows, required_column="measurement")
