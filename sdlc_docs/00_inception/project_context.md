# Project Context

## How to Use This Document

This document turns an approved Clarified Project Request into an evidence-grounded, high-level definition of the software project.

Rules:

1. Verify that the source request is closed, ready, fully approved, and has no blocking issues.
2. Use only approved evidence and recorded stakeholder answers as confirmed facts.
3. Classify substantive information as `Confirmed fact`, `Derived interpretation`, `Assumption`, `Open question`, or `Approved decision`.
4. Record evidence for confirmed facts, derived interpretations, and approved decisions.
5. Never silently fill a gap. Use `Not identified in the approved source` for non-blocking gaps.
6. Ask no more than 20 distinct Working Questions across the document lifecycle.
7. Ask questions in small rounds, normally one to four, and stop until answers are available.
8. Remove Working Questions before approval.
9. Do not include detailed requirements, user stories, acceptance criteria, architecture, implementation plans, repository issues, or test plans.
10. Close the document only after valid human approval as `Ready for Product Requirements`.

---

## 1. Document Control

- **Project name:** Research CSV Cleaner
- **Source request:** `clarified_project_request.md`
- **Prepared by:** Codex
- **Version:** 2.0
- **Last updated:** 2026-09-09
- **Document state:** Closed
- **Active change:** CR-0001

## 2. Project Summary

Researchers need the existing local Research CSV Cleaner to keep all rows from an uploaded or local experiment CSV and annotate invalid numeric values instead of removing rows. The updated useful version should read a CSV file, validate one selected numeric column, write a resulting CSV containing every input row, add a `validation_errors` column for rows with detected problems, report how many rows contain validation errors, provide a small Streamlit interface for upload, selection, preview, and download, and keep the existing CLI operational.

`Derived interpretation`: Keeping all rows while marking invalid values helps researchers inspect and decide how to handle problematic experiment rows without losing source rows. This is based on CR-0001's approved instruction that invalid rows must no longer be removed.

## 3. Evidence and Classification Register

Record substantive statements that materially shape the Project Context.

| Statement | Classification | Evidence or basis | Confirmation path if unconfirmed |
|---|---|---|---|
| The project is a Python tool for cleaning research CSV files. | Confirmed fact | `clarified_project_request.md`, Initial Understanding; original informal request | - |
| Researchers receive experiment CSV files and currently clean them manually. | Confirmed fact | `clarified_project_request.md`, Critical Question 1 answer | - |
| Invalid values can be missed or handled inconsistently during manual cleaning. | Confirmed fact | `clarified_project_request.md`, Critical Question 1 answer | - |
| The project should reduce missed or inconsistent handling of invalid values. | Derived interpretation | Based on the confirmed current problem that invalid values can be missed or handled inconsistently | - |
| The initial release ran locally on individual CSV files and removed invalid rows. | Approved decision | `clarified_project_request.md`, Initial Release Readiness Approval; prior approved Project Context version 1.0 | - |
| CR-0001 changes the active behavior so invalid rows must no longer be removed. | Approved decision | `clarified_project_request.md`, Change Request CR-0001 and CR-0001 Readiness Approval | - |
| CR-0001 requires all rows to remain in the output CSV. | Approved decision | `clarified_project_request.md`, Change Request CR-0001 and CR-0001 Readiness Approval | - |
| CR-0001 requires invalid rows to contain a `validation_errors` column explaining detected problems. | Approved decision | `clarified_project_request.md`, Change Request CR-0001 and CR-0001 Readiness Approval | - |
| CR-0001 requires reporting how many rows contain validation errors. | Approved decision | `clarified_project_request.md`, Change Request CR-0001 and CR-0001 Readiness Approval | - |
| CR-0001 requires a small Streamlit interface for CSV upload, numeric-column selection, validated-data preview, validation-error count, and CSV download. | Approved decision | `clarified_project_request.md`, Change Request CR-0001 and CR-0001 Readiness Approval | - |
| CR-0001 requires the existing CLI to continue working. | Approved decision | `clarified_project_request.md`, Change Request CR-0001 and CR-0001 Readiness Approval | - |
| The implementation should be small, testable, and easy to understand. | Approved decision | `clarified_project_request.md`, Critical Question 3 answer and Initial Release Readiness Approval; no CR-0001 evidence removes this constraint | - |
| There is no special deadline beyond the workshop exercise. | Confirmed fact | `clarified_project_request.md`, Critical Question 3 answer; no CR-0001 evidence changes this | - |
| Additional shared infrastructure is not required. | Confirmed fact | `clarified_project_request.md`, Critical Question 3 answer; CR-0001 requests a local Streamlit interface, not shared infrastructure | - |
| Detailed definitions of invalid numeric values are deferred to requirements clarification. | Approved decision | `clarified_project_request.md`, Initial Understanding and Critical Question 3 impact | - |
| Edwin Carreño approved CR-0001 as ready for Project Context update. | Approved decision | `clarified_project_request.md`, CR-0001 Readiness Approval | - |

## 4. Background

Researchers receive CSV files from experiments and currently clean those files manually. The approved request identifies a risk in that current process: invalid values can be missed or handled inconsistently.

The initial implemented release removed rows with invalid values. CR-0001 changes the desired active behavior: invalid rows must remain available in the resulting CSV and must be annotated with validation errors.

## 5. Problem Statement

Manual cleaning of research CSV files can miss invalid values or handle them inconsistently. Removing invalid rows also prevents researchers from inspecting those rows in the resulting CSV after validation.

`Derived interpretation`: Preserving invalid rows with explicit validation errors better supports research review because the output keeps the original row set visible. This is based on CR-0001's approved instruction that all rows must remain in the output CSV.

## 6. Why the Project Is Needed

The project is needed so researchers have a small local tool that supports consistent identification of invalid numeric values while preserving the full experiment row set for review.

## 7. Desired Future Situation

Researchers can use either the existing CLI or a small Streamlit interface to validate an individual experiment CSV file. The resulting CSV keeps every input row, marks detected numeric validation problems in a `validation_errors` column, and shows how many rows contain validation errors.

## 8. Project Goal

Update the existing local Research CSV Cleaner so researchers can validate one numeric column, preserve every row, annotate invalid rows with validation errors, see how many rows contain validation errors, and use either the CLI or a small Streamlit interface.

## 9. Expected Outcomes

- A CSV file can be read as input.
- One selected numeric column can be validated.
- Every input row remains in the resulting CSV.
- Rows with invalid values include an explanation in a `validation_errors` column.
- A resulting CSV file can be written or downloaded.
- The tool reports or displays how many rows contain validation errors.
- Researchers can use a small Streamlit interface to upload a CSV file.
- Researchers can select the numeric column to validate in the Streamlit interface.
- Researchers can preview the validated data in the Streamlit interface.
- Researchers can download the resulting CSV from the Streamlit interface.
- The existing CLI remains operational.
- The implementation remains small, testable, and easy to understand.

## 10. People Involved

### Intended Users

- Researchers who receive experiment CSV files.

### Other People Affected

- Not identified in the approved source.

### Confirmed Responsibilities

- **Edwin Carreño:** Approved the initial clarified project request as ready on 2026-09-09.
- **Edwin Carreño:** Approved CR-0001 as ready for Project Context update on 2026-09-09.

## 11. High-Level Scope

### Included

- Local processing of individual research CSV files.
- Validation of one selected numeric column.
- Preservation of all input rows in the resulting CSV.
- A `validation_errors` column explaining detected problems on invalid rows.
- Reporting or displaying the number of rows containing validation errors.
- Writing or downloading the resulting CSV.
- Continuing support for the existing CLI.
- A small Streamlit interface for CSV upload, numeric-column selection, validated-data preview, validation-error count, and CSV download.

### Excluded

- Shared workflow integration.
- Database integration.
- Web service.
- Shared deployment infrastructure.

### Future Design Considerations

- Not identified in the approved source.

## 12. MVP Boundary

The MVP boundary is the smallest useful software scope approved for CR-0001. It does not include hypotheses, experiments, or business validation.

### Intended User

Researchers who receive experiment CSV files.

### Minimum Useful Outcome

A researcher can validate one numeric column in an individual CSV file, keep every row in the resulting CSV, and see which rows contain validation errors.

### Included High-Level Capabilities

- Read a CSV file.
- Validate one selected numeric column.
- Preserve all input rows in the resulting CSV.
- Add validation-error explanations for invalid rows.
- Write or download the resulting CSV.
- Report or display how many rows contain validation errors.
- Provide a small Streamlit interface for upload, numeric-column selection, preview, and download.
- Keep the existing CLI operational.

### Explicitly Excluded

- Shared workflow integration.
- Database.
- Web service.
- Shared deployment infrastructure.

### Confirmed Delivery Limits

- No special deadline beyond the workshop exercise.
- The implementation should remain small, testable, and easy to understand.
- No additional shared infrastructure is required.

### Completion Condition

CR-0001 is delivered when the tool can read a CSV file through the existing CLI and the Streamlit interface, validate one selected numeric column, preserve all rows, annotate invalid rows in `validation_errors`, provide a validation-error row count, and produce a resulting CSV for researcher use.

## 13. Constraints

- The tool must run locally on individual CSV files.
- The existing CLI must remain operational.
- The Streamlit interface must support local upload, numeric-column selection, preview, validation-error count, and resulting CSV download.
- The implementation should remain small, testable, and easy to understand.
- No shared workflow integration, database, web service, or shared deployment infrastructure is required.
- No special deadline exists beyond the workshop exercise.

## 14. Assumptions

No assumptions recorded.

## 15. Dependencies

- A local Streamlit interface is now part of the approved scope.

## 16. Risks and Uncertainties

- **Detailed invalid-value rules are not yet defined for CR-0001 wording:** Product requirements will need to define what makes a numeric value invalid and what explanation appears in `validation_errors`.
  - **Classification:** Approved decision
  - **Evidence or basis:** `clarified_project_request.md`, Initial Understanding and Critical Question 3 impact state that detailed invalid-value definitions are deferred to requirements clarification; CR-0001 requests validation-error explanations.
  - **Affected project area:** Product requirements
- **Existing row-removal expectations are superseded by CR-0001:** Product requirements, architecture, tests, and implementation assumptions must distinguish approved historical behavior from active CR-0001 behavior.
  - **Classification:** Approved decision
  - **Evidence or basis:** `clarified_project_request.md`, CR-0001 contradictions and CR-0001 Readiness Approval.
  - **Affected project area:** Product requirements, architecture, validation, implementation.
- **Streamlit changes the previous interface boundary:** Architecture will need to revisit the prior CLI-only decision and dependency assumptions.
  - **Classification:** Approved decision
  - **Evidence or basis:** `clarified_project_request.md`, CR-0001 impact and CR-0001 Readiness Approval.
  - **Affected project area:** Architecture.

## 17. Success Criteria

- The tool can read a CSV file.
- The tool can validate one selected numeric column.
- The tool preserves all input rows in the resulting CSV.
- Invalid rows contain validation-error explanations.
- The tool writes or downloads a resulting CSV file.
- The tool reports or displays how many rows contain validation errors.
- Researchers can upload, configure, preview, and download through a small Streamlit interface.
- The existing CLI remains operational.
- The implementation is small, testable, and easy to understand.

## 18. Confirmed Decisions and Responsibilities

- **Person who requested the project:** Not identified.
- **Person who makes project-level decisions:** Not assigned in the approved source.
- **Person who confirms the software meets the agreed scope:** Not assigned in the approved source.
- **Person responsible for building the software:** Not assigned in the approved source.
- **Person who approved the initial clarified project request:** Edwin Carreño, Software developer.
- **Person who approved CR-0001 readiness:** Edwin Carreño, Software developer.

## 19. Validation Report

- **Approved source modified:** No
- **Unsupported confirmed claims:** 0
- **Derived interpretations without basis:** 0
- **Classification conflicts across sections:** 0
- **Mixed confirmed-and-derived statements:** 0
- **Stakeholder-confirmed interpretations not promoted:** 0
- **Assumptions without confirmation path:** 0
- **Open questions presented as resolved:** 0
- **Scope contradictions:** 0
- **Premature downstream detail:** 0
- **Authorized traceability fields changed:** None retained; attempted Project context row activation was reverted because the canonical workflow trace does not support reopening a completed foundation row while downstream initial-release rows remain complete.
- **Unauthorized traceability changes detected:** 0
- **Traceability Mutation Guard:** Passed

## 20. Human Review

- [x] Ready for Product Requirements
- [ ] Not Ready
- **Reviewer:** Edwin Carreño
- **Role or responsibility:** Software developer
- **Approval date:** 2026-09-09
- **Blocking Issues or Feedback:** None
