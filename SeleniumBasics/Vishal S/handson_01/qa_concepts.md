# Hands-On 1: QA Concepts, Functional Testing & Defect Lifecycle

**Course:** Digital Nurture 5.0 — Python Full Stack Engineer Track  
**Domain:** QA Concepts & Test Automation — Selenium Basics  
**Document:** `qa_concepts.md`

---

## Task 1: Map Testing Types to a Real System

### 1. Concrete Test Cases Across Test Levels for Course Management API

| Testing Type | Description & Purpose | Concrete Test Case for Course Management API |
| :--- | :--- | :--- |
| **Unit Testing** | Testing an individual component, method, or function in total isolation from external dependencies (e.g., database, network). | **Test Case:** Validate course code format function `validate_course_code(code: str)`.<br>**Verification:** Pass `"CS101"` (valid) to ensure it returns `True`, and `"101-CS"` (invalid) to ensure it returns `False`, mocking out all DB calls. |
| **Integration Testing** | Testing the interaction and interface between two or more integrated modules (e.g., API layer + Database layer). | **Test Case:** Verify persistence upon executing `POST /api/courses/` with a valid JSON payload (`{"code": "CS101", "name": "Python 101", "credits": 4}`).<br>**Verification:** Confirm that the endpoint returns `201 Created` AND an SQL query directly to PostgreSQL confirms a new record exists in the `courses` table with ID `101`. |
| **System Testing** | Testing the complete, fully integrated end-to-end software application to evaluate compliance with specified requirements. | **Test Case:** End-to-end course creation, student enrollment, and capacity tracking.<br>**Verification:** Admin creates course `CS101` (capacity 30) via API -> Student registers via API -> Capacity decrements to 29 -> Notification service dispatches confirmation email to student log. |
| **User Acceptance Testing (UAT)** | Testing performed by end users or domain experts (e.g., College Admin) in a business environment to confirm system readiness for production deployment. | **Test Case:** College Admin batch-imports semester courses.<br>**Verification:** College Admin logs into the Admin Portal UI, uploads a CSV file containing 15 new course offerings, verifies batch preview, clicks "Confirm Import", and verifies all 15 courses appear under their department catalog. |

---

### 2. Functional vs. Non-Functional Classification & Example

- **Classification of Above Test Cases:**
  - All four test cases detailed in Step 1 are **Functional Tests** because they validate *what* the system is supposed to do according to functional business logic and specification requirements.

- **Non-Functional Test Example for Course Management API:**
  - **Category:** *Performance & Load Testing*
  - **Test Case:** Execute concurrent `GET /api/courses/` requests under peak traffic conditions.
  - **Scenario:** Simulate **200 concurrent user sessions** requesting the active course catalog over a 10-minute duration using Locust/JMeter.
  - **Metric/Criterion:** Average response latency must remain **< 200 ms**, 95th percentile latency **< 500 ms**, and error rate must be **0.00%** (zero HTTP 5xx errors).

---

### 3. Black-Box Testing vs. White-Box Testing

```
+-------------------------------------------------------------------------+
|                          BLACK-BOX TESTING                              |
|   Inputs  --->  [ Software System (Internal Code Hidden) ]  ---> Outputs |
|   Focus: Functional behavior, inputs, expected outputs, user flows      |
|   Role: QA Testers, Automation Engineers, UAT Users                     |
+-------------------------------------------------------------------------+

+-------------------------------------------------------------------------+
|                          WHITE-BOX TESTING                              |
|   Inputs  --->  [ Code Logic / Branches / Data Structures ] ---> Outputs |
|   Focus: Branch coverage, statement coverage, memory/resource leaks     |
|   Role: Software Developers, Code Reviewers                             |
+-------------------------------------------------------------------------+
```

- **Black-Box Testing (Specification-Based):**
  - Testing the application without any knowledge of internal code structure, implementation language, or database schemas.
  - Tests are designed strictly based on requirements and specifications.
  - **Who performs it:** QA Engineers, Software Testers, and End Users during UAT.

- **White-Box Testing (Structural / Clear-Box):**
  - Testing the internal structure, code paths, branches, conditions, and internal data flows with complete access to the source code.
  - Tests verify line coverage, branch coverage, and internal logic algorithms.
  - **Who performs it:** Software Developers (during Unit & Code Review phases) and specialized White-Box Test Automation Engineers.

---

### 4. Formal Test Cases for `POST /api/courses/` Endpoint

| Test Case ID | Description | Preconditions | Test Steps | Expected Result | Actual Result | Pass/Fail |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC_API_001** | Verify successful course creation with all valid required fields (Happy Path). | API server is running; database is reachable; user is authenticated with Admin role. | 1. Send `POST` request to `/api/courses/`<br>2. Headers: `Content-Type: application/json`<br>3. Body: `{"course_code": "CS101", "title": "Intro to Computer Science", "credits": 3, "department": "CS"}` | HTTP Status `201 Created`. Response JSON contains unique `id`, `course_code: "CS101"`, `created_at` timestamp. | | |
| **TC_API_002** | Verify error handling when attempting to create a course with a duplicate course code. | Course code `"CS101"` already exists in the database. | 1. Send `POST` request to `/api/courses/`<br>2. Body: `{"course_code": "CS101", "title": "Advanced CS", "credits": 4, "department": "CS"}` | HTTP Status `409 Conflict` (or `400 Bad Request`). Response JSON payload: `{"error": "Course code CS101 already exists."}`. No duplicate row inserted. | | |
| **TC_API_003** | Verify validation error response when mandatory field (`credits`) is missing from request body. | API server is running; user is authenticated. | 1. Send `POST` request to `/api/courses/`<br>2. Body: `{"course_code": "MATH201", "title": "Calculus II", "department": "MATH"}` | HTTP Status `400 Bad Request` (or `422 Unprocessable Entity`). Response payload explicitly states: `"Field 'credits' is required."` | | |

---

## Task 2: Defect Lifecycle & Severity Classification

### 5. The Complete Defect Lifecycle

```
  +-------+      Assign       +----------+      Open       +------+
  |  NEW  |  -------------->  | ASSIGNED | ------------->  | OPEN |
  +-------+                   +----------+                 +------+
      |                            |                          |
      | Reject                     | Defer                    | Fix
      v                            v                          v
+----------+                 +----------+                 +-------+
| REJECTED |                 | DEFERRED |                 | FIXED |
+----------+                 +----------+                 +-------+
                                                              |
                                                              | Retest
                                                              v
+----------+                 Verify                       +---------+
|  CLOSED  |  <-----------------------------------------  | RETEST  |
+----------+                                              +---------+
```

#### Defect States Description:
1. **New:** Defect is logged by QA for the first time with complete steps to reproduce and environment logs.
2. **Assigned:** Lead QA / Manager reviews and assigns the defect to a specific Developer or Team.
3. **Open:** Developer analyzes the bug and starts working on a fix.
4. **Fixed:** Developer resolves the code issue, writes unit tests, passes local builds, and deploys the fix to the test environment.
5. **Retest:** QA executes the original test case in the test environment to verify the fix.
6. **Verified:** QA confirms the fix works as expected with no regression.
7. **Closed:** Defect is formally closed in the bug tracking tool (e.g. Jira).

#### Special Alternative Paths:
- **Rejected:** The Developer or Lead determines the report is invalid, not reproducible, working as designed per specs, or a duplicate. The bug is closed without code changes.
- **Deferred:** The bug is acknowledged as valid, but due to low priority, low severity, or release scope constraints, fixing it is postponed to a future sprint/version.

---

### 6. Bug Severity & Priority Classification

| Bug Description | Severity | Priority | Detailed Justification |
| :--- | :--- | :--- | :--- |
| **a) `POST /api/courses/` returns 500 Internal Server Error for all requests.** | **Critical** | **P1 (Blocker)** | **Severity:** System is completely unusable for course creation; zero workarounds exist.<br>**Priority:** Core business functionality is blocked; must be fixed immediately before any deployment or testing can continue. |
| **b) Course names longer than 150 characters are silently truncated without an error.** | **Medium** | **P3** | **Severity:** Corrupts/truncates data silently (data integrity concern), but affects only an extreme edge case (rarely are course titles > 150 chars).<br>**Priority:** Not blocking core operations; can be scheduled in an upcoming sprint. |
| **c) The `/docs` Swagger page has a typo in the API description.** | **Low** | **P4** | **Severity:** Purely cosmetic documentation error; zero impact on API code execution or functionality.<br>**Priority:** Lowest priority fix; can be addressed during routine documentation cleanups. |
| **d) Login with correct credentials occasionally returns 401 on the first attempt (intermittent).** | **High** | **P1** | **Severity:** Intermittent failure points to serious underlying system instability (e.g., auth service race conditions, database session sync delays).<br>**Priority:** High urgency because intermittent bugs damage user trust and are harder to diagnose if delayed. |

---

### 7. Formal Defect Report for Bug (a)

```markdown
================================================================================
DEFECT REPORT: DEF-101
================================================================================
Defect ID:          DEF-101
Title:              [POST /api/courses/] HTTP 500 Internal Server Error returned 
                    on all course creation requests
Environment:        Staging Environment (Linux Ubuntu 22.04 LTS, PostgreSQL 14.2)
Build Version:      v1.4.2-build.88
Severity:           Critical
Priority:           P1 (Blocker)
Reported By:        QA Automation Engineer
Assigned To:        Backend Lead Developer
Date Reported:      2026-07-26

--------------------------------------------------------------------------------
STEPS TO REPRODUCE:
--------------------------------------------------------------------------------
1. Open Postman or execute cURL command targeting Staging API base URL.
2. Set Request Method to POST and URL to:
   https://staging-api.college.edu/api/courses/
3. Set Header: Content-Type: application/json
4. Provide valid body payload:
   {
     "course_code": "CS101",
     "title": "Introduction to Computer Science",
     "credits": 4,
     "department": "CS"
   }
5. Click 'Send' to submit request.

--------------------------------------------------------------------------------
EXPECTED RESULT:
--------------------------------------------------------------------------------
API returns HTTP Status Code 201 Created with JSON response containing generated 
course ID and course details.

--------------------------------------------------------------------------------
ACTUAL RESULT:
--------------------------------------------------------------------------------
API returns HTTP Status Code 500 Internal Server Error with body payload:
{"detail": "Internal Server Error"}

--------------------------------------------------------------------------------
ATTACHMENTS:
--------------------------------------------------------------------------------
1. screenshot_of_500_error.png (Postman execution screenshot)
2. server_app_log.txt (Backend stack trace showing NullPointer in CourseService.py)
================================================================================
```

---

### 8. Difference Between Severity and Priority (With Real-World Example)

- **Severity (Technical Impact):** Refers to the technical degree of impact a defect has on the software architecture, system stability, or data integrity. Defined by **QA**.
- **Priority (Business Urgency):** Refers to how urgently the defect must be fixed based on business goals, release schedules, or customer visibility. Defined by **Product Managers / Business Leads**.

```
                        SEVERITY vs PRIORITY MATRIX
         +-------------------------------------------------------+
         | High Severity / Low Priority  | High Severity / High  |
         | (Obscure admin crash)         | (Main Checkout 500)   |
  HIGH   |-------------------------------+-----------------------|
SEVERITY | Low Severity / Low Priority   | Low Severity / High   |
         | (Minor typo on sub-page)      | (Company logo typo    |
  LOW    |                               |  on Homepage)         |
         +-------------------------------------------------------+
                           LOW                  HIGH
                                   PRIORITY
```

#### Real-World Example: High Severity but Low Priority
- **Scenario:** The background automated annual log archival utility crashes with a memory dump (`High Severity`) when archiving data for fiscal years prior to 2010.
- **Why High Severity:** System crashes completely and throws an unhandled exception.
- **Why Low Priority:** This annual script is only run once a year in December by a single system admin, and affected archived data is 16+ years old. The release planned for next week is focused on student enrollment. Hence, the bug fix can be deferred to a future maintenance cycle (`P3/P4 Priority`).

#### Real-World Example: Low Severity but High Priority
- **Scenario:** The company logo image on the public login page is slightly stretched and has a typo in the brand slogan (`Low Severity`).
- **Why Low Severity:** Software functions perfectly; users can log in with zero functional issues.
- **Why High Priority:** Today is the major public product launch press conference. The brand damage is unacceptable, requiring an immediate hotfix (`P1 Priority`).
