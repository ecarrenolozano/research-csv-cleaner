Feature: Local research CSV cleaning

  Scenario: CSV input is read
    Given a local CSV file exists
    When the researcher runs the tool with that file as input
    Then the tool reads the CSV file for cleaning

  Scenario: Required numeric column validation is applied
    Given a local CSV file contains the configured required numeric column
    When the researcher runs the tool
    Then the tool treats missing values, empty values, values that cannot be parsed as floating-point numbers, NaN values, and infinite values as invalid

  Scenario: Required numeric column is missing
    Given a local CSV file does not contain the configured required numeric column
    When the researcher runs the tool
    Then the tool fails with a clear error message
    And the tool does not create an output file

  Scenario: Invalid rows are removed
    Given a local CSV file contains rows with invalid values in the required numeric column
    When the researcher runs the tool
    Then the cleaned output excludes the rows with invalid values

  Scenario: Supported invalid numeric values are removed
    Given a local CSV file contains rows where the required numeric column has missing values, empty values, values that cannot be parsed as floating-point numbers, NaN values, or infinite values
    When the researcher runs the tool
    Then the cleaned output excludes those rows

  Scenario: Cleaned CSV is written
    Given the tool has finished cleaning the input CSV
    When the cleaning run completes
    Then the tool writes a cleaned CSV file

  Scenario: Removed row count is reported
    Given the tool has removed rows during cleaning
    When the cleaning run completes
    Then the tool reports the number of rows removed
