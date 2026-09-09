"""Technical smoke tests for the CLI application module."""

from collections.abc import Callable

from research_csv_cleaner import cli_application


def test_cli_application_exposes_main_entry_point() -> None:
    assert isinstance(cli_application.main, Callable)
