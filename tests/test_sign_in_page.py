import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestsSignInPage:

    def test_signin_login_to_account_button(self, chrome_driver):
        chrome_driver.get('https://stellarburgers.nomoreparties.site')
        chrome_driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
        chrome_driver.find_element(By.XPATH, ".//label[text()='Email']/following-sibling::input").send_keys('adementyeva8123@yandex.ru')
        chrome_driver.find_element(By.XPATH, ".//label[text()='Пароль']/following-sibling::input").send_keys("s1D#fO23R")
        chrome_driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
        assert WebDriverWait(chrome_driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
        chrome_driver.quit()

    def test_signin_personal_account_button(self, chrome_driver):
        chrome_driver.get('https://stellarburgers.nomoreparties.site')
        chrome_driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        chrome_driver.find_element(By.XPATH, ".//label[text()='Email']/following-sibling::input").send_keys('adementyeva8123@yandex.ru')
        chrome_driver.find_element(By.XPATH, ".//label[text()='Пароль']/following-sibling::input").send_keys("s1D#fO23R")
        chrome_driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
        assert WebDriverWait(chrome_driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
        chrome_driver.quit()

    def test_signin_registration_form(self, chrome_driver):
        chrome_driver.get('https://stellarburgers.nomoreparties.site/register')
        chrome_driver.find_element(By.XPATH, ".//a[text()='Войти']").click()
        chrome_driver.find_element(By.XPATH, ".//label[text()='Email']/following-sibling::input").send_keys('adementyeva8123@yandex.ru')
        chrome_driver.find_element(By.XPATH, ".//label[text()='Пароль']/following-sibling::input").send_keys("s1D#fO23R")
        chrome_driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
        assert WebDriverWait(chrome_driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
        chrome_driver.quit()

    def test_signin_password_recovery_form(self, chrome_driver):
        chrome_driver.get('https://stellarburgers.nomoreparties.site/forgot-password')
        chrome_driver.find_element(By.XPATH, ".//a[text()='Войти']").click()
        chrome_driver.find_element(By.XPATH, ".//label[text()='Email']/following-sibling::input").send_keys('adementyeva8123@yandex.ru')
        chrome_driver.find_element(By.XPATH, ".//label[text()='Пароль']/following-sibling::input").send_keys("s1D#fO23R")
        chrome_driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
        assert WebDriverWait(chrome_driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
        chrome_driver.quit()