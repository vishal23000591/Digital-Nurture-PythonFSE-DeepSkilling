# Hands-On 7: Page Object Model (POM) Design Pattern

**Course:** Digital Nurture 5.0 — Python Full Stack Engineer Track  
**Domain:** QA Concepts & Test Automation — Selenium Basics  
**Document:** `README.md`

---

## Page Object Model (POM) Architecture Overview

This directory contains a complete, production-grade **Page Object Model (POM)** test automation framework implemented with **Python, Selenium WebDriver, and pytest**.

### Folder Structure
```
handson_07/
├── pages/                          # Page Object Abstraction Layer
│   ├── __init__.py
│   ├── base_page.py                # Base Page class (WebDriver actions, waits, navigation)
│   ├── simple_form_page.py         # Simple Form Demo Page Object
│   ├── checkbox_page.py            # Checkbox Demo Page Object
│   ├── dropdown_page.py            # Select Dropdown Page Object
│   └── input_form_page.py          # Input Form Submit Page Object
│
├── tests/                          # Test Execution Layer
│   ├── __init__.py
│   └── test_pom_playground.py     # Clean test functions with ZERO direct find_element calls
│
├── conftest.py                     # Pytest fixtures (driver, base_url, screenshot on failure)
├── pytest.ini                      # Pytest config options & HTML reporting flags
└── README.md                       # Architecture & Maintenance Documentation
```

---

## Step 59: Locator Maintenance Analysis (Flat Script vs. Page Object Model)

### Question:
*What problem would occur in a flat (non-POM) script if the Submit button's ID changed from `'submit'` to `'btn-submit'`? How does POM solve this?*

---

### 1. Problem in a Flat (Non-POM) Automation Script

In a traditional flat test script (where locator finding logic and test assertions are mixed together in the test files):

```python
# FLAT (NON-POM) SCRIPT DISADVANTAGE:
# If 'submit' ID changes across 20 different test files:
def test_case_1(driver):
    driver.find_element(By.ID, "submit").click() # Hardcoded locator

def test_case_2(driver):
    driver.find_element(By.ID, "submit").click() # Duplicated hardcoded locator

# ... repeated across 20+ test files!
```

- **Massive Maintenance Burden:** If the application developer renames the button ID from `'submit'` to `'btn-submit'`, **every single test file** referencing `driver.find_element(By.ID, "submit")` will fail with a `NoSuchElementException`.
- **High Risk of Error:** The QA engineer has to manually locate and edit 20, 50, or 100+ separate occurrences of the locator across multiple test files. Missing even one instance breaks the entire regression test suite build.
- **Low Readability:** Test functions are cluttered with raw HTML element locators rather than expressing business behavior.

---

### 2. How the Page Object Model (POM) Solves This

In a **Page Object Model** framework architecture, UI locators and interaction mechanisms are encapsulated as class-level constants inside page object classes, while test files contain **zero** `find_element` calls:

```python
# 1. PAGE OBJECT FILE (pages/simple_form_page.py) - Encapsulates Locator
class SimpleFormPage(BasePage):
    # Locator defined EXACTLY ONCE as a class tuple:
    SUBMIT_BTN = (By.ID, "btn-submit") # Updated in ONE single place!

    def click_submit(self):
        self.click(self.SUBMIT_BTN)

# 2. TEST FILE (tests/test_pom_playground.py) - Pure Business Logic
def test_simple_form_submission(driver, base_url):
    page = SimpleFormPage(driver)
    page.click_submit() # Test file remains untouched!
```

#### Key Benefits of POM:
1. **Single Point of Maintenance (DRY Principle):** When the developer changes the element ID from `'submit'` to `'btn-submit'`, you update **one single line of code in one file** (`simple_form_page.py`). All 20+ test cases immediately pass without modifying a single line in any test file.
2. **Clear Separation of Concerns:**
   - **Page Files:** Handle *HOW* to interact with the UI (locators, actions, waits).
   - **Test Files:** Handle *WHAT* to test (test flow, business expectations, assertions).
3. **Readable & Self-Documenting Tests:** Test functions read like business requirements (`page.enter_message("Hello")`, `page.click_submit()`) rather than low-level DOM queries (`driver.find_element(By.ID, "user-message").send_keys("Hello")`).
