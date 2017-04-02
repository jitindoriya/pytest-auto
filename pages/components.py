from selenium.webdriver.common.by import By


class LoginPage(object):

    LOGIN_LINK = (By.LINK_TEXT,'Login')

    EMAIL_FIELD = (By.ID,'user_email')

    PASSWORD_FIELD = (By.ID, 'user_password')

    LOGIN_BUTTON = (By.NAME, 'commit')
