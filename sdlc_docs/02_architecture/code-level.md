# Code-Level Architecture

This index records developer-owned code structure that implements approved
architecture elements. It does not replace the approved C4 architecture baseline.

## Issue Coverage

| Issue | Requirement and stories | Architecture element | Code map |
|---|---|---|---|
| #1 - Implement local research CSV cleaning | REQ-0001; US-0001 through US-0005 | AE-002 CLI Application | [CLI application code map](containers/cli-application/code-level.md) |
| #7 - Validate one selected numeric column | REQ-0002; US-0007 | AE-002 CLI Application; shared validation semantics for AE-003 later | [CLI application code map](containers/cli-application/code-level.md) |
| #8 - Preserve all input rows | REQ-0002; US-0008 | AE-002 CLI Application; shared validation semantics for AE-003 later | [CLI application code map](containers/cli-application/code-level.md) |
| #9 - Add validation-error explanations for invalid rows | REQ-0002; US-0009 | AE-002 CLI Application; shared validation semantics for AE-003 later | [CLI application code map](containers/cli-application/code-level.md) |

## Container Maps

- [CLI Application](containers/cli-application/code-level.md)

## Boundary Notes

- Current implemented behavior remains in the local Python CLI process.
- Python standard-library modules provide argument handling, CSV I/O, numeric
  validation, path handling, and process exit behavior.
- No database, web service, GUI, external API, or additional runtime dependency
  is introduced.
