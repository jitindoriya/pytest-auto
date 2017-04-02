from selenium.webdriver.common.by import By
from base.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"


    def clickLoginLink(self):
        self.waitForElementAndClick(self._login_link, locatorType="link")

    def enterEmail(self, email):
        self.waitForElementAndType(text=email, locator=self._email_field)

    def enterPassword(self, password):
        self.waitForElementAndType(text=password, locator=self._password_field)

    def clickLoginButton(self):
        self.waitForElementAndClick(self._login_button, locatorType="name")

    def login(self, email, password):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()