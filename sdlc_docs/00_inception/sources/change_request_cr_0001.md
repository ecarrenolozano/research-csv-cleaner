# Change Request CR-0001

## Source Metadata

- **Date received:** 2026-09-09
- **Provided by:** Requester in chat
- **Scope:** Change to the existing Research CSV Cleaner project after initial CLI implementation was merged.

## Request

Invalid rows must no longer be removed. All rows must remain in the output CSV, and invalid rows must contain a validation_errors column explaining the detected problems.

Researchers also want a small Streamlit interface that allows them to upload a CSV file, select the numeric column to validate, preview the validated data, see how many rows contain validation errors, and download the resulting CSV. The existing CLI must continue to work.

Continue using the installed SDLC workflow. Inspect the current repository state and all previously approved artifacts before making changes. Identify conflicts or impacts on requirements, architecture, acceptance criteria, tests, and implementation assumptions. Do not implement anything yet. Guide me through the required change process and stop at the next human approval gate.

## Change Intake Approval

Approved to reopen SDLC requirements for CR-0001: preserve all rows, add validation_errors output, report validation-error row count, add Streamlit upload/preview/download interface, and keep the existing CLI operational.
