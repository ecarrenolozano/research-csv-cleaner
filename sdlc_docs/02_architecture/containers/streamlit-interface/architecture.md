# Streamlit Interface Architecture

- **Structurizr container identifier:** streamlit
- **Container folder:** streamlit-interface
- **Decision status:** Confirmed architect decision
- **Evidence basis:** REQ-0002; CAP-006, CAP-007, CAP-008, CAP-009, CAP-011, CAP-013, CAP-014, CAP-015, CAP-016; ADR-001.

## Container Identity

AE-003 is the local Streamlit execution container inside Research CSV Cleaner.

## Purpose

Provide a small local interface for researchers who want to validate a CSV without using the command line.

## Responsibilities

Accept a CSV upload, allow selected numeric column input, apply shared validation semantics, preserve all rows, add detailed `validation_errors` values for invalid rows, preview validated data, display validation-error row count, and provide the resulting CSV for download.

## Covered Capabilities and Stories

CAP-006 / US-0006; CAP-007 / US-0007; CAP-008 / US-0008; CAP-009 / US-0009; CAP-011 / US-0011; CAP-013 / US-0013; CAP-014 / US-0014; CAP-015 / US-0015; CAP-016 / US-0016.

## Interfaces Provided

Local Streamlit user interface for CSV upload, selected-column input, validated-data preview, validation-error count display, and resulting CSV download.

## Interfaces Consumed

Uploaded CSV file content, local Python runtime facilities, Streamlit runtime, and product-owned validation logic. No external services.

## Data Ownership

The researcher supplies uploaded CSV content. The Streamlit interface owns only per-session working data and downloadable generated CSV content. No shared persistence is part of this container.

## Dependencies

Python runtime, Streamlit runtime, and product-owned validation logic. Exact dependency declaration belongs to technical foundation or implementation work.

## Internal Building Blocks

Upload handling, column selection, validation invocation, preview rendering, count display, and download generation are internal responsibilities. No material internal boundary requires a Component view.

## Runtime Responsibilities

Accept a researcher-uploaded CSV, allow numeric-column selection, validate selected-column values, preserve all rows, annotate invalid rows with detailed explanations for missing, empty, unparseable, NaN, or infinite values, display the count of rows containing validation errors, preview validated data, and provide the resulting CSV for download.

## Quality Attributes

Small, testable where practical, understandable, and consistent with CLI validation behavior.

## Constraints

Local Streamlit interface only; no shared workflow integration, database, shared web service, or shared deployment infrastructure.

## Risks and Technical Debt

Streamlit adds a runtime dependency and an interactive path. Exact page layout, upload limits, browser support, and large-file behavior remain unspecified beyond approved requirements.

## Related ADR

ADR-001.

## Open Decisions

No material architecture decisions remain for this container.
