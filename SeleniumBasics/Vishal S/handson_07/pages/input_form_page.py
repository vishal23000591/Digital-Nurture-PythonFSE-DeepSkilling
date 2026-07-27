from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class InputFormPage(BasePage):
    """Page Object for Input Form Submit page."""

    # Class-level locators (tuples)
    NAME_INPUT = (By.ID, "name")
    EMAIL_INPUT = (By.ID, "inputEmail4")
    PASSWORD_INPUT = (By.ID, "inputPassword4")
    COMPANY_INPUT = (By.ID, "company")
    WEBSITE_INPUT = (By.ID, "websitename")
    COUNTRY_SELECT = (By.NAME, "country")
    CITY_INPUT = (By.ID, "inputCity")
    ADDRESS1_INPUT = (By.ID, "inputAddress1")
    ADDRESS2_INPUT = (By.ID, "inputAddress2")
    STATE_INPUT = (By.ID, "inputState")
    ZIP_INPUT = (By.ID, "inputZip")
    SUBMIT_BTN = (By.XPATH, "//button[text()='Submit']")
    SUCCESS_MSG = (By.CSS_SELECTOR, ".success-msg")

    def fill_form(
        self,
        name: str,
        email: str,
        password: str,
        company: str,
        website: str,
        country: str,
        city: str,
        address1: str,
        address2: str,
        state: str,
        zipcode: str
    ):
        """Fills out all fields on the Input Form Submit page."""
        self.send_keys(self.NAME_INPUT, name)
        self.send_keys(self.EMAIL_INPUT, email)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.send_keys(self.COMPANY_INPUT, company)
        self.send_keys(self.WEBSITE_INPUT, website)

        country_element = self.wait_for_element(self.COUNTRY_SELECT)
        select_country = Select(country_element)
        select_country.select_by_visible_text(country)

        self.send_keys(self.CITY_INPUT, city)
        self.send_keys(self.ADDRESS1_INPUT, address1)
        self.send_keys(self.ADDRESS2_INPUT, address2)
        self.send_keys(self.STATE_INPUT, state)
        self.send_keys(self.ZIP_INPUT, zipcode)

    def submit_form(self):
        """Clicks the Submit button."""
        self.click(self.SUBMIT_BTN)

    def get_success_message(self) -> str:
        """Returns the success message text displayed upon successful form submission."""
        element = self.wait_for_element(self.SUCCESS_MSG)
        return element.text
