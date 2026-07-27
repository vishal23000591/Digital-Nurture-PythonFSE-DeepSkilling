"""
Hands-On 4

Selenium Components

1. WebDriver
   - Controls the browser.
   - Sends commands from Python to Chrome.

2. Selenium Grid
   - Runs tests on multiple browsers and machines.
   - Used for parallel execution.

3. Selenium IDE
   - Browser extension.
   - Used for Record and Playback.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()

options.add_argument("--headless")

driver = webdriver.Chrome(
    service=Service(
        ChromeDriverManager().install()
    ),
    options=options
)

driver.implicitly_wait(10)

driver.get("https://www.lambdatest.com/selenium-playground/")

print(driver.title)

driver.quit()
