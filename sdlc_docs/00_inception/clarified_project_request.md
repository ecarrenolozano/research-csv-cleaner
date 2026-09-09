# Clarified Project Request

## Document Control

- **Document state:** Closed
- **Created:** 2026-09-09
- **Last updated:** 2026-09-09
- **Active change:** CR-0001

## Source Metadata

| Source | Type | Date | Provided by | Notes |
|---|---|---|---|---|
| [informal_project_request.md](sources/informal_project_request.md) | Informal request supplied in chat | 2026-09-09 | Requester | Original requirement preserved verbatim. |
| Direct chat clarification | Stakeholder answers supplied in chat | 2026-09-09 | Requester | Answers recorded for critical questions 1-3. |
| [change_request_cr_0001.md](sources/change_request_cr_0001.md) | Change request supplied in chat | 2026-09-09 | Requester | Requests preservation of invalid rows with validation errors, adds a Streamlit interface, and keeps the CLI operational. |

## Initial Understanding

The requester wants a small Python tool for researchers who receive experiment CSV files and currently clean them manually. The project should reduce the chance that invalid values are missed or handled inconsistently.

The first version will run locally on individual CSV files. It does not need integration with a shared workflow, database, web service, or GUI.

The first version is successful if it can read a CSV file, validate one required numeric column, remove rows with invalid values, write a cleaned CSV, and report how many rows were removed. The implementation should remain small, testable, and easy to understand. There is no special deadline beyond the workshop exercise and no additional infrastructure is required. Detailed definitions of invalid numeric values are deferred to requirements clarification.

## Critical Questions

### Question 1

- **Status:** Answered
- **Question:** Who will use the tool, and what problem does their current CSV-cleaning process cause?
- **Answer:** Researchers who receive CSV files from experiments and currently clean them manually. The main problem is that invalid values can be missed or handled inconsistently.
- **Answered by:** Requester (chat, 2026-09-09)
- **Impact:** Confirms the intended users and the project rationale.

### Question 2

- **Status:** Answered
- **Question:** What is the intended first-release usage boundary: a tool run locally on research files, or something integrated into a shared research workflow?
- **Answer:** The first version will run locally on individual CSV files. It does not need integration with a shared workflow, database, web service, or GUI.
- **Answered by:** Requester (chat, 2026-09-09)
- **Impact:** Confirms the initial release boundary and excludes shared workflow integration, database, web service, and GUI scope for the first version.

### Question 3

- **Status:** Answered
- **Question:** What outcome would make the first version successful, and are there any mandatory constraints or deadlines?
- **Answer:** The first version is successful if it can read a CSV file, validate one required numeric column, remove rows with invalid values, write a cleaned CSV, and report how many rows were removed. The implementation should be small, testable, and easy to understand. There is no special deadline beyond the workshop exercise, and no additional infrastructure is required.
- **Answered by:** Requester (chat, 2026-09-09)
- **Impact:** Confirms first-version success conditions and material constraints while leaving detailed validation rules for the requirements stage.

## Contradictions

CR-0001 contradicts the previously approved first-release behavior and scope in these ways:

- The initial request said invalid rows should be removed; CR-0001 says invalid rows must remain in the output CSV.
- The initial request said the tool should report how many rows were removed; CR-0001 says researchers need to see how many rows contain validation errors.
- The initial request excluded a GUI; CR-0001 requests a small Streamlit interface.

These contradictions require updated Project Context, Product Requirements, Product Architecture, acceptance criteria, validation tests, and implementation assumptions before code changes begin.

## Change Request CR-0001

### Initial Understanding

The requester wants the existing Research CSV Cleaner to preserve every input row in the generated CSV. Rows with invalid values in the selected numeric column should be annotated with a `validation_errors` column that explains the detected problem instead of being removed.

Researchers also need a small local Streamlit interface. The interface should allow CSV upload, numeric-column selection, validated-data preview, a count of rows containing validation errors, and download of the resulting CSV. The already implemented CLI must remain operational.

The change is a material product and architecture change. It supersedes the row-removal behavior for future work while preserving the initial release artifacts as approved history.

### Critical Questions

No blocking project-level questions are currently identified. Detailed acceptance-criterion wording belongs to Product Requirements after this change-intake record is approved.

### Impact

- Reopen Project Context because the approved context currently describes row removal and excludes GUI scope.
- Create a new product requirement or increment requirement rather than rewriting approved REQ-0001 in place.
- Retire or supersede the row-removal story behavior for future output.
- Add acceptance criteria for preserving all rows, populating `validation_errors`, reporting validation-error row count, Streamlit upload, numeric-column selection, preview, and download.
- Rework architecture because Streamlit introduces a local UI path and at least one runtime dependency.
- Update unit, integration, and BDD validation coverage before implementation is considered complete.

## Initial Release Readiness Approval

- [x] Ready
- [ ] Not Ready
- **Approver:** Edwin Carreño
- **Role:** Software developer
- **Approval date:** 2026-09-09
- **Blocking Issues:** None

## CR-0001 Readiness Approval

- [x] Ready
- [ ] Not Ready
- **Approver:** Edwin Carreño
- **Role:** Software developer
- **Approval date:** 2026-09-09
- **Blocking Issues:** None
