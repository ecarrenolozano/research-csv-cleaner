# Code-Level Architecture

This index records developer-owned code structure that implements approved
architecture elements. It does not replace the approved C4 architecture baseline.

## Issue Coverage

| Issue | Requirement and stories | Architecture element | Code map |
|---|---|---|---|
| #1 - Implement local research CSV cleaning | REQ-0001; US-0001 through US-0005 | AE-002 CLI Application | [CLI application code map](containers/cli-application/code-level.md) |
| #6 - Read a CSV file | REQ-0002; US-0006 | AE-002 CLI Application; AE-003 Streamlit Interface | [CLI application code map](containers/cli-application/code-level.md); [Streamlit interface code map](containers/streamlit-interface/code-level.md) |
| #7 - Validate one selected numeric column | REQ-0002; US-0007 | AE-002 CLI Application; shared validation semantics for AE-003 later | [CLI application code map](containers/cli-application/code-level.md) |
| #8 - Preserve all input rows | REQ-0002; US-0008 | AE-002 CLI Application; shared validation semantics for AE-003 later | [CLI application code map](containers/cli-application/code-level.md) |
| #9 - Add validation-error explanations for invalid rows | REQ-0002; US-0009 | AE-002 CLI Application; shared validation semantics for AE-003 later | [CLI application code map](containers/cli-application/code-level.md) |
| #10 - Write the resulting CSV | REQ-0002; US-0010 | AE-002 CLI Application | [CLI application code map](containers/cli-application/code-level.md) |
| #11 - Download the resulting CSV | REQ-0002; US-0011 | AE-003 Streamlit Interface | [Streamlit interface code map](containers/streamlit-interface/code-level.md) |
| #12 - Report validation-error row count | REQ-0002; US-0012 | AE-002 CLI Application | [CLI application code map](containers/cli-application/code-level.md) |
| #13 - Display validation-error row count | REQ-0002; US-0013 | AE-003 Streamlit Interface | [Streamlit interface code map](containers/streamlit-interface/code-level.md) |
| #14 - Upload a CSV file through Streamlit | REQ-0002; US-0014 | AE-003 Streamlit Interface | [Streamlit interface code map](containers/streamlit-interface/code-level.md) |
| #15 - Select the numeric column through Streamlit | REQ-0002; US-0015 | AE-003 Streamlit Interface | [Streamlit interface code map](containers/streamlit-interface/code-level.md) |
| #16 - Preview validated data through Streamlit | REQ-0002; US-0016 | AE-003 Streamlit Interface | [Streamlit interface code map](containers/streamlit-interface/code-level.md) |
| #17 - Keep the existing CLI operational | REQ-0002; US-0017 | AE-002 CLI Application | [CLI application code map](containers/cli-application/code-level.md) |

## Container Maps

- [CLI Application](containers/cli-application/code-level.md)
- [Streamlit Interface](containers/streamlit-interface/code-level.md)

## Boundary Notes

- Current implemented behavior remains in the local Python CLI process and the
  local Streamlit interface.
- Python standard-library modules provide argument handling, CSV I/O, numeric
  validation, path handling, and process exit behavior.
- Streamlit provides the local browser interface. No database, web service,
  external API, or additional runtime dependency is introduced.
