from selenium.webdriver.remote.webdriver import WebDriver
from tests.utils.locators import Locators
from tests.testbase import *


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.web = driver
        self.get = Locators(driver)
        self.usernameInput = lambda: self.get.byDataTest("username")
        self.passwordInput = lambda: self.get.byDataTest("password")
        self.submitButton = lambda: self.get.byDataTest("login-button")
        self.look_out_user_message_error_locator = (
            By.CLASS_NAME,
            "error-message-container",
        )
        #
        # ERROR MESSAGES
        #
        self.user_look_out_error_message = (
            "Epic sadface: Sorry, this user has been locked out."
        )

    def enterUsername(self, inputValue: str):
        return self.usernameInput().send_keys(inputValue)

    def enterPassword(self, inputValue: str):
        return self.passwordInput().send_keys(inputValue)

    def clickSubmit(self):
        return self.submitButton().click()

    def submitLoginForm(self, username, password):
        self.enterUsername(username)
        self.enterPassword(password)
        self.clickSubmit()

    def error_message_look_out(self):
        return self.web.find_element(*self.look_out_user_message_error_locator).text
