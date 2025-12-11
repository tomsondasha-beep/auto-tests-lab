from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Настройка браузера
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Открываем страницу логина 
    driver.get("http://localhost:5500/lab3.html")  

    # Находим поля ввода логина и пароля
    username_input = driver.find_element(By.ID, "username")  
    password_input = driver.find_element(By.ID, "password")

    # Вводим валидные credentials
    username_input.send_keys("user")  
    password_input.send_keys("pass")

    # Отправляем форму 
    driver.find_element(By.ID, "login-btn").send_keys(Keys.RETURN)

    # Ждём перехода / загрузки страницы 
    time.sleep(4)

    # Проверяем успешный вход по появлению элемента Logout
    # logout_element = WebDriverWait(driver, 5).until(
    #     EC.visibility_of_element_located((By.ID, "logout"))
    # )
    logout_element = driver.find_element(By.XPATH, "//button[text()='Logout']")
    if logout_element.is_displayed():
        print("Тест успешен: элемент 'Logout' найден.")
    else:
        print("Тест провален: элемент 'Logout' не найден.")

finally:
    # Закрываем браузер
    driver.quit()
