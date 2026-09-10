# Backlog Priority

## Source

- **Repository:** `ecarrenolozano/research-csv-cleaner`
- **Issue source:** GitHub open issue list and local approved SDLC artifacts
- **Inspection date:** 2026-09-10
- **Planning mode:** Manual implementation guidance only
- **Active increment:** CR-0001 / REQ-0002

No GitHub issues, Project items, labels, assignments, milestones, branches,
commits, or pull requests were changed by this planning document.

## Current Implementation Baseline

Historical issue #1 implemented REQ-0001 and is closed. That implementation is
useful as a baseline, but it is not active CR-0001 completion evidence because
REQ-0001 removed invalid rows and reported removed-row count.

Current local code already provides:

- CLI entry point and argument parsing.
- CSV reading and CSV writing for local file paths.
- selected-column presence validation.
- numeric invalid-value detection for missing, empty, unparseable, NaN, and
  infinite values.
- row preservation in the resulting CLI CSV for issue #8 / US-0008.
- detailed `validation_errors` explanations in the resulting CLI CSV for issue
  #9 / US-0009.
- a CLI count message based on the historical removed-row behavior.
- a Streamlit entry-point shell and runtime dependency.

Current local code does not yet provide CR-0001 behavior for reporting
validation-error row count with final CLI wording or operating the Streamlit
upload, selection, preview, count, and download workflow.

Existing validation feature files and BDD steps are historical REQ-0001
evidence. They still assert that invalid rows are removed, so they must not be
treated as CR-0001 validation evidence.

## Unresolved Issue Inventory

All listed issues are open and were observed in the GitHub Product Backlog on
2026-09-10.

### Coordination Issues

| Issue | Title | Role in planning |
|---|---|---|
| #3 | CR-0001 - Shared CSV validation behavior | Parent coordination track for shared validation and resulting CSV behavior. |
| #4 | CR-0001 - CLI continuity and validation reporting | Parent coordination track for CLI reporting and continuity. |
| #5 | CR-0001 - Streamlit validation interface | Parent coordination track for local Streamlit workflow. |

The parent issues organize implementation work. The child user-story issues
below are the preferred implementation slices unless a later approved proposal
explicitly combines or splits scope.

### User-Story Issues

| Issue | Title | Current implementation impact | Readiness |
|---|---|---|---|
| #6 | US-0006 - Read a CSV file | Existing CLI CSV read path is reusable; Streamlit upload read path still needs adaptation. | Ready as verification/adaptation work. |
| #7 | US-0007 - Validate one selected numeric column | Numeric classification and missing-column handling mostly exist in CLI code. | Ready as verification/adaptation work. |
| #8 | US-0008 - Preserve all input rows | Implemented locally; unit and CLI integration tests confirm invalid rows remain in the resulting CSV. | Ready for later validation. |
| #9 | US-0009 - Add validation-error explanations for invalid rows | Implemented locally; unit and CLI integration tests confirm specific `validation_errors` explanations for invalid rows and empty explanations for valid rows. | Ready for later validation. |
| #10 | US-0010 - Write the resulting CSV | CSV writing exists but writes historical cleaned output without invalid rows or `validation_errors`. | Ready for adaptation. |
| #11 | US-0011 - Download the resulting CSV | Streamlit download is not implemented. | Ready after Streamlit validation result exists. |
| #12 | US-0012 - Report validation-error row count | CLI count exists for removed rows, not validation-error rows. | Ready for adaptation. |
| #13 | US-0013 - Display validation-error row count | Streamlit count display is not implemented. | Ready after Streamlit validation result exists. |
| #14 | US-0014 - Upload a CSV file through Streamlit | Streamlit shell exists; upload is not implemented. | Ready after shared result behavior is stable. |
| #15 | US-0015 - Select the numeric column through Streamlit | Streamlit column selection is not implemented. | Ready after upload/read path exists. |
| #16 | US-0016 - Preview validated data through Streamlit | Streamlit preview is not implemented. | Ready after validation result exists. |
| #17 | US-0017 - Keep the existing CLI operational | CLI exists but must preserve the accepted command shape while changing output semantics. | Ready for regression-focused adaptation. |

## Suggested Implementation Order

1. **Issue #8 - US-0008 - Preserve all input rows** - locally implemented

   This is the core CR-0001 behavior change. The historical implementation
   removed invalid rows; this slice now preserves every input row before
   dependent output and reporting work builds on it.

2. **Issue #9 - US-0009 - Add validation-error explanations for invalid rows** - locally implemented

   Row preservation is now paired with annotations. This slice introduces
   detailed explanations for each invalid numeric problem: missing, empty,
   unparseable, NaN, and infinite values.

3. **Issue #7 - US-0007 - Validate one selected numeric column**

   Existing numeric classification should be verified and adapted to feed the
   new explanation-producing validation result. This is not a from-scratch
   implementation.

4. **Issue #10 - US-0010 - Write the resulting CSV**

   CSV writing already exists, but it must write the CR-0001 result: all input
   rows plus `validation_errors`.

5. **Issue #12 - US-0012 - Report validation-error row count**

   The CLI already reports a count, but the meaning changes from removed rows
   to rows containing validation errors.

6. **Issue #17 - US-0017 - Keep the existing CLI operational**

   After the shared transformation and count semantics are adapted, the CLI
   should be regression-checked against the existing command shape and CR-0001
   output behavior.

7. **Issue #6 - US-0006 - Read a CSV file**

   CSV reading exists for the CLI. Handle this as verification and reuse work,
   with any needed adapter for uploaded Streamlit files.

8. **Issue #14 - US-0014 - Upload a CSV file through Streamlit**

   The Streamlit shell and dependency exist. Upload can now attach to the shared
   CSV read/validation flow.

9. **Issue #15 - US-0015 - Select the numeric column through Streamlit**

   Column selection depends on uploaded CSV headers and should reuse the same
   selected-column validation semantics as the CLI.

10. **Issue #16 - US-0016 - Preview validated data through Streamlit**

    Preview depends on the CR-0001 validated result produced by the shared
    transformation.

11. **Issue #13 - US-0013 - Display validation-error row count**

    Count display should use the same row-count semantics introduced for the
    CLI: rows containing validation errors, not removed rows.

12. **Issue #11 - US-0011 - Download the resulting CSV**

    Download should come after the Streamlit interface can produce the validated
    result to preview and count.

## Dependency And Risk Notes

- The highest-risk behavior is the semantic change from filtering rows to
  annotating rows. Implementing #8 and #9 first reduces the chance of duplicating
  old behavior across CLI and Streamlit code.
- Shared validation semantics are required by ARCH-002 and ADR-001. Avoid
  duplicating numeric validation rules separately in the CLI and Streamlit
  entry points.
- Code-level architecture currently documents only historical issue #1 and the
  CLI container. CR-0001 implementation proposals should evaluate whether to
  update the central code-level index and add or update container maps,
  especially for the Streamlit Interface container.
- Exact CLI output text, exact Streamlit layout, CSV dialect, encoding,
  malformed-file handling, overwrite or same-path behavior, and large-file
  capacity remain unspecified beyond approved acceptance criteria.
- Any need for new product behavior, dependency changes, or material
  architecture decisions must route back to the owning SDLC stage before
  implementation continues.

## Next Action

Validate the locally implemented subset for US-0008 and US-0009, or select
exactly one remaining implementation issue for the next
`g-implement-repository-work` execution.
