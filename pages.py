from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class WikipediaPage:
    def __init__(self):
        options = Options()
        options.add_argument("--incognito")
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
        self.wait = WebDriverWait(self.driver, 20)

    def open(self):
        self.driver.get("https://wikipedia.org")

    def search(self, query):
        field = self.wait.until(
            EC.element_to_be_clickable((By.NAME, "search"))
        )
        field.click()
        field.send_keys(query)
        field.submit()
        self.wait.until(
	    EC.title_contains(query)
	)

    def get_title(self):
        return self.driver.title

    def close(self):
        self.driver.close()