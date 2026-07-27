from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://www.lambdatest.com/selenium-playground")

wait = WebDriverWait(driver, 10)

checkbox_link = wait.until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Checkbox Demo"))
)

checkbox_link.click()

option1 = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//label[text()='Option 1']")
    )
) 

print(option1.text)

input("Press Enter to close...")
driver.quit()
