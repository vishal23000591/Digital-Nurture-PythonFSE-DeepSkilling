from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckboxPage(BasePage):
    """Page Object for Checkbox Demo page."""

    # Class-level locators
    SINGLE_CHECKBOX = (By.XPATH, "(//input[@type='checkbox'])[1]")
    OPTION1_CHECKBOX = (By.XPATH, "//label[contains(text(),'Option 1')]/preceding-sibling::input | (//input[@type='checkbox'])[2]")

    def check_option(self, index: int = 1):
        """Checks the specified checkbox if not already selected."""
        locator = self.SINGLE_CHECKBOX if index == 1 else self.OPTION1_CHECKBOX
        element = self.wait_for_element(locator)
        if not element.is_selected():
            self.click(locator)

    def uncheck_option(self, index: int = 1):
        """Unchecks the specified checkbox if selected."""
        locator = self.SINGLE_CHECKBOX if index == 1 else self.OPTION1_CHECKBOX
        element = self.wait_for_element(locator)
        if element.is_selected():
            self.click(locator)

    def is_option_checked(self, index: int = 1) -> bool:
        """Returns True if the specified checkbox is checked, False otherwise."""
        locator = self.SINGLE_CHECKBOX if index == 1 else self.OPTION1_CHECKBOX
        element = self.wait_for_element(locator)
        return element.is_selected()
