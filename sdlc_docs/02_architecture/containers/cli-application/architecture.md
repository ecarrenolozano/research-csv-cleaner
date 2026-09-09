# CLI Application Architecture

- **Structurizr container identifier:** cli
- **Container folder:** cli-application
- **Decision status:** Confirmed architect decision
- **Evidence basis:** REQ-0001; CAP-001–CAP-005; DEC-001 in the root architecture.

## Container Identity

AE-002 is the single local Python execution container inside Research CSV Cleaner.

## Purpose

Clean one research CSV through the developer-selected minimal CLI.

## Responsibilities

Read CSV, validate the required numeric column, filter invalid rows, write cleaned CSV, and report the removed-row count.

## Covered Capabilities and Stories

CAP-001 / US-0001; CAP-002 / US-0002; CAP-003 / US-0003; CAP-004 / US-0004; CAP-005 / US-0005.

## Interfaces Provided

DEC-001: CLI accepting input CSV path, output CSV path, and required numeric column name. Exact invocation spelling is deferred. Missing-column error and removed-row report follow US-0002 and US-0005.

## Interfaces Consumed

Local filesystem and Python runtime facilities. No external services.

## Data Ownership

The researcher supplies local files. The application reads the input and produces cleaned output; it owns only per-run working data, with no independent persistent store.

## Dependencies

Internal architecture constraint: Python standard library for CLI argument handling, CSV I/O, and numeric validation. Exact implementation APIs remain for implementation design.

## Internal Building Blocks

I/O, numeric classification, filtering, and accounting are internal responsibilities. No material internal boundary requires a Component view.

## Runtime Responsibilities

Verify column presence before output creation. Exclude missing, empty, unparseable, NaN, and infinite numeric values. Report excluded-row count after cleaning. See root runtime view for approved behavior provenance.

## Quality Attributes

Small, testable, understandable, as required by Project Context. No invented capacity target.

## Constraints

Local individual-file operation; three CLI inputs; no GUI, database, or web service.

## Risks and Technical Debt

Unspecified CSV and output-path edge cases require review before affected implementation; see root section 11. No accepted debt.

## Related ADR

None warranted. DEC-001 and the root architecture record the interface and simple structural rationale.

## Open Decisions

No material architecture decisions remain. Detailed command syntax and code decomposition belong to implementation design.
