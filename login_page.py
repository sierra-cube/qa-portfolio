from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class LoginPage:

    def __init__(self):
        options = Options()
        options.add_argument("--incognito")
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
        self.wait = WebDriverWait(self.driver, 10)

    def open(self):
        self.driver.get(
            "https://the-internet.herokuapp.com/login"
        )

    def login(self, username, password):
        self.wait.until(
            EC.presence_of_element_located((By.ID, "username"))
        ).send_keys(username)
        self.driver.find_element(
            By.ID, "password"
        ).send_keys(password)
        self.driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
        ).click()

    def get_message(self):
        message = self.wait.until(
            EC.presence_of_element_located((By.ID, "flash"))
        )
        return message.text

    def close(self):
        self.driver.close()