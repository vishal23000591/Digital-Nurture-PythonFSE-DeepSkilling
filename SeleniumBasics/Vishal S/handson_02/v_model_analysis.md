# Hands-On 2: SDLC vs TDLC — V-Model & Agile QA Integration

**Course:** Digital Nurture 5.0 — Python Full Stack Engineer Track  
**Domain:** QA Concepts & Test Automation — Selenium Basics  
**Document:** `v_model_analysis.md`

---

## Task 1: V-Model Mapping

### 9. Complete V-Model Diagram

```
                        SDLC ↔ TDLC V-MODEL DIAGRAM
                        
DEVELOPMENT PHASES (SDLC)                           TESTING PHASES (TDLC)
+------------------------+                         +------------------------+
| Requirements Analysis  | <=====================> |   Acceptance Testing   |
+------------------------+                         +------------------------+
            \                                           /
             \                                         /
   +-------------------+                     +-------------------+
   |   System Design   | <=================> |  System Testing   |
   +-------------------+                     +-------------------+
               \                                   /
                \                                 /
      +--------------------+           +--------------------+
      | Architecture Design| <=======> | Integration Testing|
      +--------------------+           +--------------------+
                  \                             /
                   \                           /
         +-------------------+       +-------------------+
         |   Module Design   | <===> |   Unit Testing    |
         +-------------------+       +-------------------+
                     \                       /
                      \                     /
                       +-------------------+
                       |    CODING (DEV)   |  <--- Bottom Vertex
                       +-------------------+
```

---

### 10. SDLC to TDLC Phase Mappings & Test Artifacts

For each development phase on the left side of the V-Model, corresponding test planning occurs, producing specific test artifacts:

| SDLC Phase (Development) | Corresponding TDLC Phase (Testing) | Test Artifact Produced During Dev Phase |
| :--- | :--- | :--- |
| **Requirements Analysis** | **Acceptance Testing** | **Acceptance Test Plan & User Acceptance Test Cases** based on business user stories. |
| **System Design** | **System Testing** | **System Test Plan & End-to-End Test Scenarios** based on functional system specs. |
| **Architecture Design** | **Integration Testing** | **Integration Test Plan & API Interface Test Cases** covering component interactions. |
| **Module Design** | **Unit Testing** | **Unit Test Specifications & Test Data Suites** covering algorithm logic branches. |
| **Coding** | **Test Execution** | **Executable Source Code & Unit Test Execution Logs**. |

---

### 11. Entry and Exit Criteria for All 4 Testing Levels

```
                   ENTRY CRITERIA  --->  [ TESTING LEVEL ]  --->  EXIT CRITERIA
```

| Testing Level | Entry Criteria (Prerequisites to Start) | Exit Criteria (Criteria to Complete) |
| :--- | :--- | :--- |
| **Unit Testing** | 1. Code module compilation is clean.<br>2. Unit test scripts written and peer-reviewed.<br>3. Developer local environment configured. | 1. 100% of unit tests pass.<br>2. Minimum 85% code statement coverage achieved.<br>3. Zero critical static analysis/linter errors. |
| **Integration Testing**| 1. Unit testing signed off.<br>2. API modules deployed to Integration test environment.<br>3. Interface specs & DB schema migrated. | 1. All API endpoint integration flows pass.<br>2. Database transactions commit/rollback accurately.<br>3. Zero high-severity interface defects open. |
| **System Testing** | 1. Integration testing completed & signed off.<br>2. Full system build deployed to QA environment.<br>3. System test data seeded. | 1. 100% planned system test cases executed.<br>2. Defect density within acceptable SLA.<br>3. Zero Critical or High open defects. |
| **Acceptance Testing** | 1. System testing signed off by QA team.<br>2. Build deployed to UAT / Staging environment.<br>3. UAT test scripts & user accounts ready. | 1. Business stakeholders approve user story execution.<br>2. All acceptance criteria met.<br>3. Formal UAT sign-off document executed. |

---

### 12. Early QA Engagement Points in the V-Model

QA should engage long before the testing phases on the right side of the V-Model. Two critical early engagement points for the Course Management API project are:

1. **Requirements Analysis Phase (Left Side Top):**
   - **Action:** QA participates in business requirement reviews to perform **Testability Analysis**.
   - **Value for Course Management API:** QA identifies vague requirements (e.g., "API should handle high course load") and converts them into precise testable metrics (e.g., "API must handle 100 requests/sec with <200ms latency"). Catching ambiguous logic here costs 10x to 100x less than fixing it after code is written.

2. **Architecture & System Design Phase (Left Side Middle):**
   - **Action:** QA reviews API specs (OpenAPI / Swagger schemas) and DB models.
   - **Value for Course Management API:** QA designs API contract test cases and mock services before developers finish backend endpoints. This allows frontend and backend teams to integrate seamlessly with predefined response schemas.

---

## Task 2: Agile QA and Shift-Left Testing

### 13. Problems Caused by Traditional Waterfall Testing

In Waterfall, testing takes place in a isolated phase after development is 100% complete. For the Course Management API, this causes 3 major problems:

1. **Delayed Defect Discovery:** System bugs (such as database deadlocks during student course enrollment) are found at the very end of the schedule, making root cause fixes extremely expensive and risky.
2. **Severe Schedule Compression (QA Squeeze):** When development delays occur, the project deadline rarely moves. Consequently, the QA testing phase is squeezed from 3 weeks down to 3 days, forcing incomplete testing and shipping untested code.
3. **High Cost of Rework from Misunderstood Specs:** If a developer misinterprets how course credit limits should be calculated, fixing it during late testing requires refactoring API controllers, DB schemas, and frontend forms.

---

### 14. QA Role Across the 4 Agile Ceremonies

```
+-------------------------------------------------------------------------+
|                         AGILE CEREMONIES & QA ROLE                      |
|                                                                         |
| 1. Sprint Planning   --->  Define Acceptance Criteria & Estimate QA     |
| 2. Daily Standup     --->  Share QA Progress & Call Out Blockers        |
| 3. Sprint Review     --->  Demo Tested User Stories to Stakeholders     |
| 4. Retrospective     --->  Improve Quality Metrics & Test Processes     |
+-------------------------------------------------------------------------+
```

- **Sprint Planning:** QA reviews user stories, clarifies edge cases, helps define testable **Acceptance Criteria** (Given-When-Then format), and estimates testing story points.
- **Daily Standup:** QA communicates daily progress (e.g., "Completed API automated scripts for Story #42"), highlights environment blockers, and aligns with developers on bug fixes.
- **Sprint Review (Demo):** QA collaborates with Product Owners to demonstrate fully tested user stories and confirm that acceptance criteria are satisfied in the working software.
- **Sprint Retrospective:** QA presents quality metrics (defect distribution, automation coverage), identifies process bottlenecks, and proposes quality improvements for the next sprint.

---

### 15. Concrete Shift-Left Practices for Course Management API

Shift-Left means pushing testing activities earlier in the SDLC timeline:

| Shift-Left Practice | Application to Course Management API |
| :--- | :--- |
| **(a) Reviewing Requirements for Testability** | QA reviews the course creation user story during refinement and asks: *"What happens if a course code contains special characters like `CS#101`?"*, clarifying validation rules before code is typed. |
| **(b) Test-Driven & Behavior-Driven Dev (TDD/BDD)** | Developers write failing pytest unit tests for course creation logic before writing the API handler code, guaranteeing code is written strictly to pass tests. |
| **(c) Static Code Analysis** | Integrating linters (`flake8`, `ruff`, `bandit`) into the Git commit hook / CI pipeline to detect code formatting bugs, security flaws, and dead code automatically. |
| **(d) API Contract Testing** | Using OpenAPI/Swagger contracts to validate request/response JSON schemas automatically in CI before integrating API endpoints with frontend code. |

---

### 16. Acceptance Criteria in Given-When-Then (Gherkin) Format

**User Story:**  
`As a college admin, I want to create a new course, so that students can enroll in it.`

```gherkin
Feature: Course Creation Management
  As a college admin
  I want to create a new course
  So that students can enroll in it

  # Scenario 1: Happy Path - Successful Course Creation
  Scenario: Create a valid course with all required fields
    Given the user is authenticated as a "College Admin"
    And the course code "CS101" does not exist in the database
    When the admin submits a POST request to "/api/courses/" with:
      | field       | value                            |
      | course_code | CS101                            |
      | title       | Introduction to Computer Science |
      | credits     | 4                                |
      | department  | Computer Science                 |
    Then the response status code should be 201
    And the response body should contain the created course ID
    And the course "CS101" should be stored in the database

  # Scenario 2: Negative Path - Duplicate Course Code
  Scenario: Attempt to create a course with an existing course code
    Given the user is authenticated as a "College Admin"
    And a course with course code "CS101" already exists in the database
    When the admin submits a POST request to "/api/courses/" with:
      | field       | value                            |
      | course_code | CS101                            |
      | title       | Advanced Computer Science        |
      | credits     | 3                                |
      | department  | Computer Science                 |
    Then the response status code should be 409
    And the response error message should be "Course code CS101 already exists."
    And no new record should be created in the database

  # Scenario 3: Negative Path - Missing Required Fields
  Scenario: Attempt to create a course without specifying credits
    Given the user is authenticated as a "College Admin"
    When the admin submits a POST request to "/api/courses/" with:
      | field       | value                            |
      | course_code | MATH201                          |
      | title       | Calculus II                      |
      | credits     |                                  |
      | department  | Mathematics                      |
    Then the response status code should be 400
    And the response error message should state "Field 'credits' is required."
```
