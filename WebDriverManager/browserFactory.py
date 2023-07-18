from selenium import webdriver


class BrowserFactory:
    @staticmethod
    def get_driver(browser="chrome"):
        if browser.lower() == "chrome":
            return webdriver.Chrome()
        elif browser == "Safari":
            return webdriver.Safari()