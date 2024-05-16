import pytest
import random
import string
from selenium import webdriver


@pytest.fixture
def chrome_driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    return chrome_driver


@pytest.fixture
def email():
    email = 'alinadementyeva8' + str(random.randint(100,999)) + '@yandex.ru'
    return email
