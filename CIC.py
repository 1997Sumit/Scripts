import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Testp:
    def __init__(self):
        # Step 1: Initialize the WebDriver and open the website
        self.driver = webdriver.Chrome()
        self.driver.get("https://stage.cicsacv.com/")

        # Step 2: Maximize the browser window
        self.driver.maximize_window()

        # Step 3: Wait for the modal to appear and close it (if present)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "mc-closeModal"))
            ).click()
        except Exception as e:
            print("Modal not found or error in closing it:", e)

        # Step 4: Get all the links on the page
        self.links = self.driver.find_elements(By.TAG_NAME, "a")

        # Step 5: Extract URLs from the links
        self.urls = [link.get_attribute("href") for link in self.links if link.get_attribute("href")]

        # Step 6: Open each URL in a new tab
        for url in self.urls:
            # Open the URL in a new tab
            self.driver.execute_script(f"window.open('{url}', '_blank')")
            time.sleep(1)  # Optional: wait between opening tabs

    def close(self):
        # Step 7: Wait for 5 seconds to observe the opened tabs
        time.sleep(5)

        # Step 8: Close the browser
        self.driver.quit()


if __name__ == "__main__":
    # Step 9: Execute the test
    test = Testp()
    test.close()
