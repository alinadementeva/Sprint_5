from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestsRegistrationPage:

    def test_registration_success(self, chrome_driver, email):
        chrome_driver.get('https://stellarburgers.nomoreparties.site/register')
        chrome_driver.find_element(By.XPATH, ".//label[text()='Имя']/following-sibling::input").send_keys("Alina")
        chrome_driver.find_element(By.XPATH, ".//label[text()='Email']/following-sibling::input").send_keys(email)
        chrome_driver.find_element(By.XPATH, ".//label[text()='Пароль']/following-sibling::input").send_keys("s1D#fO23R")
        chrome_driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()
        WebDriverWait(chrome_driver, 10).until(
            expected_conditions.url_changes('https://stellarburgers.nomoreparties.site/register'))
        assert chrome_driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        chrome_driver.quit()

    def test_registration_incorrect_password(self, chrome_driver, email):
        chrome_driver.get('https://stellarburgers.nomoreparties.site/register')
        chrome_driver.find_element(By.XPATH, ".//label[text()='Имя']/following-sibling::input").send_keys("Alina")
        chrome_driver.find_element(By.XPATH, ".//label[text()='Email']/following-sibling::input").send_keys(email)
        chrome_driver.find_element(By.XPATH, ".//label[text()='Пароль']/following-sibling::input").send_keys("Sw1")
        chrome_driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()
        WebDriverWait(chrome_driver, 10).until(
            expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/register'))
        assert chrome_driver.find_element(By.XPATH, ".//p[text()='Некорректный пароль']")
        chrome_driver.quit()