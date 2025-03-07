import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Testp:
    def __init__(self):
        # Initialize the WebDriver
        self.driver = webdriver.Chrome()

    def open_links_in_new_tabs(self, url):
        # Open the webpage
        self.driver.get(url)
        time.sleep(1)  # Allow time for the page to load
        self.driver.maximize_window()

        # Find all links on the page
        links = self.driver.find_elements(By.TAG_NAME, "a")

        # Open each link in a new tab
        for link in links:
            link_url = link.get_attribute("href")
            if link_url:
                self.driver.execute_script(f"window.open('{link_url}', '_blank');")
                print(f"Opening link: {link_url}")
                time.sleep(2)  # Pause before opening the next link

    def close_driver(self):
        # Optionally close the browser after task completion
        self.driver.quit()


if __name__ == "__main__":
    test = Testp()
    test.open_links_in_new_tabs("https://dev.pfeifer.com.mx/")
    time.sleep(50)  # Let all tabs open for 50 seconds before closing
    test.close_driver()
time.sleep(50)
