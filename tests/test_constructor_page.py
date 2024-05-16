from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestsConstructorPage:

    def test_constructor_buns_tab(self, chrome_driver):
        chrome_driver.get('https://stellarburgers.nomoreparties.site')
        WebDriverWait(chrome_driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//span[contains(text(),'Начинки')]")))
        chrome_driver.find_element(By.XPATH, ".//span[text()='Начинки']").click()
        WebDriverWait(chrome_driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//span[contains(text(),'Булки')]")))
        chrome_driver.find_element(By.XPATH, ".//span[text()='Булки']").click()
        assert WebDriverWait(chrome_driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "html/body/div/div/main/section["
                                                                       "@class='BurgerIngredients_ingredients__1N8v2"
                                                                       "']/div/div/span[text()='Булки']")))
        chrome_driver.quit()


    def test_constructor_sauces_tab(self, chrome_driver):
        chrome_driver.get('https://stellarburgers.nomoreparties.site')
        WebDriverWait(chrome_driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//span[contains(text(),'Соусы')]")))
        chrome_driver.find_element(By.XPATH, ".//span[text()='Соусы']").click()
        assert WebDriverWait(chrome_driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, ".//h2[text()='Соусы']")))
        chrome_driver.quit()

    def test_constructor_filling_tab(self, chrome_driver):
        chrome_driver.get('https://stellarburgers.nomoreparties.site')
        WebDriverWait(chrome_driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//span[contains(text(),'Начинки')]")))
        chrome_driver.find_element(By.XPATH, ".//span[text()='Начинки']").click()
        assert WebDriverWait(chrome_driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, ".//h2[text()='Начинки']")))
        chrome_driver.quit()