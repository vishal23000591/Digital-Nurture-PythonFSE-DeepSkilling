from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class DropdownPage(BasePage):
    """Page Object for Select Dropdown List demo page."""

    # Class-level locators
    SELECT_DROPDOWN = (By.ID, "select-demo")
    SELECTED_VALUE_TEXT = (By.CSS_SELECTOR, ".selected-value")

    def select_day(self, day_name: str):
        """Selects a day option from the dropdown by visible text."""
        element = self.wait_for_element(self.SELECT_DROPDOWN)
        select = Select(element)
        select.select_by_visible_text(day_name)

    def get_selected_day(self) -> str:
        """Returns the currently selected option text from the Select element."""
        element = self.wait_for_element(self.SELECT_DROPDOWN)
        select = Select(element)
        return select.first_selected_option.text

    def get_displayed_message(self) -> str:
        """Returns the displayed selected value text on the page."""
        element = self.wait_for_element(self.SELECTED_VALUE_TEXT)
        return element.text
