import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Define the path to the ChromeDriver executable
#SERVICE_PATH = "D://Selenium//Webdriver//chromedriver-win64//chromedriver-win64//chromedriver.exe"

# Initialize the Chrome WebDriver with the service object
#service_obj = Service(executable_path=SERVICE_PATH)
driver = webdriver.Chrome()

# Open the target website
driver.get("https://stage.cicsacv.com/")

# Maximize the browser window
driver.maximize_window()

# Wait for the page to load
time.sleep(2)

# Click on the "Iniciar sesión" button
driver.find_element(By.XPATH, "//span[text()='Iniciar sesión']").click()

# Click on the "Registrate" link to go to the registration page
time.sleep(1)
driver.find_element(By.XPATH, "//span[normalize-space()='Registrate']").click()

# Wait for the page to load
time.sleep(2)

# Fill out the registration form
driver.find_element(By.ID, "firstname").send_keys("Sumit")
driver.find_element(By.ID, "lastname").send_keys("Sharma")
driver.find_element(By.ID, "email_address").send_keys("fishcon1@yopmail.com")
driver.find_element(By.ID, "password").send_keys("sumit@123")
driver.find_element(By.ID, "password-confirmation").send_keys("sumit@123")
driver.find_element(By.ID, "taxvat").send_keys("12345")
time.sleep(20)
#driver.find_element(By.ID, "recaptcha-anchor").click()


# Submit the registration form
driver.find_element(By.XPATH, "//button[@title='Crear una Cuenta']").click()

# Wait for the account to be created and the page to update
time.sleep(2)

# Verify the account by checking the user's name (Sumit Sharma)
#driver.find_element(By.XPATH, "//b[normalize-space()='Sumit Sharma']").click()

# Wait for the profile menu to appear
time.sleep(2)

# Log out from the account
driver.find_element(By.XPATH, "//ul[@class='list']//a[normalize-space()='Cerrar sesión']").click()

# Wait for the logout to complete
time.sleep(3)

# Close the browser
driver.quit()

