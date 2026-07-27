import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def base_url():
    """Session-scoped fixture providing the base URL for LambdaTest Selenium Playground."""
    return "https://www.lambdatest.com/selenium-playground/"


@pytest.fixture(scope="function")
def driver():
    """Function-scoped fixture initializing and tearing down Chrome WebDriver instance."""
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1280,800")

    driver_instance = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    driver_instance.implicitly_wait(5)

    yield driver_instance

    driver_instance.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture screenshot on test failure in POM test suite."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver_instance = item.funcargs.get("driver")
        if driver_instance:
            test_name = item.name.replace("[", "_").replace("]", "_").replace("-", "_")
            driver_instance.save_screenshot(f"{test_name}_failure.png")
