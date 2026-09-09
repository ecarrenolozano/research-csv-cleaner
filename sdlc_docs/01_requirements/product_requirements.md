# Product Requirements

## 1. Document Control

- **Project:** Research CSV Cleaner
- **Mode:** Initial release
- **Source project context or increment issue:** `sdlc_docs/00_inception/project_context.md`
- **Last updated:** 2026-09-09
- **Active scope state:** Approved

## 2. Requirements Overview

| Requirement | Requirement status | Stories | Story status | Source | Repository issues |
|---|---|---|---|---|---|
| REQ-0001 - Local research CSV cleaning | Approved | US-0001, US-0002, US-0003, US-0004, US-0005 | Approved | `sdlc_docs/00_inception/project_context.md`; stakeholder clarification in chat on 2026-09-09 | Not created |

### Source Statement Coverage Register

Record every controlling source statement exactly once. Classify broad category statements such as "manage", "handle", or "support" as `Umbrella`; do not create an umbrella capability or story from them.

| Source ID | Source scope statement | Source location | Statement role | Decomposed into CAP IDs | Rationale |
|---|---|---|---|---|---|
| SRC-001 | Read a CSV file. | `project_context.md` section 12, Included High-Level Capabilities | Atomic | CAP-001 | Single observable capability from the approved MVP boundary. |
| SRC-002 | Validate one required numeric column. | `project_context.md` section 12, Included High-Level Capabilities | Atomic | CAP-002 | Single observable capability from the approved MVP boundary. |
| SRC-003 | Remove rows with invalid values in that column. | `project_context.md` section 12, Included High-Level Capabilities | Atomic | CAP-003 | Single observable capability from the approved MVP boundary. |
| SRC-004 | Write a cleaned CSV file. | `project_context.md` section 12, Included High-Level Capabilities | Atomic | CAP-004 | Single observable capability from the approved MVP boundary. |
| SRC-005 | Report how many rows were removed. | `project_context.md` section 12, Included High-Level Capabilities | Atomic | CAP-005 | Single observable capability from the approved MVP boundary. |

### Source Scope Coverage Matrix

Record only atomic capabilities. Every row must reference one or more Source IDs from the register. Never use an umbrella verb as the atomic capability.

| Scope ID | Atomic capability | Source IDs | Source scope statement | Source location | Disposition | Requirement / Stories | Rationale or approval evidence |
|---|---|---|---|---|---|---|---|
| CAP-001 | Read a CSV file | SRC-001 | Read a CSV file. | `project_context.md` section 12, Included High-Level Capabilities | Covered | REQ-0001 / US-0001 | Single independently observable outcome |
| CAP-002 | Validate one required numeric column | SRC-002 | Validate one required numeric column. | `project_context.md` section 12, Included High-Level Capabilities | Covered | REQ-0001 / US-0002 | Stakeholder clarified invalid numeric values and missing-column behavior in chat on 2026-09-09. |
| CAP-003 | Remove rows with invalid values in the required numeric column | SRC-003 | Remove rows with invalid values in that column. | `project_context.md` section 12, Included High-Level Capabilities | Covered | REQ-0001 / US-0003 | Stakeholder clarified that rows with missing, empty, non-floating-point, NaN, or infinite values in the required numeric column should be removed. |
| CAP-004 | Write a cleaned CSV file | SRC-004 | Write a cleaned CSV file. | `project_context.md` section 12, Included High-Level Capabilities | Covered | REQ-0001 / US-0004 | Single independently observable outcome |
| CAP-005 | Report the number of removed rows | SRC-005 | Report how many rows were removed. | `project_context.md` section 12, Included High-Level Capabilities | Covered | REQ-0001 / US-0005 | Single independently observable outcome |

## 3. Requirements

## REQ-0001 - Local research CSV cleaning

- **Status:** Approved
- **Source:** `sdlc_docs/00_inception/project_context.md`
- **Evidence or basis:** Approved Project Context sections 8, 11, 12, and 17; stakeholder clarification in chat on 2026-09-09.
- **Imported classification:** Not applicable
- **Repository representation:** Not created
- **Repository issue:** Not created
- **Description:** The first release must let a researcher clean one local research CSV file by validating one required numeric column, removing rows with invalid values in that column, writing a cleaned CSV file, and reporting how many rows were removed.
- **Approved by:** Edwin Carreño
- **Reviewer role or responsibility:** Software Engineer
- **Approval date:** 2026-09-09
- **Blocking Issues or Feedback:** None

### US-0001 - Read a CSV file

- **Status:** Approved
- **Source or evidence basis:** CAP-001; approved Project Context section 12.
- **Covered scope IDs:** CAP-001
- **Atomicity:** Single observable outcome
- **Repository issue:** Not created

As a researcher
I want the tool to read a local CSV file
so that I can start cleaning experiment data from a file I received.

#### Acceptance Criteria

**Scenario: CSV input is read**

Given a local CSV file exists
When the researcher runs the tool with that file as input
Then the tool reads the CSV file for cleaning.

### US-0002 - Validate one required numeric column

- **Status:** Approved
- **Source or evidence basis:** CAP-002; approved Project Context section 12; stakeholder clarification in chat on 2026-09-09.
- **Covered scope IDs:** CAP-002
- **Atomicity:** Single observable outcome
- **Repository issue:** Not created

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

### US-0003 - Remove rows with invalid values

- **Status:** Approved
- **Source or evidence basis:** CAP-003; approved Project Context section 12; stakeholder clarification in chat on 2026-09-09.
- **Covered scope IDs:** CAP-003
- **Atomicity:** Single observable outcome
- **Repository issue:** Not created

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

### US-0004 - Write a cleaned CSV file

- **Status:** Approved
- **Source or evidence basis:** CAP-004; approved Project Context section 12.
- **Covered scope IDs:** CAP-004
- **Atomicity:** Single observable outcome
- **Repository issue:** Not created

As a researcher
I want the tool to write a cleaned CSV file
so that I have a cleaned copy of the experiment data.

#### Acceptance Criteria

**Scenario: Cleaned CSV is written**

Given the tool has finished cleaning the input CSV
When the cleaning run completes
Then the tool writes a cleaned CSV file.

### US-0005 - Report removed row count

- **Status:** Approved
- **Source or evidence basis:** CAP-005; approved Project Context section 12.
- **Covered scope IDs:** CAP-005
- **Atomicity:** Single observable outcome
- **Repository issue:** Not created

As a researcher
I want the tool to report how many rows were removed
so that I can see the effect of the cleaning run.

#### Acceptance Criteria

**Scenario: Removed row count is reported**

Given the tool has removed rows during cleaning
When the cleaning run completes
Then the tool reports the number of rows removed.

### Requirement Validation

- **Source evidence recorded:** Yes
- **Approved content changed:** No
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
| REQ-0001 | Approved | Edwin Carreño | Software Engineer | 2026-09-09 | None |
