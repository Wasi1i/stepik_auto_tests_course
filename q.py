from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
import math
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной 
    
    button = browser.find_element(By.CSS_SELECTOR, "#book")
    
    button1 = WebDriverWait(browser, 12).until(
        ES.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), '$100'))

    button.click()
#scroll
    browser.execute_script("window.scrollBy(0, 100);")

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    input3 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input3.send_keys(y)
    
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "#solve")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()