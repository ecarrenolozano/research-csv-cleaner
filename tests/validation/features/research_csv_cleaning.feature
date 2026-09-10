Feature: Local research CSV cleaning

  # Historical REQ-0001 validation evidence, superseded by CR-0001:
  # - CSV input was read.
  # - Required numeric-column validation was applied.
  # - Missing required numeric column failed with a clear error and no output.
  # - Invalid rows were removed.
  # - Supported invalid numeric values were removed.
  # - A cleaned CSV was written.
  # - Removed-row count was reported.

  Scenario: US-0007 selected numeric column validation is applied
    Given a CSV file contains selected-column values that are missing, empty, unparseable as floating-point numbers, NaN, or infinite
    When the researcher validates the file
    Then the tool treats those selected-column values as invalid

  Scenario: US-0006 CSV input is read for validation
    Given a CSV file is available for validation
    When the researcher validates the file
    Then the tool reads the CSV file for validation

  Scenario: US-0007 selected numeric column is missing
    Given a CSV file does not contain the selected numeric column
    When the researcher validates the file
    Then the tool fails with a clear missing-column error
    And the tool does not create a resulting CSV

  Scenario: US-0008 invalid rows remain in the resulting CSV
    Given a CSV file contains rows with invalid values in the selected numeric column
    When the researcher validates the file
    Then the resulting CSV contains every input row

  Scenario: US-0009 invalid rows include validation errors
    Given a CSV file contains rows with invalid values in the selected numeric column
    When the researcher validates the file
    Then each invalid row contains an explanation in the validation_errors column

  Scenario: US-0009 validation errors explain the specific invalid numeric problem
    Given a CSV file contains selected-column values that are missing, empty, unparseable as floating-point numbers, NaN, or infinite
    When the researcher validates the file
    Then each invalid row's validation_errors value explains the specific invalid numeric problem detected for that row

  Scenario: US-0009 valid rows have no validation errors
    Given a CSV file contains rows with valid values in the selected numeric column
    When the researcher validates the file
    Then each valid row has no error explanation in the validation_errors column

  Scenario: US-0010 resulting CSV is written
    Given a CSV file is available for validation
    When the researcher validates the file
    Then the tool writes a resulting CSV file

  Scenario: US-0011 resulting CSV is downloaded
    Given validation has completed in the Streamlit interface
    When the researcher downloads the resulting CSV
    Then the interface provides the resulting CSV for download

  Scenario: US-0012 validation-error row count is reported
    Given the CLI has detected rows with validation errors
    When the validation run completes
    Then the CLI reports the number of rows containing validation errors

  Scenario: US-0013 validation-error row count is displayed
    Given validation has completed in the Streamlit interface
    When the validated data is available
    Then the interface displays the number of rows containing validation errors

  Scenario: US-0014 CSV file is uploaded
    Given the Streamlit interface is open
    When the researcher uploads a CSV file
    Then the interface accepts the CSV file for validation

  Scenario: US-0015 numeric column is selected
    Given a CSV file is uploaded in the Streamlit interface
    When the researcher selects a numeric column
    Then the interface uses that selected column for validation

  Scenario: US-0016 validated data is previewed
    Given validation has completed in the Streamlit interface
    When the validated data is available
    Then the interface previews the validated data

  Scenario: US-0017 existing CLI still runs
    Given a researcher provides the existing CLI inputs
    When the researcher runs the CLI
    Then the CLI validates the CSV and produces the resulting CSV
