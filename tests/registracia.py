import fake as fake
from faker import Faker
from selenium.webdriver.common.by import By

from WebDriverManager.WebDriverManager import WebDriverManager
from setup.basetest import BaseTest

fake = Faker()
email = fake.email()
password = fake.password()


class RegistrationForm(BaseTest):

    def test_registration(self):
        self.set_up()
        create_a_new_accaunt = WebDriverManager.driver.find_element(By.XPATH, "//a[normalize-space()='Create a new account']")
        create_a_new_accaunt.click()
        first_name = WebDriverManager.driver.find_element(By.ID, "user[first_name]")
        first_name.send_keys(fake.user_name())
        last_name = WebDriverManager.driver.find_element(By.ID, "user[last_name]")
        last_name.send_keys(fake.last_name())
        email1 = WebDriverManager.driver.find_element(By.ID, "user[email]")
        email1.send_keys(email)
        password1 = WebDriverManager.driver.find_element(By.ID, "user[password]")
        password1.send_keys(password)
        check_box = WebDriverManager.driver.find_element(By.ID, "user[terms]")
        check_box.click()
        sign_up = WebDriverManager.driver.find_element(By.XPATH, "//button[@type='submit']")
        sign_up.click()

    def test_homepage(self):
        self.set_up()
        product_element = WebDriverManager.driver.find_element(By.XPATH, "//h2[@class='collections__heading']")
        assert product_element.is_displayed()

    def test_log_out(self):
        self.set_up()
        profile_drop_down = WebDriverManager.driver.find_element(By.XPATH, "//i[@class='fa fa-caret-down']")
        profile_drop_down.click()
        sing_out = WebDriverManager.driver.find_element(By.XPATH, "//a[normalize-space()='Sign Out']")
        sing_out.click()

    def test_log_in(self):
        self.set_up()
        sing_in = WebDriverManager.driver.find_element(By.XPATH, "//a[normalize-space()='Sign In']")
        sing_in.click()
        email2 = WebDriverManager.driver.find_element(By.ID, "user[email]")
        email2.send_keys(email)
        password2 = WebDriverManager.driver.find_element(By.ID, "user[password]")
        password2.send_keys(password)
        sing_in_button = WebDriverManager.driver.find_element(By.XPATH, "//button[@type='submit']")
        sing_in_button.click()

    def test_homepage1(self):
        self.set_up()
        product_element1 = WebDriverManager.driver.find_element(By.XPATH, "//h2[@class='collections__heading']")
        assert product_element1.is_displayed()


ragaca1 = RegistrationForm()
ragaca1.test_registration()
ragaca1.test_homepage()
ragaca1.test_log_out()
ragaca1.test_log_in()
ragaca1.test_homepage1()