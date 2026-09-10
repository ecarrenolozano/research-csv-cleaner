"""Technical smoke tests for the Streamlit interface module."""

from collections.abc import Callable

from research_csv_cleaner import streamlit_interface


def test_streamlit_interface_exposes_main_entry_point() -> None:
    assert isinstance(streamlit_interface.main, Callable)
