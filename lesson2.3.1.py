from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    browser.switch_to.alert.accept()
    x = browser.find_element(By.ID, 'input_value')
    x_value=x.text
    y=math.log(math.fabs(12*math.sin(int(x_value))))
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    button2 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()