# ADR-001: Local Dual-Interface Application

- **Status:** Accepted
- **Date:** 2026-09-09
- **Decision owners:** Architecture draft for CR-0001
- **Related capabilities:** CAP-006, CAP-007, CAP-008, CAP-009, CAP-010, CAP-011, CAP-012, CAP-013, CAP-014, CAP-015, CAP-016, CAP-017
- **Affected architecture elements:** AE-002 CLI Application, AE-003 Streamlit Interface

## Context

REQ-0002 requires the existing CLI to remain operational and also requires a small Streamlit interface for upload, selected-column input, validated-data preview, validation-error count display, and resulting CSV download.

REQ-0002 also changes the validation behavior: invalid rows are preserved, invalid rows receive detailed `validation_errors` explanations, and row counts describe rows containing validation errors.

## Decision Drivers

- Preserve the existing command-line workflow.
- Add the required local Streamlit interface.
- Keep validation behavior consistent across both interfaces.
- Avoid unapproved shared infrastructure, databases, remote APIs, or a shared web service.
- Keep the system small, testable, and understandable.

## Considered Options

- Keep only the CLI and add flags for preview/download-like behavior.
- Replace the CLI with a Streamlit-only interface.
- Add a local Streamlit interface alongside the CLI and share validation semantics in product-owned code.
- Add a separate backend service used by both interfaces.

## Decision

Use two local entry-point containers inside Research CSV Cleaner:

- AE-002 CLI Application.
- AE-003 Streamlit Interface.

Both entry points use shared validation semantics in product-owned code. No separate backend service, database, remote API, or shared deployment infrastructure is introduced.

## Consequences

### Positive

- The existing CLI workflow remains available.
- Researchers gain the requested local Streamlit interface.
- Shared validation semantics reduce the risk of CLI and Streamlit results diverging.
- The architecture stays local and small.

### Negative

- The product has a second runtime entry point.
- Streamlit introduces a runtime dependency.

### Risks

- Validation behavior can drift if implementation duplicates logic between interfaces.
- Large CSV behavior remains unspecified.

## Validation

ARCH-002 maps CAP-006 through CAP-017 to AE-002 and AE-003. The architecture package validator is the deterministic check for this mapping.

## Supersedes

DEC-001 is superseded only where it limited the product to a CLI-only interface. The CLI remains supported.

## Superseded By

None.
