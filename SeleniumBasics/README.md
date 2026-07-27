# Selenium Basics & Test Automation – Digital Nurture 5.0

This directory contains implementation files, conceptual analysis documents, and test scripts for **Selenium Basics & Test Automation**, part of the **Digital Nurture 5.0 – Python Full Stack Engineer Track**.

It covers the core concepts of software testing, defect lifecycles, V-Model and Agile QA integration, test automation ROI, Selenium WebDriver architecture, locators, dynamic waits, Pytest integration, and the Page Object Model (POM) design pattern.

---

# Repository Structure

```text
SeleniumBasics/
├── README.md                       # Dedicated Selenium Basics README (This file)
└── Vishal S/
    ├── requirements.txt            # Python dependencies for the automation suite
    ├── handson_01/                 # QA Concepts & Defect Lifecycle
    │   └── qa_concepts.md          # Analysis document covering testing types and bug severity
    ├── handson_02/                 # SDLC vs TDLC & V-Model
    │   └── v_model_analysis.md     # Analysis document mapping V-Model and Agile ceremonies
    ├── handson_03/                 # Test Automation Strategy
    │   └── automation_strategy.md  # Analysis document on ROI, flaky tests, and frameworks
    ├── handson_04/                 # WebDriver & Session Setup
    │   ├── setup_test.py           # Headless Chrome session verification
    │   ├── navigation_test.py      # Window sizing, navigation, and screenshots
    │   └── screenshots/
    │       └── playground_screenshot.png
    ├── handson_05/                 # Element Locators & Interaction Basics
    │   ├── locator_demo.py         # Locating input fields using CSS Selectors and Link Text
    │   └── checkbox_demo.py        # Interacting with checkboxes using Explicit Waits
    ├── handson_06/                 # Pytest Integration & Parameterization
    │   ├── conftest.py             # Session and function-scoped driver fixtures
    │   ├── pytest.ini              # Pytest CLI configuration
    │   ├── test_playground.py      # Parameterized tests for forms, checkboxes, and dropdowns
    │   └── report.html             # Generated HTML test execution report
    └── handson_07/                 # Page Object Model (POM) Design Pattern
        ├── conftest.py             # Reusable setup and tear down with screenshot hook
        ├── pytest.ini              # Pytest CLI configuration
        ├── pages/                  # Page Object Abstraction Layer
        │   ├── base_page.py        # Core actions wrapper (waits, clicks, inputs)
        │   ├── simple_form_page.py # Page class for Simple Form Demo
        │   ├── checkbox_page.py    # Page class for Checkbox Demo
        │   ├── dropdown_page.py    # Page class for Select Dropdown Demo
        │   └── input_form_page.py  # Page class for Input Form Submission
        ├── tests/                  # Test Execution Layer
        │   └── test_pom_playground.py # Clean POM-based test suite
        └── report.html             # Generated POM test execution report
```

---

# Technologies & Tools Used

### Languages & Testing Libraries
- **Python 3.x**: The base language for writing test scripts.
- **Selenium WebDriver (v4+)**: Browser automation API to interact with DOM elements dynamically.
- **Pytest**: Core testing framework facilitating parameterization, fixtures, and execution rules.
- **Webdriver Manager**: Automated binary driver management for Chrome/Chromium.

### Reporting & Formatting
- **pytest-html**: Generates interactive HTML execution reports.
- **Markdown & Gherkin (G-W-T)**: For writing structured automation specifications and test documentation.

---

# Detailed Hands-On Breakdown

## [Hands-On 1: QA Concepts, Functional Testing & Defect Lifecycle](file:///Users/vishal/Desktop/Python%20Backend%20Framework%20Solutions/SeleniumBasics/Vishal%20S/handson_01/qa_concepts.md)
- **Objective**: Establish solid theoretical understanding of software testing, defect states, and severity/priority mapping.
- **Key Implementations**:
  - Mapped four levels of testing (Unit, Integration, System, UAT) to a Course Management API.
  - Classified tests as Functional or Non-Functional (Performance & Load metrics).
  - Contrasted Black-Box vs. White-Box testing approaches.
  - Defined the complete Defect Lifecycle from *New* and *Assigned* to *Retest* and *Closed*.
  - Handled severity vs. priority decisions with concrete real-world examples.

## [Hands-On 2: SDLC vs TDLC — V-Model & Agile QA Integration](file:///Users/vishal/Desktop/Python%20Backend%20Framework%20Solutions/SeleniumBasics/Vishal%20S/handson_02/v_model_analysis.md)
- **Objective**: Analyze development lifecycles and understand how QA activities shift left in Agile models.
- **Key Implementations**:
  - Mapped SDLC phases directly to matching TDLC phases inside a classic V-Model.
  - Defined Entry and Exit criteria for Unit, Integration, System, and Acceptance levels.
  - Analyzed early engagement points for QA in Requirements and System Design phases.
  - Discussed traditional Waterfall bottlenecks and mapped out QA roles in Agile Ceremonies.
  - Composed test specifications using Given-When-Then (Gherkin/BDD) format.

## [Hands-On 3: Test Automation Process, Lifecycle & Framework Types](file:///Users/vishal/Desktop/Python%20Backend%20Framework%20Solutions/SeleniumBasics/Vishal%20S/handson_03/automation_strategy.md)
- **Objective**: Learn when to automate, calculate financial ROI, mitigate flaky tests, and compare framework architectures.
- **Key Implementations**:
  - Applied 5 automation suitability criteria to core backend endpoints.
  - Formulated a mathematical Return on Investment (ROI) model to determine the breakeven point.
  - Documented mitigation strategies for flaky tests using dynamic waits.
  - Compared Linear, Modular, Data-Driven, Keyword-Driven, and Hybrid framework architectures.
  - Outlined directory structure of an enterprise Hybrid Automation suite.

## [Hands-On 4: WebDriver Components, Session Setup & Browser Interactions](file:///Users/vishal/Desktop/Python%20Backend%20Framework%20Solutions/SeleniumBasics/Vishal%20S/handson_04/)
- **Objective**: Install Selenium and set up driver sessions, manage browser windows, and perform navigation commands.
- **Key Implementations**:
  - Documented the role of WebDriver, Selenium Grid, and Selenium IDE.
  - Initialized headless Chrome sessions with WebDriver Manager.
  - Performed navigation commands (`driver.get`, `driver.back`), window resizing, and captured screenshots on target pages.

## [Hands-On 5: Element Locators & Interaction Basics](file:///Users/vishal/Desktop/Python%20Backend%20Framework%20Solutions/SeleniumBasics/Vishal%20S/handson_05/)
- **Objective**: Find and manipulate web elements using diverse locator strategies and dynamic waits.
- **Key Implementations**:
  - Leveraged `By.LINK_TEXT` and `By.CSS_SELECTOR` to automate form elements.
  - Implemented dynamic element visibility and clickability checks using `WebDriverWait` and `expected_conditions`.
  - Automated interaction flows with standard input elements and checkboxes.

## [Hands-On 6: Pytest Integration, Parameterization & Reporting](file:///Users/vishal/Desktop/Python%20Backend%20Framework%20Solutions/SeleniumBasics/Vishal%20S/handson_06/)
- **Objective**: Convert scripts into formal test suites using pytest fixtures, parameterization hooks, and report generation.
- **Key Implementations**:
  - Created session-scoped (`base_url`) and function-scoped (`driver`) fixtures.
  - Implemented data-driven verification of forms using `@pytest.mark.parametrize`.
  - Configured custom pytest hooks (`pytest_runtest_makereport`) to automatically save screenshots on failure.
  - Integrated `pytest-html` plugin to generate execution summaries.

## [Hands-On 7: Page Object Model (POM) Design Pattern](file:///Users/vishal/Desktop/Python%20Backend%20Framework%20Solutions/SeleniumBasics/Vishal%20S/handson_07/)
- **Objective**: Structurally refactor test scripts to decouple page objects (UI details) from test cases (business verification).
- **Key Implementations**:
  - Created a robust `BasePage` wrapper class for Selenium actions.
  - Built page classes (`SimpleFormPage`, `CheckboxPage`, `DropdownPage`, `InputFormPage`) to encapsulate element locators and action methods.
  - Authored a clean test suite (`test_pom_playground.py`) with zero direct locator references.
  - Conducted locator maintenance analysis (POM vs. flat script).
