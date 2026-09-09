"""Technical smoke tests for package metadata."""

from research_csv_cleaner import __version__


def test_package_exposes_current_version() -> None:
    assert __version__ == "0.1.0"
