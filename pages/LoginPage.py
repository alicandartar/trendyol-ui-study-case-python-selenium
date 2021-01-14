from selenium.webdriver import ActionChains

from utils.locators import *
from utils.userCredentials import UserCredentials
from pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.emailTextBox = Locators.emailTextBox
        self.passTextBox = Locators.passwordTextBox
        self.loginButton = Locators.loginButton
        self.testMail = UserCredentials.test_username
        self.testPassword = UserCredentials.test_password

    def user_login(self):
        driver = self.driver
        driver.find_element(*self.emailTextBox).send_keys(*self.testMail)
        driver.find_element(*self.passTextBox).send_keys(*self.testPassword)
        driver.find_element(*self.loginButton).click()
