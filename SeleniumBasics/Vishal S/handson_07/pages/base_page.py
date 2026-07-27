from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Base Page Object class containing common WebDriver actions and waits."""

    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url: str):
        """Navigates to the specified URL."""
        self.driver.get(url)

    def get_title(self) -> str:
        """Returns the current page title."""
        return self.driver.title

    def wait_for_element(self, locator: tuple, timeout: int = 10):
        """Waits for an element to be visible in the DOM."""
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def find_element(self, locator: tuple):
        """Locates and returns an element after waiting for visibility."""
        return self.wait_for_element(locator)

    def click(self, locator: tuple, timeout: int = 10):
        """Waits for element to be clickable and performs a click action."""
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def send_keys(self, locator: tuple, text: str, timeout: int = 10):
        """Waits for element visibility, clears existing text, and types text."""
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(text)
