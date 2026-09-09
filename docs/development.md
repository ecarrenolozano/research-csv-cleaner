# Development

This project uses `uv` for dependency management and local command execution.

## Setup

Install all dependency groups from the locked environment:

```bash
uv sync --locked --all-groups
```

Install the pre-commit hooks when working locally:

```bash
uv run pre-commit install
```

## Local Execution

Run the current CLI entry point from the repository checkout:

```bash
uv run python -m research_csv_cleaner.cli_application
```

The first release is a checkout-based local Python application. Packaging is
validated with a wheel build, but no standalone installer or deployed service is
part of the approved architecture.

## Tests

Run the full test suite:

```bash
uv run pytest
```

The test suite is organized by purpose:

- `tests/unit/`: isolated technical or product units.
- `tests/integration/`: collaboration among real components.
- `tests/regression/`: confirmed defects, intentionally empty until needed.
- `tests/validation/`: future pytest-bdd acceptance scenarios.

Collect tests without executing them:

```bash
uv run pytest --collect-only
```

## Quality Checks

Run the same checks used by CI:

```bash
uv run pytest
uv run ruff check .
uv run ruff format --check .
uv run mypy src
uv build
```

## Documentation

Serve the documentation locally:

```bash
uv run mkdocs serve
```
