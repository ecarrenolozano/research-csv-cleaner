# Product Architecture

## Document Control

- **Project:** Research CSV Cleaner
- **Architecture baseline:** ARCH-002
- **Source Project Context:** `sdlc_docs/00_inception/project_context.md`
- **Source Product Requirements:** `sdlc_docs/01_requirements/product_requirements.md`
- **Last updated:** 2026-09-09
- **Architecture state:** Complete

## How to View This Architecture

The canonical architecture model is `sdlc_docs/02_architecture/diagrams/workspace.dsl`.

With Docker and Docker Compose installed, run from the repository root:

```bash
docker compose -f sdlc_docs/02_architecture/diagrams/docker-compose.yml up
```

Open http://localhost:8080. Stop the viewer with:

```bash
docker compose -f sdlc_docs/02_architecture/diagrams/docker-compose.yml down
```

The viewer is documentation tooling, not product infrastructure. Docker has not been run during this architecture update. No images have been exported.

## 1. Introduction and Goals

### 1.1 Requirements Overview

Confirmed requirement: REQ-0002 supplies CR-0001 behavior for local CSV validation with row preservation, validation-error explanations, CLI continuity, and a small Streamlit interface. It covers CAP-006 through CAP-017 and US-0006 through US-0017. REQ-0001 is preserved as historical initial-release scope and superseded for active behavior.

### 1.2 Quality Goals

Confirmed requirement: keep the implementation small, testable, and easy to understand. Consistent numeric validation must apply across the CLI and Streamlit interface. No performance, capacity, accessibility, browser-support, or large-file thresholds have been approved.

### 1.3 Stakeholders

Researchers use the tool. Edwin Carreño is the recorded reviewer for the CR-0001 Project Context, Product Requirements, and ARCH-002 architecture approval.

## 2. Constraints

Confirmed requirement: the tool runs locally on individual CSV files, preserves all input rows, explains invalid numeric values in `validation_errors`, reports or displays validation-error row count, keeps the existing CLI operational, and adds a small Streamlit interface.

Confirmed requirement: no shared workflow integration, database, web service, or shared deployment infrastructure is required. The Streamlit interface is a local user interface, not a shared web service.

Confirmed architect decision: use two local entry-point containers inside the same software system: AE-002 CLI Application and AE-003 Streamlit Interface. Both delegate validation semantics to shared application logic at implementation time so that CAP-007, CAP-008, CAP-009, and counting behavior stay consistent. See ADR-001.

## 3. Context and Scope

### 3.1 Business Context

A researcher supplies an experiment CSV and receives a resulting CSV. The resulting CSV keeps every input row and marks invalid numeric values in `validation_errors`. The researcher can run the existing CLI workflow or use the local Streamlit interface for upload, selection, preview, count display, and download.

**Structurizr view:** `SystemContext`

### 3.2 Technical Context

The software system runs on the researcher's local machine. The CLI consumes local input/output paths and a selected numeric column. The Streamlit interface consumes an uploaded CSV file and the selected numeric column, then previews and downloads the resulting CSV. Both interfaces rely on local Python runtime facilities and product-owned validation logic. No external system, remote API, database, or shared server is in scope.

## 4. Solution Strategy

Use one local Python software system with two user-facing entry points:

- AE-002 CLI Application for existing command-line workflows.
- AE-003 Streamlit Interface for local upload, selection, preview, count display, and download.

The row-validation transformation is an internal responsibility shared by both entry points. Keeping it shared avoids divergent validation behavior while avoiding a separate service or database that the approved scope does not require.

## 5. Building Block View

### 5.1 Whitebox Overall System

AE-001, Research CSV Cleaner, contains AE-002, CLI Application, and AE-003, Streamlit Interface. Their documentation lives in [containers/cli-application/architecture.md](containers/cli-application/architecture.md) and [containers/streamlit-interface/architecture.md](containers/streamlit-interface/architecture.md).

**Structurizr view:** `Containers`

### 5.2 Level 2

AE-002 handles command-line argument intake, local CSV file reading and writing, error reporting, and validation-error row count reporting.

AE-003 handles local Streamlit upload, selected-column input, validation preview, validation-error row count display, and resulting CSV download.

CSV parsing, selected-column validation, row preservation, `validation_errors` annotation, and validation-error row counting are shared internal responsibilities. The exact module, function, and packaging names remain implementation design.

### 5.3 Level 3

A Component view is not needed for ARCH-002. The material architecture question is the local entry-point set, not a hard internal component boundary. Shared validation logic is a code-organization responsibility to be designed during implementation.

## 6. Runtime View

CLI run: accept the existing CLI inputs, read the input CSV, verify the selected column, validate each selected-column value, preserve every row, add or populate `validation_errors`, write the resulting CSV, and report how many rows contain validation errors.

Streamlit run: accept an uploaded CSV, allow numeric-column selection, validate each selected-column value, preserve every row, add or populate `validation_errors`, preview the validated data, display how many rows contain validation errors, and provide the resulting CSV for download.

Missing selected column: fail with a clear error and avoid creating a resulting CSV, following US-0007. Streamlit should surface the validation failure within the local interface rather than producing a misleading result.

Invalid values: missing, empty, unparseable floating-point values, NaN, and infinities are invalid. Each invalid row needs a detailed explanation of the specific invalid numeric problem in `validation_errors`.

## 7. Deployment View

Confirmed requirement: execution occurs on the researcher's local machine. The CLI runs as a local Python command. The Streamlit interface runs locally as a Streamlit process. No database, shared web service, remote hosting, or shared deployment infrastructure is part of this architecture.

A separate Deployment view is not needed because there is one local machine environment and no approved deployment topology beyond local execution.

## 8. Crosscutting Concepts

| Concept | Classification | Evidence | Architecture approach |
|---|---|---|---|
| Numeric validity | Confirmed requirement | CAP-007, US-0007, Product Requirements | Apply the same invalid-value classification for both local interfaces. |
| Row preservation | Confirmed requirement | CAP-008, US-0008, Product Requirements | Transform rows by annotation instead of filtering. |
| Validation-error explanations | Confirmed requirement | CAP-009, US-0009, Product Requirements | Populate `validation_errors` for invalid rows with the specific invalid numeric problem. |
| Validation-error row count | Confirmed requirement | CAP-012, CAP-013, US-0012, US-0013 | Count rows with validation errors and expose the count through the active interface. |
| CLI continuity | Confirmed requirement | CAP-017, US-0017, Product Requirements | Keep a command-line entry point that accepts the existing run shape while producing CR-0001 output. |
| Local Streamlit interface | Confirmed requirement | CAP-011, CAP-013, CAP-014, CAP-015, CAP-016 | Provide a local Streamlit entry point for upload, selection, preview, count display, and download. |
| Shared validation semantics | Confirmed architect decision | ADR-001 | Keep validation and annotation behavior shared by the CLI and Streamlit entry points. |
| Shared persistence and authentication | Not applicable | Project Context sections 11-13 | No shared service, database, account model, or authentication boundary is part of this scope. |

## 9. Architectural Decisions

ADR-001 selects a local dual-interface architecture: preserve the existing CLI container, add a Streamlit Interface container, and keep validation semantics shared inside the product code. This supersedes DEC-001 only where DEC-001 limited the product to a CLI-only interface. The CLI itself remains part of the architecture.

No additional ADR is needed for a database, remote API, or deployment platform because those options are outside the approved scope.

## 10. Quality Requirements

### 10.1 Quality Requirements Overview

The architecture must support the approved CR-0001 capabilities while keeping the implementation small, testable, and understandable. The most important quality concern is consistent validation behavior across both local entry points.

### 10.2 Quality Scenarios

For the same input CSV and selected numeric column, the CLI and Streamlit interface should produce equivalent validation-error annotations and row counts. For a missing selected column, each interface should avoid producing a resulting CSV and make the failure clear. These scenarios restate approved behavior rather than adding capacity or formatting guarantees.

## 11. Risks and Technical Debt

CSV dialect, encoding, malformed-file handling, overwrite or same-path behavior, exact CLI output text, exact Streamlit layout, and large-file capacity remain unspecified beyond approved acceptance criteria. Implementation must avoid adding stronger guarantees for these cases without requirements clarification.

The Streamlit interface adds a runtime dependency and a second local entry point. The main risk is duplicated validation behavior; ADR-001 addresses this by requiring shared validation semantics.

No accepted technical debt is added by ARCH-002.

## 12. Glossary

- **Selected numeric column:** the CSV column chosen for validation in a run.
- **Invalid row:** a row whose selected-column value meets an approved invalid-value condition.
- **Validation errors:** row-level explanations stored in the `validation_errors` column for detected invalid numeric values.
- **Resulting CSV:** the CSV produced after validation; it preserves all input rows and includes validation-error annotations.
- **Container:** a C4 execution boundary; here it means a local CLI process or local Streamlit process, not a Docker product deployment.

# Workflow Extensions

## Architecture Element Register

| Element ID | Type | Name | Evidence IDs | Decision status | ADR or open decision |
|---|---|---|---|---|---|
| AE-001 | Software System | Research CSV Cleaner | REQ-0002 | Confirmed requirement | None |
| AE-002 | Container | CLI Application | CAP-006, CAP-007, CAP-008, CAP-009, CAP-010, CAP-012, CAP-017; ADR-001 | Confirmed architect decision | ADR-001 |
| AE-003 | Container | Streamlit Interface | CAP-006, CAP-007, CAP-008, CAP-009, CAP-011, CAP-013, CAP-014, CAP-015, CAP-016; ADR-001 | Confirmed architect decision | ADR-001 |

## Requirements-to-Architecture Coverage

| Capability | Stories | Architecture elements | Coverage | Evidence |
|---|---|---|---|---|
| CAP-001 | US-0001 | ARCH-001 historical baseline | Covered | Superseded historical capability from REQ-0001; preserved for traceability only. |
| CAP-002 | US-0002 | ARCH-001 historical baseline | Covered | Superseded historical capability from REQ-0001; preserved for traceability only. |
| CAP-003 | US-0003 | ARCH-001 historical baseline | Covered | Superseded historical capability from REQ-0001; preserved for traceability only. |
| CAP-004 | US-0004 | ARCH-001 historical baseline | Covered | Superseded historical capability from REQ-0001; preserved for traceability only. |
| CAP-005 | US-0005 | ARCH-001 historical baseline | Covered | Superseded historical capability from REQ-0001; preserved for traceability only. |
| CAP-006 | US-0006 | AE-002, AE-003 | Covered | Both interfaces read CSV input through their local entry-point mechanisms. |
| CAP-007 | US-0007 | AE-002, AE-003 | Covered | Both interfaces use shared selected-column validation semantics. |
| CAP-008 | US-0008 | AE-002, AE-003 | Covered | Shared validation transformation preserves all rows for both interfaces. |
| CAP-009 | US-0009 | AE-002, AE-003 | Covered | Shared validation transformation annotates invalid rows with detailed validation errors. |
| CAP-010 | US-0010 | AE-002 | Covered | CLI Application writes the resulting CSV file. |
| CAP-011 | US-0011 | AE-003 | Covered | Streamlit Interface provides resulting CSV download. |
| CAP-012 | US-0012 | AE-002 | Covered | CLI Application reports validation-error row count. |
| CAP-013 | US-0013 | AE-003 | Covered | Streamlit Interface displays validation-error row count. |
| CAP-014 | US-0014 | AE-003 | Covered | Streamlit Interface accepts uploaded CSV files. |
| CAP-015 | US-0015 | AE-003 | Covered | Streamlit Interface accepts selected numeric column input. |
| CAP-016 | US-0016 | AE-003 | Covered | Streamlit Interface previews validated data. |
| CAP-017 | US-0017 | AE-002 | Covered | CLI Application remains a supported local entry point. |

## Architecture Validation

- **arc42 structure validator:** Passed
- **Container structure validator:** Passed
- **Structurizr model validator:** Passed
- **Diagram documentation validator:** Passed
- **Docker Compose validator:** Passed
- **Architecture hygiene validator:** Passed
- **Product behavior discipline validator:** Passed
- **Architecture package validator command:** `python3 .agents/skills/d-design-product-architecture/scripts/validate_architecture_package.py sdlc_docs/00_inception/project_context.md sdlc_docs/01_requirements/product_requirements.md sdlc_docs/02_architecture --require-report-sync`
- **Validation report synchronized:** Yes
- **Unresolved material decisions:** 0
- **Unsupported product behavior introduced:** 0
- **Validation result:** Passed

Product behavior derives from approved REQ-0002 and US-0006 through US-0017. ARCH-002 adds no user-visible behavior beyond the approved CR-0001 requirements. Structural validation does not establish runtime correctness or successful diagram rendering.

## Approval Record

| Architecture baseline | Decision | Approved by | Role or responsibility | Date | Blocking Issues or Feedback |
|---|---|---|---|---|---|
| ARCH-001 | Approved, superseded by ARCH-002 | Edwin Carreño | Software developer | 2026-09-09 | None |
| ARCH-002 | Approved | Edwin Carreño | Software developer | 2026-09-09 | None |
