import sys
import os

# Add parent directory to sys.path to allow importing pages package cleanly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pages.simple_form_page import SimpleFormPage
from pages.checkbox_page import CheckboxPage
from pages.dropdown_page import DropdownPage
from pages.input_form_page import InputFormPage


def test_simple_form_submission(driver, base_url):
    """
    Refactored Simple Form Submission test using Page Object Model (SimpleFormPage).
    Contains ZERO direct driver.find_element calls.
    """
    page = SimpleFormPage(driver)
    page.navigate_to(f"{base_url}simple-form-demo/")
    page.enter_message("Hello Selenium")
    page.click_submit()

    assert page.get_displayed_message() == "Hello Selenium", (
        f"Expected 'Hello Selenium', got '{page.get_displayed_message()}'"
    )


def test_checkbox_demo(driver, base_url):
    """
    Refactored Checkbox Demo test using Page Object Model (CheckboxPage).
    Contains ZERO direct driver.find_element calls.
    """
    page = CheckboxPage(driver)
    page.navigate_to(f"{base_url}checkbox-demo/")

    page.check_option(1)
    assert page.is_option_checked(1), "Expected option 1 to be checked."

    page.uncheck_option(1)
    assert not page.is_option_checked(1), "Expected option 1 to be unchecked."


def test_dropdown_selection(driver, base_url):
    """
    Refactored Select Dropdown test using Page Object Model (DropdownPage).
    Contains ZERO direct driver.find_element calls.
    """
    page = DropdownPage(driver)
    page.navigate_to(f"{base_url}select-dropdown-demo/")

    page.select_day("Wednesday")
    assert page.get_selected_day() == "Wednesday", (
        f"Expected selected day 'Wednesday', got '{page.get_selected_day()}'"
    )
    assert "Wednesday" in page.get_displayed_message(), (
        f"Expected 'Wednesday' in displayed text, got '{page.get_displayed_message()}'"
    )


def test_input_form_submit(driver, base_url):
    """
    Input Form Submit test using Page Object Model (InputFormPage).
    Fills out complex input form, submits, and asserts success message.
    Contains ZERO direct driver.find_element calls.
    """
    page = InputFormPage(driver)
    page.navigate_to(f"{base_url}input-form-demo/")

    page.fill_form(
        name="John Doe",
        email="johndoe@example.com",
        password="SecretPassword123",
        company="TechCorp Inc",
        website="https://example.com",
        country="United States",
        city="New York",
        address1="123 Automation Ave",
        address2="Suite 400",
        state="NY",
        zipcode="10001"
    )

    page.submit_form()

    success_msg = page.get_success_message()
    assert "Thanks for contacting us" in success_msg or "succesfully" in success_msg.lower(), (
        f"Expected success message upon form submission, but got: '{success_msg}'"
    )
