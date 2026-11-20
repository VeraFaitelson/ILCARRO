"""Page Object for the Registration page"""

from selenium.webdriver.common.by import By

from models.user import User
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    """Encapsulates locators and actions for creating a new user account"""

    # Locators specific to the Registration page
    LOGIN_LINK = (By.XPATH, "//a[text()='Log in']")
    REGISTRATION_LINK = (By.XPATH, "//a[text()='Click here']")
    FIRST_NAME_INPUT = (By.NAME, "firstName")
    LAST_NAME_INPUT = (By.NAME, "lastName")
    EMAIL_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    TERMS_OF_USE_CHECKBOX = (By.NAME, "termsOfUse")
    BUTTON_REGISTRATION = (By.CSS_SELECTOR, "button.btn.btn--primary")

    def open_registration_page(self):
        """Navigates to the Registration form via the Login page"""
        self.click(self.LOGIN_LINK)
        self.click(self.REGISTRATION_LINK)
        self.find(self.FIRST_NAME_INPUT)

    def fill_first_name_field(self, first_name: str):
        """Enters first name into the First Name field"""
        self.fill(self.FIRST_NAME_INPUT, first_name)

    def fill_last_name_field(self, last_name: str):
        """Enters last name into the Last Name field"""
        self.fill(self.LAST_NAME_INPUT, last_name)

    def fill_email_field(self, email: str):
        """Enters email into the Email field"""
        self.fill(self.EMAIL_INPUT, email)

    def fill_password_field(self, password: str):
        """Enters password into the Password field"""
        self.fill(self.PASSWORD_INPUT, password)

    def fill_registration_form(self, user: User):
        """Fills all text fields of the registration form using a User model"""
        self.fill_first_name_field(user.first_name)
        self.fill_last_name_field(user.last_name)
        self.fill_email_field(user.email)
        self.fill_password_field(user.password)

    def click_on_terms_of_use(self):
        """Checks the 'Terms of Use' agreement checkbox"""
        self.click(self.TERMS_OF_USE_CHECKBOX)

    def click_on_registration_button(self):
        """Clicks the 'Y'alla!' registration submit button"""
        self.click(self.BUTTON_REGISTRATION)

    def is_submit_button_disabled(self) -> bool:
        """Checks if the Registration submit button is currently disabled"""
        return self.is_button_disabled(self.BUTTON_REGISTRATION)