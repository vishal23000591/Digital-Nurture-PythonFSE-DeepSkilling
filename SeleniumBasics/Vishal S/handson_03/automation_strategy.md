# Hands-On 3: Test Automation Process, Lifecycle & Framework Types

**Course:** Digital Nurture 5.0 — Python Full Stack Engineer Track  
**Domain:** QA Concepts & Test Automation — Selenium Basics  
**Document:** `automation_strategy.md`

---

## Task 1: Automation Decision and Test Case Selection

### 17. 5 Criteria for Deciding What to Automate

| # | Criterion | Explanation | Application to Scenario: `POST /api/courses/ returns 201` |
| :-: | :--- | :--- | :--- |
| **1** | **Frequency & Repetitiveness** | Tests that must be executed frequently (e.g., on every pull request, daily CI build, or release build) yield high time savings when automated. | **Pass:** This core endpoint test will be executed hundreds of times across every CI build during regression testing. |
| **2** | **Risk & Business Criticality** | Features critical to core business revenue or operations must work reliably; automated testing guarantees immediate feedback on regression. | **Pass:** Course creation is the core business capability of the API; a failure completely blocks the application. |
| **3** | **Technical Stability** | Automated tests require a stable target API or UI contract. Automating unstable, rapidly changing features causes excessive script maintenance. | **Pass:** The REST API endpoint payload structure (`/api/courses/`) is standardized and stable. |
| **4** | **Data-Driven Requirements** | Tests requiring execution across numerous data combinations/permutations (e.g., various payload inputs) are ideal for automated parameterization. | **Pass:** Endpoint must be verified with various valid payloads (different departments, credit values, title lengths). |
| **5** | **Feasibility & Execution Time** | Tests that are human-error prone or take significant manual effort to set up benefit immediately from script execution speed. | **Pass:** Automated execution takes < 1 second versus manual Postman payload composition taking ~2 minutes. |

**Verdict:** The scenario satisfies all 5 criteria and is a **Prime Candidate for Test Automation**.

---

### 18. Automate vs. Manual Decisions for 6 Test Scenarios

| Scenario | Decision | Detailed Justification |
| :--- | :-: | :--- |
| **(a) Regression test for all CRUD endpoints after every code change.** | **Automate** | Highly repetitive, predictable input/output, executed on every CI build. Manual execution would create a major testing bottleneck. |
| **(b) Exploratory testing of a new search feature.** | **Manual** | Requires human intuition, creative input variation, visual assessment, and ad-hoc problem investigation. Cannot be scripted in advance. |
| **(c) Performance test: 100 concurrent users calling `GET /api/courses/`.** | **Automate** | Physically impossible for human testers to execute 100 simultaneous requests manually; requires load tools (Locust/JMeter). |
| **(d) UI test for the login form.** | **Automate** | Critical path test, executed frequently across regression cycles, with predictable UI inputs and expected redirect states. |
| **(e) Verify the API documentation (Swagger) is accurate.** | **Manual** | One-time visual and contextual inspection comparing documentation text readability against business specs. |
| **(f) Smoke test: verify the API is reachable after deployment.** | **Automate** | Fast, repetitive health-check test executed immediately post-deployment in CI/CD pipeline to gate deployment success. |

---

### 19. Test Automation ROI Definition & Mathematical Calculation

#### Definition:
**Test Automation Return on Investment (ROI)** is a metric evaluating whether the time/cost invested in developing and maintaining automated test scripts yields net savings compared to performing the same tests manually over time.

$$\text{ROI} = \frac{\text{Manual Testing Cost} - (\text{Automation Development Cost} + \text{Maintenance Cost})}{\text{Automation Development Cost} + \text{Maintenance Cost}} \times 100\%$$

#### Given Scenario Parameters:
- **Initial Automation Script Creation Time:** $4.0$ hours ($240$ minutes).
- **Manual Test Execution Time per Run:** $0.5$ hours ($30$ minutes).
- **Maintenance Overhead:** $0.0$ hours for Runs 1 to 10; $20\%$ of manual execution time ($0.2 \times 0.5\text{ h} = 0.1\text{ h} = 6\text{ mins}$) per run starting from Run 11 onwards.

#### Cumulative Effort Calculation Table:

| Run Number ($N$) | Cumulative Manual Time (Hours) | Cumulative Automation Time (Hours) | Net Time Saved (Hours) | Status / ROI Stage |
| :-: | :-: | :-: | :-: | :--- |
| **1** | $0.5$ | $4.00$ | $-3.50$ | Investment Phase |
| **2** | $1.0$ | $4.00$ | $-3.00$ | Investment Phase |
| **4** | $2.0$ | $4.00$ | $-2.00$ | Investment Phase |
| **6** | $3.0$ | $4.00$ | $-1.00$ | Investment Phase |
| **8** | **4.0** | **4.00** | **0.00** | **BREAKEVEN POINT** |
| **9** | **4.5** | **4.00** | **+0.50** | **POSITIVE ROI ACHIEVED (+0.5 hrs saved)** |
| **10** | $5.0$ | $4.00$ | $+1.00$ | Positive ROI (+1.0 hr saved) |
| **11** | $5.5$ | $4.10$ | $+1.40$ | Positive ROI (Includes 0.1h maintenance) |
| **12** | $6.0$ | $4.20$ | $+1.80$ | Positive ROI |
| **15** | $7.5$ | $4.50$ | $+3.00$ | High Positive ROI (+3.0 hrs saved) |

#### Conclusion:
- The automation script reaches the **Breakeven Point at Run 8** (where cumulative manual effort equals 4.0 hours).
- **From Run 9 onwards, the automation pays for itself**, generating positive time savings.

---

### 20. Flaky Tests: Analysis and Fix Strategies

#### Definition:
A **Flaky Test** is an automated test script that yields non-deterministic results — passing on some runs and failing on others — without any underlying changes to the source code or test environment.

#### Example:
A Selenium test clicks the "Submit" button on a course form, but fails intermittently with `NoSuchElementException` or `ElementClickInterceptedException` because an AJAX spinner overlay is still disappearing on slower network runs.

#### 3 Strategies to Prevent/Fix Flaky Tests in Selenium:
1. **Eliminate Hardcoded Sleeps (`time.sleep`):** Replace arbitrary `time.sleep(5)` calls with dynamic **Explicit Waits (`WebDriverWait` + `ExpectedConditions`)** that poll until specific DOM conditions (e.g. element clickability) are met.
2. **Use Unique, Dynamic-Resilient Locators:** Avoid brittle absolute XPaths (e.g., `/html/body/div[2]/form/div[3]/button`). Use static IDs, unique attributes, or dedicated test attributes (`data-testid="submit-btn"`).
3. **Ensure Test Isolation & Clean Setup/Teardown:** Avoid dependencies between test cases where Test B relies on data left over by Test A. Use pytest fixtures with database reset/re-seeding to ensure fresh state for every test.

---

## Task 2: Compare Automation Framework Types

### 21. Framework Architecture Comparison

```
+-------------------------------------------------------------------------+
|                    AUTOMATION FRAMEWORK TYPES                           |
|                                                                         |
|  [Linear] ----> [Modular] ----> [Data-Driven] ----> [Keyword] ----> [Hybrid]|
|  Record/       Page Object      Parametrized        Action Words    Combines|
|  Playback      Abstraction      Data Files          Table Driven    All 3   |
+-------------------------------------------------------------------------+
```

| Framework Type | One-Paragraph Description | Key Advantage | Key Disadvantage | Course Management Example |
| :--- | :--- | :--- | :--- | :--- |
| **Linear (Record & Playback)** | Sequentially recorded scripts where locators, test data, and actions are hardcoded directly into a single file without abstraction. | Extremely fast to create for one-off proof of concepts. | High maintenance cost; any UI change breaks all scripts. | Single script recording admin login and clicking course creation. |
| **Modular** | Divides application UI into independent reusable modules/classes (e.g., Page Object Model) separating UI locators from test logic. | High code reusability; locator changes are updated in one place. | Requires higher upfront setup and OOP programming knowledge. | `LoginPage` class containing login methods reused across test cases. |
| **Data-Driven** | Separates test logic from test input data, reading inputs/expected results from external data files (CSV, Excel, JSON). | Easily tests hundreds of data combinations without duplicating script code. | Managing external data schemas and parsing logic adds complexity. | Reading 50 invalid course payloads from a CSV file to test validation errors. |
| **Keyword-Driven** | Action keywords (e.g., `Click`, `EnterText`, `VerifyText`) are stored in tables/spreadsheets and interpreted by an execution engine. | Enables non-technical team members to compose tests using keywords. | Building and maintaining the underlying keyword engine requires high effort. | Excel sheet with columns: `Action: EnterText`, `Target: #username`, `Value: admin`. |
| **Hybrid** | Combines the best features of Modular (POM), Data-Driven (parameterization), and optional BDD/Keyword frameworks. | Maximum scalability, maintainability, and data flexibility for enterprise suites. | Most complex architecture to design and configure initially. | Pytest + Page Object Model + parameterized test data files + HTML reporting. |

---

### 22. Recommended Framework for Team Scenario

#### Scenario Requirements:
- Test login with **50 different user/password combinations**.
- **Reuse login steps** across 20 test cases.
- Support both **technical and non-technical team members**.

#### Recommendation:
**Hybrid Framework combining Modular (Page Object Model) + Data-Driven (pytest parameterize/CSV) + Behavior-Driven Development (BDD / Gherkin via Behave).**

#### Justification:
1. **Modular (Page Object Model):** Solves requirement #2 by encapsulating login steps into a reusable `LoginPage` method (`login_page.login(user, pwd)`), allowing all 20 test cases to call this single method.
2. **Data-Driven:** Solves requirement #1 by feeding the 50 user/password combinations from an external CSV/JSON file or `@pytest.mark.parametrize` hook without duplicating test code.
3. **BDD / Keyword Layer (Behave/Gherkin):** Solves requirement #3 by allowing non-technical team members to write test scenarios in plain English Gherkin (`Given user is on login page / When user logs in with "<username>" / Then dashbaord displays`), while technical engineers implement the underlying Page Objects.

---

### 23. Hybrid Framework Folder Structure

```
CourseManagement_Automation_Suite/
│
├── config/                         # Environment & Global Configuration
│   ├── config.ini                  # Base URLs, timeouts, browser flags
│   └── pytest.ini                  # Pytest command-line options & markers
│
├── data/                           # External Test Data Files (Data-Driven)
│   ├── login_credentials.csv       # 50 user/password test permutations
│   └── course_payloads.json        # Test payloads for course API tests
│
├── pages/                          # Page Object Classes (Modular Layer)
│   ├── base_page.py                # Core wrapper (waits, clicks, navigation)
│   ├── login_page.py               # Login page locators & actions
│   ├── dashboard_page.py           # Dashboard locators & actions
│   └── course_page.py              # Course management locators & actions
│
├── utils/                          # Shared Utility Helpers
│   ├── driver_factory.py           # Browser driver initialization (Chrome/Firefox)
│   ├── csv_reader.py               # Data parser utility for CSV files
│   └── logger.py                   # Centralized logging helper
│
├── tests/                          # Automated Test Case Scripts
│   ├── conftest.py                 # Pytest fixtures (driver setup, teardown, hooks)
│   ├── test_login.py               # Data-driven login test suite
│   └── test_course_creation.py    # Course creation test suite
│
├── reports/                        # Execution Reports & Screenshots
│   ├── html_report.html            # Pytest HTML execution report
│   └── screenshots/                # Screenshots captured automatically on failure
│
└── requirements.txt                # Python package dependencies
```
