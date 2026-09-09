# CLI Application Architecture

- **Structurizr container identifier:** cli
- **Container folder:** cli-application
- **Decision status:** Confirmed architect decision
- **Evidence basis:** REQ-0002; CAP-006, CAP-007, CAP-008, CAP-009, CAP-010, CAP-012, CAP-017; ADR-001.

## Container Identity

AE-002 is the local command-line execution container inside Research CSV Cleaner.

## Purpose

Validate one research CSV through the existing command-line workflow while producing CR-0001 row-preserving output.

## Responsibilities

Read CSV input, accept the selected numeric column from CLI arguments, apply shared validation semantics, preserve all rows, add detailed `validation_errors` values for invalid rows, write the resulting CSV, and report validation-error row count.

## Covered Capabilities and Stories

CAP-006 / US-0006; CAP-007 / US-0007; CAP-008 / US-0008; CAP-009 / US-0009; CAP-010 / US-0010; CAP-012 / US-0012; CAP-017 / US-0017.

## Interfaces Provided

CLI accepting the existing input shape: input CSV path, output CSV path, and selected numeric column name. The output behavior follows REQ-0002 instead of the superseded row-removal behavior.

## Interfaces Consumed

Local filesystem and Python runtime facilities. No external services.

## Data Ownership

The researcher supplies local files. The CLI reads the input file, creates a resulting CSV, and owns only per-run working data.

## Dependencies

Python runtime and product-owned validation logic. Exact standard-library or package use belongs to implementation design.

## Internal Building Blocks

Argument handling, CSV reading/writing, validation, annotation, and counting are internal responsibilities. No material internal boundary requires a Component view.

## Runtime Responsibilities

Verify selected-column presence before producing a result. Preserve all input rows. Annotate invalid rows with detailed explanations for missing, empty, unparseable, NaN, or infinite selected-column values. Report the number of rows containing validation errors.

## Quality Attributes

Small, testable, understandable, with validation behavior consistent with the Streamlit Interface.

## Constraints

Local individual-file operation; keep the existing CLI operational; no database, shared web service, or shared deployment infrastructure.

## Risks and Technical Debt

Exact CLI text, output-path edge cases, CSV dialect, encoding, malformed-file behavior, and large-file handling remain unspecified beyond approved requirements.

## Related ADR

ADR-001.

## Open Decisions

No material architecture decisions remain for this container.
