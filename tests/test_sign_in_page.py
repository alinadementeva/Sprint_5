import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators
import data


class TestsSignInPage:

    def test_signin_login_to_account_button(self, chrome_driver):
        chrome_driver.get(data.url)
        chrome_driver.find_element(By.XPATH, locators.sign_in_account_button).click()
        chrome_driver.find_element(By.XPATH, locators.email_input).send_keys(data.user_email)
        chrome_driver.find_element(By.XPATH, locators.password_input).send_keys(data.user_password)
        chrome_driver.find_element(By.XPATH, locators.login_button).click()
        assert WebDriverWait(chrome_driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, locators.make_an_order_button)))

    def test_signin_personal_account_button(self, chrome_driver):
        chrome_driver.get(data.url)
        chrome_driver.find_element(By.XPATH, locators.personal_account_button).click()
        chrome_driver.find_element(By.XPATH, locators.email_input).send_keys(data.user_email)
        chrome_driver.find_element(By.XPATH, locators.password_input).send_keys(data.user_password)
        chrome_driver.find_element(By.XPATH, locators.login_button).click()
        assert WebDriverWait(chrome_driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, locators.make_an_order_button)))

    def test_signin_registration_form(self, chrome_driver):
        chrome_driver.get(data.url + 'register')
        chrome_driver.find_element(By.XPATH, locators.login_link).click()
        chrome_driver.find_element(By.XPATH, locators.email_input).send_keys(data.user_email)
        chrome_driver.find_element(By.XPATH, locators.password_input).send_keys(data.user_password)
        chrome_driver.find_element(By.XPATH, locators.login_button).click()
        assert WebDriverWait(chrome_driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, locators.make_an_order_button)))

    def test_signin_password_recovery_form(self, chrome_driver):
        chrome_driver.get(data.url + 'forgot-password')
        chrome_driver.find_element(By.XPATH, locators.login_link).click()
        chrome_driver.find_element(By.XPATH, locators.email_input).send_keys(data.user_email)
        chrome_driver.find_element(By.XPATH, locators.password_input).send_keys(data.user_password)
        chrome_driver.find_element(By.XPATH, locators.login_button).click()
        assert WebDriverWait(chrome_driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, locators.make_an_order_button)))