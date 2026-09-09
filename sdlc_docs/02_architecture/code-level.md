# Code-Level Architecture

This index records developer-owned code structure that implements approved
architecture elements. It does not replace the approved C4 architecture baseline.

## Issue Coverage

| Issue | Requirement and stories | Architecture element | Code map |
|---|---|---|---|
| #1 - Implement local research CSV cleaning | REQ-0001; US-0001 through US-0005 | AE-002 CLI Application | [CLI application code map](containers/cli-application/code-level.md) |

## Container Maps

- [CLI Application](containers/cli-application/code-level.md)

## Boundary Notes

- The implementation remains a single local Python CLI process.
- Python standard-library modules provide argument handling, CSV I/O, numeric
  validation, path handling, and process exit behavior.
- No database, web service, GUI, external API, or additional runtime dependency
  is introduced.
