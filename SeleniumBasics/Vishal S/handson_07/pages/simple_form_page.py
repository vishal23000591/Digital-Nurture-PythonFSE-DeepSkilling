from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SimpleFormPage(BasePage):
    """Page Object for Simple Form Demo page."""

    # Class-level locators (tuples)
    MESSAGE_INPUT = (By.ID, "user-message")
    SHOW_INPUT_BTN = (By.ID, "showInput")
    DISPLAYED_MESSAGE = (By.ID, "message")

    def enter_message(self, text: str):
        """Enters message into the input field."""
        self.send_keys(self.MESSAGE_INPUT, text)

    def click_submit(self):
        """Clicks the 'Get Checked Value' / Submit button."""
        self.click(self.SHOW_INPUT_BTN)

    def get_displayed_message(self) -> str:
        """Returns the displayed message text."""
        element = self.wait_for_element(self.DISPLAYED_MESSAGE)
        return element.text
