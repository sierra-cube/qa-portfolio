from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Чистый Chrome без кэша
options = Options()
options.add_argument("--incognito")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.get("https://wikipedia.org")

wait = WebDriverWait(driver, 10)
search = wait.until(EC.element_to_be_clickable((By.NAME, "search")))

search.click()
search.send_keys("Python")
search.submit()

print(driver.title)

driver.close()