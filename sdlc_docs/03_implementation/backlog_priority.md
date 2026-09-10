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
  infinite values for issue #7 / US-0007.
- row preservation in the resulting CLI CSV for issue #8 / US-0008.
- detailed `validation_errors` explanations in the resulting CLI CSV for issue
  #9 / US-0009.
- resulting CSV writing for issue #10 / US-0010.
- validation-error row count reporting for issue #12 / US-0012.
- CLI continuity for issue #17 / US-0017.
- Streamlit CSV upload and read behavior for issues #14 and #6.
- Streamlit numeric-column selection for issue #15.
- Streamlit validated-data preview for issue #16.
- Streamlit validation-error row count display for issue #13.
- Streamlit resulting CSV download for issue #11.

Current local code provides the planned CR-0001 child-story implementation
scope. Product-level BDD validation remains a separate downstream workflow gate.

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
| #6 | US-0006 - Read a CSV file | Implemented locally; CLI and Streamlit paths read CSV input for validation. | Ready for later validation. |
| #7 | US-0007 - Validate one selected numeric column | Implemented locally; unit and CLI integration tests confirm selected-column invalid-value classification and missing-column failure without output creation. | Ready for later validation. |
| #8 | US-0008 - Preserve all input rows | Implemented locally; unit and CLI integration tests confirm invalid rows remain in the resulting CSV. | Ready for later validation. |
| #9 | US-0009 - Add validation-error explanations for invalid rows | Implemented locally; unit and CLI integration tests confirm specific `validation_errors` explanations for invalid rows and empty explanations for valid rows. | Ready for later validation. |
| #10 | US-0010 - Write the resulting CSV | Implemented locally; CLI integration tests confirm the validation run writes a resulting CSV with preserved rows and `validation_errors`. | Ready for later validation. |
| #11 | US-0011 - Download the resulting CSV | Implemented locally; Streamlit provides a resulting CSV download after validation. | Ready for later validation. |
| #12 | US-0012 - Report validation-error row count | Implemented locally; CLI integration tests confirm the success message reports rows containing validation errors. | Ready for later validation. |
| #13 | US-0013 - Display validation-error row count | Implemented locally; Streamlit displays rows containing validation errors after validation. | Ready for later validation. |
| #14 | US-0014 - Upload a CSV file through Streamlit | Implemented locally; Streamlit accepts CSV uploads for validation. | Ready for later validation. |
| #15 | US-0015 - Select the numeric column through Streamlit | Implemented locally; Streamlit offers uploaded CSV headers for selected-column validation. | Ready for later validation. |
| #16 | US-0016 - Preview validated data through Streamlit | Implemented locally; Streamlit previews validated rows with `validation_errors`. | Ready for later validation. |
| #17 | US-0017 - Keep the existing CLI operational | Implemented locally; CLI integration tests confirm the existing command shape still validates and writes resulting CSV output. | Ready for later validation. |

## Suggested Implementation Order

1. **Issue #8 - US-0008 - Preserve all input rows** - locally implemented

   This is the core CR-0001 behavior change. The historical implementation
   removed invalid rows; this slice now preserves every input row before
   dependent output and reporting work builds on it.

2. **Issue #9 - US-0009 - Add validation-error explanations for invalid rows** - locally implemented

   Row preservation is now paired with annotations. This slice introduces
   detailed explanations for each invalid numeric problem: missing, empty,
   unparseable, NaN, and infinite values.

3. **Issue #7 - US-0007 - Validate one selected numeric column** - locally implemented

   Existing numeric classification and selected-column presence handling already
   cover this slice in the CLI path. Unit and CLI integration tests confirm the
   approved invalid numeric classes and missing-column failure behavior.

4. **Issue #10 - US-0010 - Write the resulting CSV** - locally implemented

   The CLI path writes the CR-0001 result with all input rows and
   `validation_errors`. CLI integration tests read the resulting CSV back from
   the output path and confirm its contents.

5. **Issue #12 - US-0012 - Report validation-error row count** - locally implemented

   The CLI now reports rows containing validation errors instead of using the
   historical removed-row wording.

6. **Issue #17 - US-0017 - Keep the existing CLI operational** - locally implemented

   The existing CLI command shape remains operational while producing CR-0001
   output behavior.

7. **Issue #6 - US-0006 - Read a CSV file** - locally implemented

   CSV input is read through the existing CLI path and the Streamlit uploaded
   file path.

8. **Issue #14 - US-0014 - Upload a CSV file through Streamlit** - locally implemented

   The Streamlit interface accepts CSV files through a file uploader.

9. **Issue #15 - US-0015 - Select the numeric column through Streamlit** - locally implemented

   The Streamlit interface lists uploaded CSV headers for numeric-column
   selection.

10. **Issue #16 - US-0016 - Preview validated data through Streamlit** - locally implemented

    The Streamlit interface previews validated rows after applying shared
    validation semantics.

11. **Issue #13 - US-0013 - Display validation-error row count** - locally implemented

    The Streamlit interface displays the number of rows containing validation
    errors.

12. **Issue #11 - US-0011 - Download the resulting CSV** - locally implemented

    The Streamlit interface provides the validated result as downloadable CSV.

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

Continue with CR-0001 user-story validation for US-0006 through US-0017.
