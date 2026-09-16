# Research CSV Cleaner

A small local research data cleaning tool for validating numeric CSV columns from either a command-line interface or a Streamlit application.

The cleaner keeps every input row, checks one selected numeric column, and appends a `validation_errors` column that explains invalid values. It reports values that are missing, empty, non-numeric, `NaN`, or infinite.

## Features

- Validate a selected numeric column in a CSV file.
- Preserve all original rows and columns.
- Add a `validation_errors` column to the resulting CSV.
- Report the number of rows containing validation errors.
- Run as a CLI for repeatable local workflows.
- Run as a Streamlit app for upload, preview, and download workflows.

## Development approach

This repository follows an AI-assisted, documentation-driven software development lifecycle. AI may support analysis, planning, implementation, testing, and documentation, but designated artifacts require human approval before work proceeds to the next stage.

Start with:

1. `sdlc_docs/trace_workflow.md` to see workflow status and next action.
2. `sdlc_docs/00_inception/sources/` to store original project request evidence.
3. `sdlc_docs/00_inception/project_context.md` after request clarification and approval.

Consult `WORKFLOW.md` for the complete staged sequence and skill ownership.

The AI SDLC Agent Skills are installed under:

```text
.agents/skills/
```

They are maintained separately in:

```text
https://github.com/ecarrenolozano/ai-sdlc-skills
```

## Requirements

- Python 3.12 or newer
- `uv`
- Node.js/npm only when updating the installed Agent Skills

## Setup

```bash
uv sync --all-groups
uv run pre-commit install
```

## CLI Usage

Run the CLI from the repository checkout with an input CSV path, an output CSV path, and the required numeric column to validate:

```bash
uv run python -m research_csv_cleaner.cli_application INPUT.csv OUTPUT.csv REQUIRED_COLUMN
```

Example using the included sample data:

```bash
uv run python -m research_csv_cleaner.cli_application \
  data/in/sample_research_data.csv \
  data/out/sample_research_data_validated.csv \
  temperature
```

On success, the CLI writes the resulting CSV and prints the number of rows containing validation errors:

```text
Rows containing validation errors: 4
```

The output CSV contains the original data plus `validation_errors`. Valid rows have an empty validation value. Invalid rows contain a specific explanation such as `temperature is empty`, `temperature is not a number`, `temperature is NaN`, or `temperature is infinite`.

If the selected numeric column is missing, the CLI exits with a non-zero status, prints a clear error, and does not create the output file.

## Streamlit App

Start the local Streamlit application:

```bash
uv run streamlit run src/research_csv_cleaner/streamlit_interface.py
```

Then use the browser interface to:

1. Upload a `.csv` file.
2. Select the numeric column to validate.
3. Review the validated rows in the preview table.
4. Check the metric showing rows containing validation errors.
5. Download the resulting CSV as `validated.csv`.

The Streamlit app applies the same validation rules as the CLI and includes the same `validation_errors` output column.

## Updating Agent Skills

To update the AI SDLC workflow skills, run from the project root:

```bash
npx skills update
```

You do not need to regenerate this project when the central skills repository changes.

To inspect the installed skills:

```bash
ls .agents/skills
```

## Quality checks

```bash
uv run pytest
uv run ruff check .
uv run ruff format --check .
uv run mypy src
```

## Documentation

```bash
uv run mkdocs serve
```

## Project metadata

- **Type:** application
- **Python:** 3.12+
- **Agent skills:** `.agents/skills/`
- **Author:** Edwin Carreño <edwin1892@gmail.com>
- **License:** MIT
