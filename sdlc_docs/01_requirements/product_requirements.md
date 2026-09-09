# Product Requirements

## 1. Document Control

- **Project:** Research CSV Cleaner
- **Mode:** Initial release update for CR-0001
- **Source project context or increment issue:** `sdlc_docs/00_inception/project_context.md`
- **Last updated:** 2026-09-09
- **Active scope state:** Approved

## 2. Requirements Overview

| Requirement | Requirement status | Stories | Story status | Source | Repository issues |
|---|---|---|---|---|---|
| REQ-0001 - Local research CSV cleaning | Superseded by CR-0001 | US-0001, US-0002, US-0003, US-0004, US-0005 | Superseded by CR-0001 | Prior approved Project Context v1.0 | Closed |
| REQ-0002 - Local CSV validation with row preservation and Streamlit interface | Approved | US-0006, US-0007, US-0008, US-0009, US-0010, US-0011, US-0012, US-0013, US-0014, US-0015, US-0016, US-0017 | Approved | `sdlc_docs/00_inception/project_context.md` CR-0001; stakeholder clarification in chat on 2026-09-09 | Created |

### Source Statement Coverage Register

Record every controlling source statement exactly once. Classify broad category statements such as "manage", "handle", or "support" as `Umbrella`; do not create an umbrella capability or story from them.

| Source ID | Source scope statement | Source location | Statement role | Decomposed into CAP IDs | Rationale |
|---|---|---|---|---|---|
| SRC-006 | Read a CSV file. | `project_context.md` section 12, Included High-Level Capabilities | Atomic | CAP-006 | Single observable capability from the approved CR-0001 MVP boundary. |
| SRC-007 | Validate one selected numeric column. | `project_context.md` section 12, Included High-Level Capabilities | Atomic | CAP-007 | Single observable capability from the approved CR-0001 MVP boundary. |
| SRC-008 | Preserve all input rows in the resulting CSV. | `project_context.md` section 12, Included High-Level Capabilities | Atomic | CAP-008 | Single observable capability from the approved CR-0001 MVP boundary. |
| SRC-009 | Add validation-error explanations for invalid rows. | `project_context.md` section 12, Included High-Level Capabilities | Atomic | CAP-009 | Single observable capability from the approved CR-0001 MVP boundary. |
| SRC-010 | Write or download the resulting CSV. | `project_context.md` section 12, Included High-Level Capabilities | Compound | CAP-010, CAP-011 | The source statement combines writing a resulting CSV and downloading a resulting CSV. |
| SRC-011 | Report or display how many rows contain validation errors. | `project_context.md` section 12, Included High-Level Capabilities | Compound | CAP-012, CAP-013 | The source statement combines CLI reporting and interface display. |
| SRC-012 | Provide a small Streamlit interface for upload, numeric-column selection, preview, and download. | `project_context.md` section 12, Included High-Level Capabilities | Compound | CAP-014, CAP-015, CAP-016, CAP-011 | The source statement combines Streamlit upload, selection, preview, and download outcomes. |
| SRC-013 | Keep the existing CLI operational. | `project_context.md` section 12, Included High-Level Capabilities | Atomic | CAP-017 | Single observable capability from the approved CR-0001 MVP boundary. |

### Source Scope Coverage Matrix

Record only atomic capabilities. Every row must reference one or more Source IDs from the register. Never use an umbrella verb as the atomic capability.

| Scope ID | Atomic capability | Source IDs | Source scope statement | Source location | Disposition | Requirement / Stories | Rationale or approval evidence |
|---|---|---|---|---|---|---|---|
| CAP-006 | Read a CSV file | SRC-006 | Read a CSV file. | `project_context.md` section 12, Included High-Level Capabilities | Covered | REQ-0002 / US-0006 | Single independently observable outcome. |
| CAP-007 | Validate one selected numeric column | SRC-007 | Validate one selected numeric column. | `project_context.md` section 12, Included High-Level Capabilities | Covered | REQ-0002 / US-0007 | Single independently observable outcome. |
| CAP-008 | Preserve all input rows in the resulting CSV | SRC-008 | Preserve all input rows in the resulting CSV. | `project_context.md` section 12, Included High-Level Capabilities | Covered | REQ-0002 / US-0008 | Single independently observable outcome. |
| CAP-009 | Add validation-error explanations for invalid rows | SRC-009 | Add validation-error explanations for invalid rows. | `project_context.md` section 12, Included High-Level Capabilities | Covered | REQ-0002 / US-0009 | Single independently observable outcome. |
| CAP-010 | Write the resulting CSV | SRC-010 | Write or download the resulting CSV. | `project_context.md` section 12, Included High-Level Capabilities | Covered | REQ-0002 / US-0010 | Single independently observable outcome decomposed from compound source statement. |
| CAP-011 | Download the resulting CSV | SRC-010, SRC-012 | Write or download the resulting CSV.; Provide a small Streamlit interface for upload, numeric-column selection, preview, and download. | `project_context.md` section 12, Included High-Level Capabilities | Covered | REQ-0002 / US-0011 | Single independently observable outcome shared by two source statements. |
| CAP-012 | Report how many rows contain validation errors | SRC-011 | Report or display how many rows contain validation errors. | `project_context.md` section 12, Included High-Level Capabilities | Covered | REQ-0002 / US-0012 | Single independently observable outcome decomposed from compound source statement. |
| CAP-013 | Display how many rows contain validation errors | SRC-011 | Report or display how many rows contain validation errors. | `project_context.md` section 12, Included High-Level Capabilities | Covered | REQ-0002 / US-0013 | Single independently observable outcome decomposed from compound source statement. |
| CAP-014 | Upload a CSV file through Streamlit | SRC-012 | Provide a small Streamlit interface for upload, numeric-column selection, preview, and download. | `project_context.md` section 12, Included High-Level Capabilities | Covered | REQ-0002 / US-0014 | Single independently observable outcome decomposed from compound source statement. |
| CAP-015 | Select the numeric column through Streamlit | SRC-012 | Provide a small Streamlit interface for upload, numeric-column selection, preview, and download. | `project_context.md` section 12, Included High-Level Capabilities | Covered | REQ-0002 / US-0015 | Single independently observable outcome decomposed from compound source statement. |
| CAP-016 | Preview validated data through Streamlit | SRC-012 | Provide a small Streamlit interface for upload, numeric-column selection, preview, and download. | `project_context.md` section 12, Included High-Level Capabilities | Covered | REQ-0002 / US-0016 | Single independently observable outcome decomposed from compound source statement. |
| CAP-017 | Keep the existing CLI operational | SRC-013 | Keep the existing CLI operational. | `project_context.md` section 12, Included High-Level Capabilities | Covered | REQ-0002 / US-0017 | Single independently observable outcome. |

## 3. Requirements

## REQ-0001 - Local research CSV cleaning

- **Status:** Superseded by CR-0001
- **Source:** Prior approved `sdlc_docs/00_inception/project_context.md` version 1.0
- **Evidence or basis:** Approved initial-release Product Requirements dated 2026-09-09; issue #1 completed; PR #2 merged.
- **Imported classification:** Not applicable
- **Repository representation:** Closed
- **Repository issue:** #1
- **Description:** The initial release allowed a researcher to clean one local research CSV file by validating one required numeric column, removing rows with invalid values, writing a cleaned CSV file, and reporting how many rows were removed.
- **Approved by:** Edwin Carreño
- **Reviewer role or responsibility:** Software Engineer
- **Approval date:** 2026-09-09
- **Blocking Issues or Feedback:** None

Historical US-0001 through US-0005 were approved for the initial release and are superseded for active CR-0001 behavior. The full prior approved text and mappings remain self-contained below.

### Historical Source Statement Coverage Register

| Source ID | Source scope statement | Source location | Statement role | Decomposed into CAP IDs | Rationale |
|---|---|---|---|---|---|
| SRC-001 | Read a CSV file. | `project_context.md` section 12, Included High-Level Capabilities | Atomic | CAP-001 | Single observable capability from the approved MVP boundary. |
| SRC-002 | Validate one required numeric column. | `project_context.md` section 12, Included High-Level Capabilities | Atomic | CAP-002 | Single observable capability from the approved MVP boundary. |
| SRC-003 | Remove rows with invalid values in that column. | `project_context.md` section 12, Included High-Level Capabilities | Atomic | CAP-003 | Single observable capability from the approved MVP boundary. |
| SRC-004 | Write a cleaned CSV file. | `project_context.md` section 12, Included High-Level Capabilities | Atomic | CAP-004 | Single observable capability from the approved MVP boundary. |
| SRC-005 | Report how many rows were removed. | `project_context.md` section 12, Included High-Level Capabilities | Atomic | CAP-005 | Single observable capability from the approved MVP boundary. |

### Historical Source Scope Coverage Matrix

| Scope ID | Atomic capability | Source IDs | Source scope statement | Source location | Disposition | Requirement / Stories | Rationale or approval evidence |
|---|---|---|---|---|---|---|---|
| CAP-001 | Read a CSV file | SRC-001 | Read a CSV file. | `project_context.md` section 12, Included High-Level Capabilities | Covered | REQ-0001 / US-0001 | Single independently observable outcome |
| CAP-002 | Validate one required numeric column | SRC-002 | Validate one required numeric column. | `project_context.md` section 12, Included High-Level Capabilities | Covered | REQ-0001 / US-0002 | Stakeholder clarified invalid numeric values and missing-column behavior in chat on 2026-09-09. |
| CAP-003 | Remove rows with invalid values in the required numeric column | SRC-003 | Remove rows with invalid values in that column. | `project_context.md` section 12, Included High-Level Capabilities | Covered | REQ-0001 / US-0003 | Stakeholder clarified that rows with missing, empty, non-floating-point, NaN, or infinite values in the required numeric column should be removed. |
| CAP-004 | Write a cleaned CSV file | SRC-004 | Write a cleaned CSV file. | `project_context.md` section 12, Included High-Level Capabilities | Covered | REQ-0001 / US-0004 | Single independently observable outcome |
| CAP-005 | Report the number of removed rows | SRC-005 | Report how many rows were removed. | `project_context.md` section 12, Included High-Level Capabilities | Covered | REQ-0001 / US-0005 | Single independently observable outcome |

#### Historical US-0001 - Read a CSV file

- **Status:** Superseded by CR-0001
- **Source or evidence basis:** CAP-001; approved Project Context section 12.
- **Covered scope IDs:** CAP-001
- **Atomicity:** Single observable outcome
- **Repository issue:** #1

As a researcher
I want the tool to read a local CSV file
so that I can start cleaning experiment data from a file I received.

#### Acceptance Criteria

**Scenario: CSV input is read**

Given a local CSV file exists
When the researcher runs the tool with that file as input
Then the tool reads the CSV file for cleaning.

#### Historical US-0002 - Validate one required numeric column

- **Status:** Superseded by CR-0001
- **Source or evidence basis:** CAP-002; approved Project Context section 12; stakeholder clarification in chat on 2026-09-09.
- **Covered scope IDs:** CAP-002
- **Atomicity:** Single observable outcome
- **Repository issue:** #1

As a researcher
I want the tool to validate one required numeric column
so that invalid numeric values can be identified consistently.

#### Acceptance Criteria

**Scenario: Required numeric column validation is applied**

Given a local CSV file contains the configured required numeric column
When the researcher runs the tool
Then the tool treats missing values, empty values, values that cannot be parsed as floating-point numbers, NaN values, and infinite values as invalid.

**Scenario: Required numeric column is missing**

Given a local CSV file does not contain the configured required numeric column
When the researcher runs the tool
Then the tool fails with a clear error message
And the tool does not create an output file.

#### Historical US-0003 - Remove rows with invalid values

- **Status:** Superseded by CR-0001
- **Source or evidence basis:** CAP-003; approved Project Context section 12; stakeholder clarification in chat on 2026-09-09.
- **Covered scope IDs:** CAP-003
- **Atomicity:** Single observable outcome
- **Repository issue:** #1

As a researcher
I want the tool to remove rows with invalid values in the required numeric column
so that the cleaned CSV excludes those invalid experiment rows.

#### Acceptance Criteria

**Scenario: Invalid rows are removed**

Given a local CSV file contains rows with invalid values in the required numeric column
When the researcher runs the tool
Then the cleaned output excludes the rows with invalid values.

**Scenario: Supported invalid numeric values are removed**

Given a local CSV file contains rows where the required numeric column has missing values, empty values, values that cannot be parsed as floating-point numbers, NaN values, or infinite values
When the researcher runs the tool
Then the cleaned output excludes those rows.

#### Historical US-0004 - Write a cleaned CSV file

- **Status:** Superseded by CR-0001
- **Source or evidence basis:** CAP-004; approved Project Context section 12.
- **Covered scope IDs:** CAP-004
- **Atomicity:** Single observable outcome
- **Repository issue:** #1

As a researcher
I want the tool to write a cleaned CSV file
so that I have a cleaned copy of the experiment data.

#### Acceptance Criteria

**Scenario: Cleaned CSV is written**

Given the tool has finished cleaning the input CSV
When the cleaning run completes
Then the tool writes a cleaned CSV file.

#### Historical US-0005 - Report removed row count

- **Status:** Superseded by CR-0001
- **Source or evidence basis:** CAP-005; approved Project Context section 12.
- **Covered scope IDs:** CAP-005
- **Atomicity:** Single observable outcome
- **Repository issue:** #1

As a researcher
I want the tool to report how many rows were removed
so that I can see the effect of the cleaning run.

#### Acceptance Criteria

**Scenario: Removed row count is reported**

Given the tool has removed rows during cleaning
When the cleaning run completes
Then the tool reports the number of rows removed.

### Historical Requirement Validation

- **Source evidence recorded:** Yes
- **Approved content changed:** Only status and CR-0001 supersession metadata were added.
- **Source scope statements omitted:** 0
- **Atomic capabilities without disposition:** 0
- **Compound stories without approved grouping:** 0
- **Coverage matrix/story mapping conflicts:** 0
- **Unsupported product behavior:** 0
- **Unresolved blocking questions:** 0
- **Duplicate repository story references:** 0
- **Overview/detail inconsistencies:** 0
- **Scope coverage validator:** Preflight passed
- **Scope validator command:** `python3 .agents/skills/c-manage-product-requirements/scripts/validate_scope_coverage.py sdlc_docs/00_inception/project_context.md sdlc_docs/01_requirements/product_requirements.md --mode initial-release`
- **Scope validator report synchronized:** Yes
- **Validation result:** Passed

## REQ-0002 - Local CSV validation with row preservation and Streamlit interface

- **Status:** Approved
- **Source:** `sdlc_docs/00_inception/project_context.md`
- **Evidence or basis:** Approved CR-0001 Project Context sections 8, 11, 12, and 17; stakeholder clarification in chat on 2026-09-09 that `validation_errors` should include a detailed explanation about each invalid numeric value.
- **Imported classification:** Not applicable
- **Repository representation:** Created
- **Repository issue:** Created
- **Description:** The CR-0001 update must let a researcher validate one selected numeric column in an individual CSV file, preserve every input row in the resulting CSV, annotate invalid rows with validation-error explanations, report or display how many rows contain validation errors, provide a small Streamlit interface for upload, selection, preview, and download, and keep the existing CLI operational.
- **Approved by:** Edwin Carreño
- **Reviewer role or responsibility:** Software developer
- **Approval date:** 2026-09-09
- **Blocking Issues or Feedback:** None

### US-0006 - Read a CSV file

- **Status:** Approved
- **Source or evidence basis:** CAP-006; approved CR-0001 Project Context section 12.
- **Covered scope IDs:** CAP-006
- **Atomicity:** Single observable outcome
- **Repository issue:** Created

As a researcher
I want the tool to read a CSV file
so that I can validate experiment data from a file I received.

#### Acceptance Criteria

**Scenario: CSV input is read for validation**

Given a CSV file is available
When the researcher validates that file
Then the tool reads the CSV file for validation.

### US-0007 - Validate one selected numeric column

- **Status:** Approved
- **Source or evidence basis:** CAP-007; approved CR-0001 Project Context section 12; prior approved invalid numeric value clarification.
- **Covered scope IDs:** CAP-007
- **Atomicity:** Single observable outcome
- **Repository issue:** Created

As a researcher
I want the tool to validate one selected numeric column
so that invalid numeric values can be identified consistently.

#### Acceptance Criteria

**Scenario: Selected numeric column validation is applied**

Given a CSV file contains the selected numeric column
When the researcher validates the file
Then the tool treats missing values, empty values, values that cannot be parsed as floating-point numbers, NaN values, and infinite values as invalid.

**Scenario: Selected numeric column is missing**

Given a CSV file does not contain the selected numeric column
When the researcher validates the file
Then the tool fails with a clear error message
And the tool does not create a resulting CSV.

### US-0008 - Preserve all input rows

- **Status:** Approved
- **Source or evidence basis:** CAP-008; approved CR-0001 Project Context section 12.
- **Covered scope IDs:** CAP-008
- **Atomicity:** Single observable outcome
- **Repository issue:** Created

As a researcher
I want the resulting CSV to keep every input row
so that invalid experiment rows remain available for review.

#### Acceptance Criteria

**Scenario: Invalid rows remain in the resulting CSV**

Given a CSV file contains rows with invalid values in the selected numeric column
When the researcher validates the file
Then the resulting CSV contains every input row.

### US-0009 - Add validation-error explanations for invalid rows

- **Status:** Approved
- **Source or evidence basis:** CAP-009; approved CR-0001 Project Context section 12; stakeholder clarification in chat on 2026-09-09 that `validation_errors` should include a detailed explanation about each invalid numeric value.
- **Covered scope IDs:** CAP-009
- **Atomicity:** Single observable outcome
- **Repository issue:** Created

As a researcher
I want invalid rows to include validation-error explanations
so that I can understand the detected problems.

#### Acceptance Criteria

**Scenario: Invalid rows include validation errors**

Given a CSV file contains rows with invalid values in the selected numeric column
When the researcher validates the file
Then each invalid row contains an explanation in the `validation_errors` column.

**Scenario: Validation errors explain the specific invalid numeric problem**

Given a CSV file contains selected-column values that are missing, empty, unparseable as floating-point numbers, NaN, or infinite
When the researcher validates the file
Then each invalid row's `validation_errors` value explains the specific invalid numeric problem detected for that row.

**Scenario: Valid rows have no validation errors**

Given a CSV file contains rows with valid values in the selected numeric column
When the researcher validates the file
Then each valid row has no error explanation in the `validation_errors` column.

### US-0010 - Write the resulting CSV

- **Status:** Approved
- **Source or evidence basis:** CAP-010; approved CR-0001 Project Context section 12.
- **Covered scope IDs:** CAP-010
- **Atomicity:** Single observable outcome
- **Repository issue:** Created

As a researcher
I want the tool to write the resulting CSV
so that I have a validated copy of the experiment data.

#### Acceptance Criteria

**Scenario: Resulting CSV is written**

Given the tool has finished validating the input CSV
When the validation run completes
Then the tool writes a resulting CSV file.

### US-0011 - Download the resulting CSV

- **Status:** Approved
- **Source or evidence basis:** CAP-011; approved CR-0001 Project Context section 12.
- **Covered scope IDs:** CAP-011
- **Atomicity:** Single observable outcome
- **Repository issue:** Created

As a researcher
I want to download the resulting CSV from the Streamlit interface
so that I can save the validated data.

#### Acceptance Criteria

**Scenario: Resulting CSV is downloaded**

Given validation has completed in the Streamlit interface
When the researcher downloads the resulting CSV
Then the interface provides the resulting CSV for download.

### US-0012 - Report validation-error row count

- **Status:** Approved
- **Source or evidence basis:** CAP-012; approved CR-0001 Project Context section 12.
- **Covered scope IDs:** CAP-012
- **Atomicity:** Single observable outcome
- **Repository issue:** Created

As a researcher
I want the CLI to report how many rows contain validation errors
so that I can see the validation result from a command-line run.

#### Acceptance Criteria

**Scenario: Validation-error row count is reported**

Given the CLI has detected rows with validation errors
When the validation run completes
Then the CLI reports the number of rows containing validation errors.

### US-0013 - Display validation-error row count

- **Status:** Approved
- **Source or evidence basis:** CAP-013; approved CR-0001 Project Context section 12.
- **Covered scope IDs:** CAP-013
- **Atomicity:** Single observable outcome
- **Repository issue:** Created

As a researcher
I want the Streamlit interface to display how many rows contain validation errors
so that I can see the validation result before downloading the CSV.

#### Acceptance Criteria

**Scenario: Validation-error row count is displayed**

Given validation has completed in the Streamlit interface
When the validated data is available
Then the interface displays the number of rows containing validation errors.

### US-0014 - Upload a CSV file through Streamlit

- **Status:** Approved
- **Source or evidence basis:** CAP-014; approved CR-0001 Project Context section 12.
- **Covered scope IDs:** CAP-014
- **Atomicity:** Single observable outcome
- **Repository issue:** Created

As a researcher
I want to upload a CSV file through the Streamlit interface
so that I can validate a file without using the command line.

#### Acceptance Criteria

**Scenario: CSV file is uploaded**

Given the Streamlit interface is open
When the researcher uploads a CSV file
Then the interface accepts the CSV file for validation.

### US-0015 - Select the numeric column through Streamlit

- **Status:** Approved
- **Source or evidence basis:** CAP-015; approved CR-0001 Project Context section 12.
- **Covered scope IDs:** CAP-015
- **Atomicity:** Single observable outcome
- **Repository issue:** Created

As a researcher
I want to select the numeric column in the Streamlit interface
so that the interface validates the column I choose.

#### Acceptance Criteria

**Scenario: Numeric column is selected**

Given a CSV file is uploaded in the Streamlit interface
When the researcher selects a numeric column
Then the interface uses that selected column for validation.

### US-0016 - Preview validated data through Streamlit

- **Status:** Approved
- **Source or evidence basis:** CAP-016; approved CR-0001 Project Context section 12.
- **Covered scope IDs:** CAP-016
- **Atomicity:** Single observable outcome
- **Repository issue:** Created

As a researcher
I want to preview validated data in the Streamlit interface
so that I can inspect validation results before downloading the CSV.

#### Acceptance Criteria

**Scenario: Validated data is previewed**

Given validation has completed in the Streamlit interface
When the validated data is available
Then the interface previews the validated data.

### US-0017 - Keep the existing CLI operational

- **Status:** Approved
- **Source or evidence basis:** CAP-017; approved CR-0001 Project Context section 12.
- **Covered scope IDs:** CAP-017
- **Atomicity:** Single observable outcome
- **Repository issue:** Created

As a researcher
I want the existing CLI to remain operational
so that command-line validation workflows continue to work.

#### Acceptance Criteria

**Scenario: Existing CLI still runs**

Given a researcher provides the existing CLI inputs
When the researcher runs the CLI
Then the CLI validates the CSV and produces the resulting CSV.

### Requirement Validation

- **Source evidence recorded:** Yes
- **Approved content changed:** Yes - REQ-0001 is preserved as superseded history; active CR-0001 behavior is recorded under REQ-0002 with new identifiers.
- **Source scope statements omitted:** 0
- **Atomic capabilities without disposition:** 0
- **Compound stories without approved grouping:** 0
- **Coverage matrix/story mapping conflicts:** 0
- **Unsupported product behavior:** 0
- **Unresolved blocking questions:** 0
- **Duplicate repository story references:** 0
- **Overview/detail inconsistencies:** 0
- **Scope coverage validator:** Passed
- **Scope validator command:** `python3 .agents/skills/c-manage-product-requirements/scripts/validate_scope_coverage.py sdlc_docs/00_inception/project_context.md sdlc_docs/01_requirements/product_requirements.md --mode initial-release`
- **Scope validator report synchronized:** Yes
- **Validation result:** Passed

## 4. Approval Record

| Requirement | Decision | Approved by | Role or responsibility | Date | Blocking Issues or Feedback |
|---|---|---|---|---|---|
| REQ-0001 | Approved, superseded by CR-0001 | Edwin Carreño | Software Engineer | 2026-09-09 | None |
| REQ-0001 traceability repair | Approved | Edwin Carreño | Software developer | 2026-09-09 | None |
| REQ-0002 | Approved | Edwin Carreño | Software developer | 2026-09-09 | None |
