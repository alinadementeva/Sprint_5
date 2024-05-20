from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helpers import email
import locators
import data


class TestsRegistrationPage:

    def test_registration_success(self, chrome_driver):
        chrome_driver.get(data.url + 'register')
        chrome_driver.find_element(By.XPATH, locators.name_input).send_keys(data.user_name)
        chrome_driver.find_element(By.XPATH, locators.email_input).send_keys(email())
        chrome_driver.find_element(By.XPATH, locators.password_input).send_keys(data.user_password)
        chrome_driver.find_element(By.XPATH, locators.registration_button).click()
        WebDriverWait(chrome_driver, 10).until(
            expected_conditions.url_changes(data.url + 'register'))
        assert chrome_driver.current_url == data.url + 'login'

    def test_registration_incorrect_password(self, chrome_driver):
        chrome_driver.get(data.url + 'register')
        chrome_driver.find_element(By.XPATH, locators.name_input).send_keys(data.user_name)
        chrome_driver.find_element(By.XPATH, locators.email_input).send_keys(email())
        chrome_driver.find_element(By.XPATH, locators.password_input).send_keys(data.user_incorrect_password)
        chrome_driver.find_element(By.XPATH, locators.registration_button).click()
        WebDriverWait(chrome_driver, 10).until(
            expected_conditions.url_to_be(data.url + 'register'))
        assert chrome_driver.find_element(By.XPATH, locators.pass_validation)
