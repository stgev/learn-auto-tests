from selenium import webdriver
from selenium.webdriver.common.by import By
from math import sin, log as ln

URL = "http://suninjuly.github.io/alert_accept.html"


def solve_captcha(x: int) -> float:
    return ln(abs(12 * sin(x)))


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get(URL)

    driver.find_element(By.CLASS_NAME, "btn").click()
    driver.switch_to.alert.accept()

    x = int(driver.find_element(By.ID, "input_value").text)
    answer = solve_captcha(x)
    driver.find_element(By.ID, "answer").send_keys(str(answer))
    driver.find_element(By.CLASS_NAME, "btn").click()

    print(driver.switch_to.alert.text)
