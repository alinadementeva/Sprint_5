from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators
import data


class TestsPersonalAccountPage:

    def test_personal_account_info(self, chrome_driver):
        chrome_driver.get(data.url)
        chrome_driver.find_element(By.XPATH, locators.sign_in_account_button).click()
        chrome_driver.find_element(By.XPATH, locators.email_input).send_keys(data.user_email)
        chrome_driver.find_element(By.XPATH, locators.password_input).send_keys(data.user_password)
        chrome_driver.find_element(By.XPATH, locators.login_button).click()
        chrome_driver.find_element(By.XPATH, locators.personal_account_button).click()
        assert WebDriverWait(chrome_driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, locators.name_info)))
        assert WebDriverWait(chrome_driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, locators.email_info)))
        assert WebDriverWait(chrome_driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, locators.password_info)))

    def test_personal_account_go_to_constructor_page(self, chrome_driver):
        chrome_driver.get(data.url)
        chrome_driver.find_element(By.XPATH, locators.sign_in_account_button).click()
        chrome_driver.find_element(By.XPATH, locators.email_input).send_keys(data.user_email)
        chrome_driver.find_element(By.XPATH, locators.password_input).send_keys(data.user_password)
        chrome_driver.find_element(By.XPATH, locators.login_button).click()
        chrome_driver.find_element(By.XPATH, locators.personal_account_button).click()
        chrome_driver.find_element(By.XPATH, locators.constructor_button).click()
        assert WebDriverWait(chrome_driver, 10).until(
            expected_conditions.url_to_be(data.url))

    def test_personal_account_logout(self, chrome_driver):
        chrome_driver.get(data.url)
        chrome_driver.find_element(By.XPATH, locators.sign_in_account_button).click()
        chrome_driver.find_element(By.XPATH, locators.email_input).send_keys(data.user_email)
        chrome_driver.find_element(By.XPATH, locators.password_input).send_keys(data.user_password)
        chrome_driver.find_element(By.XPATH, locators.login_button).click()
        chrome_driver.find_element(By.XPATH, locators.personal_account_button).click()
        WebDriverWait(chrome_driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, locators.logout_button)))
        chrome_driver.find_element(By.XPATH, locators.logout_button).click()
        assert WebDriverWait(chrome_driver, 10).until(
            expected_conditions.url_to_be(data.url + 'login'))
