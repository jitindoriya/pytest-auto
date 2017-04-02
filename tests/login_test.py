import unittest
import pytest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self,oneTimeSetUp):
        self.login_page = LoginPage(self.driver)


    # dummy login test on site
    def test_valid_login(self):
        self.login_page.login("test@email.com", "abcabc")
