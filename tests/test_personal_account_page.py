from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestsPersonalAccountPage:

    def test_personal_account_info(self, chrome_driver):
        chrome_driver.get('https://stellarburgers.nomoreparties.site')
        chrome_driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
        chrome_driver.find_element(By.XPATH, ".//label[text()='Email']/following-sibling::input").send_keys('adementyeva8123@yandex.ru')
        chrome_driver.find_element(By.XPATH, ".//label[text()='Пароль']/following-sibling::input").send_keys("s1D#fO23R")
        chrome_driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
        chrome_driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        assert WebDriverWait(chrome_driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, ".//input[@value='Alina']")))
        assert WebDriverWait(chrome_driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, ".//input[@value='adementyeva8123@yandex.ru']")))
        assert WebDriverWait(chrome_driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, ".//input[@value='*****']")))
        chrome_driver.quit()

    def test_personal_account_go_to_constructor_page(self, chrome_driver):
        chrome_driver.get('https://stellarburgers.nomoreparties.site')
        chrome_driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
        chrome_driver.find_element(By.XPATH, ".//label[text()='Email']/following-sibling::input").send_keys('adementyeva8123@yandex.ru')
        chrome_driver.find_element(By.XPATH, ".//label[text()='Пароль']/following-sibling::input").send_keys("s1D#fO23R")
        chrome_driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
        chrome_driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        chrome_driver.find_element(By.XPATH, ".//p[text()='Конструктор']").click()
        WebDriverWait(chrome_driver, 10).until(
            expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))
        chrome_driver.quit()

    def test_personal_account_logout(self, chrome_driver):
        chrome_driver.get('https://stellarburgers.nomoreparties.site')
        chrome_driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
        chrome_driver.find_element(By.XPATH, ".//label[text()='Email']/following-sibling::input").send_keys('adementyeva8123@yandex.ru')
        chrome_driver.find_element(By.XPATH, ".//label[text()='Пароль']/following-sibling::input").send_keys("s1D#fO23R")
        chrome_driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
        chrome_driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        chrome_driver.find_element(By.XPATH, ".//button[contains(.,'Выход')]").click()
        assert WebDriverWait(chrome_driver, 10).until(
            expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/login'))
        chrome_driver.quit()