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
def test_clean_rows_excludes_invalid_required_column_values_and_counts_removed_rows() -> None:
    rows = [
        {"sample": "a", "measurement": "1.25"},
        {"sample": "b", "measurement": ""},
        {"sample": "c", "measurement": "NaN"},
        {"sample": "d", "measurement": "5"},
    ]

    clean, removed_count = clean_rows(rows, required_column="measurement")

    assert clean == [
        {"sample": "a", "measurement": "1.25"},
        {"sample": "d", "measurement": "5"},
    ]
    assert removed_count == 2


@pytest.mark.unit
def test_clean_rows_raises_clear_error_when_required_column_is_absent() -> None:
    rows = [{"sample": "a", "notes": "missing measurement column"}]

    with pytest.raises(ValueError, match="measurement"):
        clean_rows(rows, required_column="measurement")
