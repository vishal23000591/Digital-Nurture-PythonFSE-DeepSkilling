from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)
driver.maximize_window()
driver.get("https://www.lambdatest.com/selenium-playground")


driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()

message_box = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Please enter your Message']")

message_box.send_keys("Hello Vishal")

driver.quit()