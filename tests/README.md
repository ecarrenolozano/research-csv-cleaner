# Tests

The test suite is organized by purpose:

- `unit/`: isolated technical or product units.
- `integration/`: collaboration among real components.
- `regression/`: confirmed defects, intentionally empty until needed.
- `validation/features/`: future Gherkin scenarios for approved behavior.
- `validation/steps/`: future pytest-bdd step definitions.

Foundation smoke tests must stay technical. Product behavior scenarios belong in
the implementation and validation workflows after the relevant story is selected.
