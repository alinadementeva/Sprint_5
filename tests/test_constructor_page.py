from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators
import data


class TestsConstructorPage:

    def test_constructor_buns_tab(self, chrome_driver):
        chrome_driver.get(data.url)
        WebDriverWait(chrome_driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.fillings_tab)))
        chrome_driver.find_element(By.XPATH, locators.fillings_tab).click()
        WebDriverWait(chrome_driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.buns_tab)))
        chrome_driver.find_element(By.XPATH,  locators.buns_tab).click()
        assert WebDriverWait(chrome_driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, locators.buns_header)))

    def test_constructor_sauces_tab(self, chrome_driver):
        chrome_driver.get(data.url)
        WebDriverWait(chrome_driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.sauces_tab)))
        chrome_driver.find_element(By.XPATH, locators.sauces_tab).click()
        assert WebDriverWait(chrome_driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, locators.sauces_header)))

    def test_constructor_filling_tab(self, chrome_driver):
        chrome_driver.get(data.url)
        WebDriverWait(chrome_driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.fillings_tab)))
        chrome_driver.find_element(By.XPATH, locators.fillings_tab).click()
        assert WebDriverWait(chrome_driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, locators.fillings_header)))