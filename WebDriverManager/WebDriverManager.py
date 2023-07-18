
from MetaClasses.SignleTonMetaClass import Singleton
from WebDriverManager.browserFactory import BrowserFactory


class WebDriverManager(metaclass=Singleton):
    driver = BrowserFactory.get_driver()

