import json
from faker import Faker

from WebDriverManager.WebDriverManager import WebDriverManager


class BaseTest:
    @staticmethod
    def set_up():
        f = open('../config/config.json')
        data = json.load(f)
        f.close()
        driver = WebDriverManager.driver
        driver.get(data["url"])
        driver.implicitly_wait(10)
        driver.maximize_window()

