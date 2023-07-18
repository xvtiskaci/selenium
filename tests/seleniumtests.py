from selenium.webdriver.common.by import By

from WebDriverManager.WebDriverManager import WebDriverManager
from setup.basetest import BaseTest


class SeleniumTests(BaseTest):

    def test_scrolldown_menu(self):
        self.set_up()
        scrolldown_element_list = WebDriverManager\
            .driver.find_elements(By.XPATH, "//li[contains(@class, 'with-child')and not(contains(@class, 'active-path'))]")
        assert scrolldown_element_list[0].text == "Overview"

