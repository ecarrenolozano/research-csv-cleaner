"""Streamlit interface entry point for Research CSV Cleaner."""

import streamlit as st


def main() -> None:
    """Run the local Streamlit interface shell."""
    st.set_page_config(page_title="Research CSV Cleaner")
    st.title("Research CSV Cleaner")


if __name__ == "__main__":
    main()
