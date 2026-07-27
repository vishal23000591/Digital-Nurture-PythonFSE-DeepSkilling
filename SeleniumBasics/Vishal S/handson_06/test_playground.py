import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize("message", ["Hello", "Selenium Automation", "12345"])
def test_simple_form_submission(driver, base_url, message):
    """
    Test parameterised simple form submission.
    Navigates to Simple Form Demo, inputs text, clicks Submit, and asserts displayed message.
    """
    driver.get(f"{base_url}simple-form-demo")

    wait = WebDriverWait(driver, 10)
    user_message_input = wait.until(
        EC.visibility_of_element_located((By.ID, "user-message"))
    )
    user_message_input.clear()
    user_message_input.send_keys(message)

    show_input_button = wait.until(
        EC.element_to_be_clickable((By.ID, "showInput"))
    )
    show_input_button.click()

    message_display = wait.until(
        EC.visibility_of_element_located((By.ID, "message"))
    )
    assert message_display.text == message, f"Expected message '{message}', but got '{message_display.text}'"


def test_checkbox_demo(driver, base_url):
    """
    Test checkbox interaction.
    Navigates to Checkbox Demo, checks single checkbox, asserts state, unchecks, and asserts state.
    """
    driver.get(f"{base_url}checkbox-demo")

    wait = WebDriverWait(driver, 10)
    checkbox = wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//input[@type='checkbox'])[1]"))
    )

    if not checkbox.is_selected():
        checkbox.click()

    assert checkbox.is_selected(), "Expected checkbox to be selected after click."

    checkbox.click()
    assert not checkbox.is_selected(), "Expected checkbox to be deselected after second click."


def test_dropdown_selection(driver, base_url):
    """
    Test dropdown selection using Select class.
    Navigates to Select Dropdown List demo, chooses 'Wednesday', and asserts selected option.
    """
    driver.get(f"{base_url}select-dropdown-demo")

    wait = WebDriverWait(driver, 10)
    dropdown_element = wait.until(
        EC.visibility_of_element_located((By.ID, "select-demo"))
    )

    select = Select(dropdown_element)
    select.select_by_visible_text("Wednesday")

    selected_option = select.first_selected_option
    assert selected_option.text == "Wednesday", f"Expected 'Wednesday', but got '{selected_option.text}'"

    displayed_text_element = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".selected-value"))
    )
    assert "Wednesday" in displayed_text_element.text, f"Expected 'Wednesday' in displayed text, got '{displayed_text_element.text}'"
