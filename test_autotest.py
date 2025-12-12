from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_login():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        driver.get("file:///home/runner/work/auto-tests-lab/auto-tests-lab/lab3.html")

        username_input = driver.find_element(By.ID, "username")
        password_input = driver.find_element(By.ID, "password")

        username_input.send_keys("user")
        password_input.send_keys("pass")

        driver.find_element(By.ID, "login-btn").send_keys(Keys.RETURN)

        time.sleep(4)

        logout_element = driver.find_element(By.XPATH, "//button[text()='Logout']")
        assert logout_element.is_displayed(), "Logout not found"

    finally:
        driver.quit()



