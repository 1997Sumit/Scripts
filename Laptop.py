import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.devtools.v130.fed_cm import click_dialog_button

# Initialize the WebDriver
driver = webdriver.Chrome()

# Navigate to the login page
driver.get("https://stage.cicsacv.com/")
time.sleep(1)
driver.maximize_window()
# Wait for the page to load
time.sleep(2)
driver.find_element(By.XPATH, "//span[text()='Iniciar sesión']").click()
time.sleep(1)

# Locate the username, password fields and login button
driver.find_element(By.ID, "customer-email").send_keys("fisvcon1@yopmail.com")  # Replace with the actual ID of the username field
driver.find_element(By.ID, "pass").send_keys("sumit@123")  # Replace with the actual ID of the password field
time.sleep(1)
driver.find_element(By.ID,"send2").click()
#driver.find_element(By.CSS_SELECTOR,"span[data-bind="i18n:'Sign In'"]").click_dialog_button()

# Wait for some time to observe the result
time.sleep(5)
driver.refresh()

# Close the browser
driver.quit()
print("Hello")
