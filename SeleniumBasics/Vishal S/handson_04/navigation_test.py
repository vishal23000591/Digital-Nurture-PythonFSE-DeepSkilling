from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.implicitly_wait(10)

driver.get("https://lambdatest.com/selenium-playground/")

driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()

assert "simple-form-demo" in driver.current_url

driver.execute_script('window.open("https://www.google.com");')

print(driver.window_handles)

driver.switch_to.window(driver.window_handles[0])
driver.save_screenshot("screenshots/playground_screenshot.png")

print(driver.title)

driver.back()

print("Current Window Size:")
print(driver.get_window_size())

driver.set_window_size(1280, 800)

print("Updated Window Size:")
print(driver.get_window_size())

driver.quit()
