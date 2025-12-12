from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_login():

    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    try:
        # путь к файлу в GitHub Actions
        driver.get("file:///home/runner/work/auto-tests-lab/auto-tests-lab/lab3.html")

        username_input = driver.find_element(By.ID, "username")
        password_input = driver.find_element(By.ID, "password")

        username_input.send_keys("user")
        password_input.send_keys("pass")

        driver.find_element(By.ID, "login-btn").send_keys(Keys.RETURN)

        time.sleep(2)

        logout_element = driver.find_element(By.XPATH, "//button[text()='Logout']")
        assert logout_element.is_displayed()

    finally:
        driver.quit()





