import time

from selenium import webdriver

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the web page
driver.get("https://stage.cicsacv.com/")
driver.maximize_window()

# Take a screenshot
driver.save_screenshot("screenshot.png")

time.sleep(2)

# Close the browser
driver.quit()

