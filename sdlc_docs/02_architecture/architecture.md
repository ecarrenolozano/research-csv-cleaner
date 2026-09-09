# Product Architecture

## Document Control

- **Project:** Research CSV Cleaner
- **Architecture baseline:** ARCH-001
- **Source Project Context:** `sdlc_docs/00_inception/project_context.md`
- **Source Product Requirements:** `sdlc_docs/01_requirements/product_requirements.md`
- **Last updated:** 2026-09-09
- **Architecture state:** Complete

## How to View This Architecture

The canonical model is `sdlc_docs/02_architecture/diagrams/workspace.dsl`.
With Docker and Docker Compose installed, run from the repository root:

```bash
docker compose -f sdlc_docs/02_architecture/diagrams/docker-compose.yml up
```

Open http://localhost:8080. Stop the viewer with:

```bash
docker compose -f sdlc_docs/02_architecture/diagrams/docker-compose.yml down
```

The viewer is documentation tooling, not product infrastructure. Docker has not been run; rendering has not been verified. No images have been exported.

## 1. Introduction and Goals

### 1.1 Requirements Overview

Confirmed requirement: REQ-0001 supplies five capabilities: read a local CSV, validate one required numeric column, remove invalid rows, write a cleaned CSV, and report removed rows. See the approved [Product Requirements](../01_requirements/product_requirements.md).

### 1.2 Quality Goals

Confirmed requirement: keep the tool small, testable, and easy to understand (Project Context sections 12–13). Consistent invalid-value handling follows US-0002 and US-0003. No performance or capacity thresholds have been agreed.

### 1.3 Stakeholders

Researchers use the tool. Edwin Carreño is the recorded requirements reviewer (Software Engineer). Architecture approval was recorded on 2026-09-09.

## 2. Constraints

Confirmed requirement: Python, local individual-file processing, no database, web service, GUI, shared workflow integration, or additional infrastructure (Project Context sections 11–13).

Confirmed architect decision: the developer selected a minimal CLI in chat on 2026-09-09; see DEC-001 below. This explicit instruction governs the interface refinement. The approved requirements remain unchanged.

Internal architecture constraint: use one process and Python standard-library facilities for argument handling, CSV I/O, and numeric validation. Architecture rationale: AE-002 can own the full small workflow without runtime services or third-party processing dependencies. Exact modules and command spelling belong to later implementation design.

## 3. Context and Scope

### 3.1 Business Context

A researcher supplies an experiment CSV and receives a cleaned CSV and removed-row count. The local filesystem holds input and output; it is an environmental resource, not a separately deployed product container.

**Structurizr view:** `SystemContext`

### 3.2 Technical Context

DEC-001 specifies a command-line interface accepting an input CSV path, an output CSV path, and the required numeric column name. Local filesystem I/O connects the application to those files. US-0002 requires a clear error and no output file when the column is absent. No network integration is required.

## 4. Solution Strategy

Confirmed architect decision: use a single local CLI application (AE-002) containing the complete cleaning workflow. This is a small, reversible decomposition matching the local scope. Separate internal responsibilities enough for focused testing, without fixing packages or classes in this baseline. No material internal boundary or independent service is justified.

## 5. Building Block View

### 5.1 Whitebox Overall System

AE-001, Research CSV Cleaner, contains AE-002, CLI Application. Its documentation is [containers/cli-application/architecture.md](containers/cli-application/architecture.md).

**Structurizr view:** `Containers`

### 5.2 Level 2

Within the application, argument handling, CSV reading/writing, numeric validation, row filtering, and counting are responsibilities rather than separate architectural components. Implementation design may choose a testable arrangement.

### 5.3 Level 3

Not applicable: deeper decomposition would prescribe implementation detail without resolving a material architecture risk. No Component view is needed.

## 6. Runtime View

Successful run: accept the three CLI inputs (DEC-001); read CSV (US-0001); check the required column and classify values (US-0002); exclude invalid rows (US-0003); write cleaned CSV (US-0004); report removed-row count (US-0005).

Missing column: establish column presence before creating output. If absent, fail with a clear error and create no output file (US-0002).

Invalid values: missing, empty, unparseable floating-point values, NaN, and infinities are invalid (US-0002/US-0003). Numerical parsing is used for validation; this architecture adds no value-normalization contract.

A prose sequence is sufficient; no Dynamic view is necessary.

## 7. Deployment View

Confirmed requirement: execution occurs on the researcher's local machine. AE-002 runs as one Python process and accesses local files. No separate infrastructure is needed. Installation packaging is deferred to the technical foundation and release stages. A separate Deployment view adds no material information to this single-host design.

## 8. Crosscutting Concepts

| Concept | Classification | Evidence | Architecture approach |
|---|---|---|---|
| Numeric validity | Confirmed requirement | US-0002, US-0003 | Apply the same invalid-value classification before filtering. |
| Missing column | Confirmed requirement | US-0002 | Check the column before opening output for creation. |
| Removed-row accounting | Confirmed requirement | US-0005 | Count rows excluded during this run and report that count. |
| Local execution | Confirmed requirement | Project Context sections 11–13 | Operate within the local filesystem and Python process. |
| Testable internal responsibilities | Internal architecture constraint | Architecture rationale: AE-002 | Keep numeric classification and I/O responsibilities independently exercisable without imposing a material component boundary. |
| Shared persistence and authentication | Not applicable | Project Context section 11 | There is no shared service or database in this release. |

## 9. Architectural Decisions

DEC-001: developer-selected CLI with three inputs, recorded verbatim below. AE-002 uses one process and standard-library facilities to keep the implementation small. These choices do not warrant separate ADRs: there is no costly or hard-to-reverse technology commitment or material internal boundary. See [ADR index](adr/README.md).

## 10. Quality Requirements

### 10.1 Quality Requirements Overview

Confirmed requirement: small, testable, understandable implementation; correct execution of all five approved capabilities. No additional quality thresholds are introduced.

### 10.2 Quality Scenarios

For the invalid numeric cases in US-0002/US-0003, validation identifies the row as invalid and filtering excludes it. For a missing column, US-0002 produces a clear failure without output creation. These restate approved acceptance criteria rather than adding guarantees. Internal review should assess whether responsibilities can be tested in isolation; the test design belongs to implementation.

## 11. Risks and Technical Debt

CSV dialect, encoding, malformed-file handling, overwrite/same-path behavior, and exact CLI/error/count formatting are not specified in approved requirements. This baseline adds no promises for these cases. Before implementing affected behavior, the implementer must identify which decisions need requirements clarification, particularly where file loss could result. These do not change the present one-process architecture.

Large-file capacity is unquantified; no memory or throughput guarantee is claimed. The existing sample entry point is not implementation evidence. No technical debt is accepted by this baseline. No material architecture decisions remain open.

## 12. Glossary

- **Required numeric column:** the column selected for validation in a run.
- **Invalid row:** a row whose required-column value meets an approved invalid-value condition.
- **Container:** a C4 execution/data boundary; here it means the CLI application, not a Docker product deployment.

# Workflow Extensions

## Developer Interface Decision

- **Decision ID:** DEC-001
- **Classification:** Confirmed architect decision
- **Source:** Developer response in this conversation, 2026-09-09.
- **Exact instruction:** “Use a command-line interface for the first release. Keep the interface minimal: the user provides an input CSV path, an output CSV path, and the name of the required numeric column.”
- **Impact:** Resolves the architecture interface question and selects the interface for existing US-0001, US-0002, and US-0004. It does not approve this complete architecture baseline. No new capabilities or story identifiers are introduced.

## Architecture Element Register

| Element ID | Type | Name | Evidence IDs | Decision status | ADR or open decision |
|---|---|---|---|---|---|
| AE-001 | Software System | Research CSV Cleaner | REQ-0001 | Confirmed requirement | None |
| AE-002 | Container | CLI Application | CAP-001, CAP-002, CAP-003, CAP-004, CAP-005; DEC-001 | Confirmed architect decision | No ADR warranted for this reversible single-process structure |

## Requirements-to-Architecture Coverage

| Capability | Stories | Architecture elements | Coverage | Evidence |
|---|---|---|---|---|
| CAP-001 | US-0001 | AE-002 | Covered | CSV input responsibility |
| CAP-002 | US-0002 | AE-002 | Covered | Required-column and numeric validation |
| CAP-003 | US-0003 | AE-002 | Covered | Invalid-row filtering |
| CAP-004 | US-0004 | AE-002 | Covered | Cleaned CSV output responsibility |
| CAP-005 | US-0005 | AE-002 | Covered | Removed-row accounting and reporting |

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

Product behavior derives from approved US-0001–US-0005, with the CLI refinement explicitly authorized by DEC-001. No other user-visible behavior is introduced. Structural validation does not establish runtime correctness or successful diagram rendering.

## Approval Record

| Architecture baseline | Decision | Approved by | Role or responsibility | Date | Blocking Issues or Feedback |
|---|---|---|---|---|---|
| ARCH-001 | Approved | Edwin Carreño | Software developer | 2026-09-09 | None |
