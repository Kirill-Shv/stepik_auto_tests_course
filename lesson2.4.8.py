from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"100")
    )
    button2 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button2.click()
    x = browser.find_element(By.ID, 'input_value')
    x_value=x.text
    y=math.log(math.fabs(12*math.sin(int(x_value))))
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    button3 = browser.find_element(By.ID, "solve")
    button3.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()