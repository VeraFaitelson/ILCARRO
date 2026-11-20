"""Page Object for the Login page"""

from selenium.webdriver.common.by import By

from models.user import User
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Encapsulates locators and actions for user authentication"""

    # Locators specific to the Login page
    LOGIN_LINK = (By.XPATH, "//a[text()='Log in']")
    EMAIL_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    BUTTON_LOGIN = (By.CSS_SELECTOR, "button.btn.btn--primary")

    def open_login_page(self):
        """Navigates to the Login page and waits for the form to load"""
        self.click(self.LOGIN_LINK)
        self.find(self.EMAIL_INPUT)

    def fill_email_field(self, email: str):
        """Enters email into the username/email field"""
        self.fill(self.EMAIL_INPUT, email)

    def fill_password_field(self, password: str):
        """Enters password into the password field"""
        self.fill(self.PASSWORD_INPUT, password)

    def fill_login_form(self, user: User):
        """Fills both email and password fields using a User model"""
        self.fill_email_field(user.email)
        self.fill_password_field(user.password)

    def click_on_login_button(self):
        """Clicks the 'Y'alla!' submit button"""
        self.click(self.BUTTON_LOGIN)

    def is_submit_button_disabled(self) -> bool:
        """Checks if the Login submit button is currently disabled"""
        return self.is_button_disabled(self.BUTTON_LOGIN)
