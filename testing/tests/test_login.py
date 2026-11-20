"""Tests for user login functionality (positive and negative scenarios)"""

from conftest import DEFAULT_USER
from pages.login_page import LoginPage
from utils.data_generator import generate_user

# Test data constants for negative scenarios
INVALID_EMAIL = "testQAgmailcom"
INVALID_PASSWORD = "test"


def test_valid_login_success(driver):
    """Verify successful login with valid credentials"""
    login_page = LoginPage(driver)

    login_page.open_login_page()
    login_page.fill_login_form(DEFAULT_USER)
    login_page.click_on_login_button()

    assert login_page.is_sign_out_displayed()


def test_login_with_invalid_email_and_valid_password(driver):
    """Verify validation error and disabled submit button when email format is invalid"""
    login_page = LoginPage(driver)
    user = generate_user()
    user.email = INVALID_EMAIL

    login_page.open_login_page()
    login_page.fill_login_form(user)

    assert login_page.is_submit_button_disabled()
    assert login_page.get_field_error_text() == "Wrong email format"
    assert not login_page.is_sign_out_displayed()


def test_login_with_valid_email_and_invalid_password(driver):
    """Verify error modal appears when password is incorrect"""
    login_page = LoginPage(driver)
    user = generate_user()
    user.email = DEFAULT_USER.email
    user.password = INVALID_PASSWORD

    login_page.open_login_page()
    login_page.fill_login_form(user)
    login_page.click_on_login_button()

    assert login_page.get_modal_title() == "Login failed"
    assert "incorrect" in login_page.get_modal_text().lower()
    login_page.close_modal()
    assert not login_page.is_sign_out_displayed()


def test_login_with_unregistered_email(driver):
    """Verify error modal appears when attempting to log in with a non-existent email"""
    login_page = LoginPage(driver)
    user = generate_user()  # Contains a newly generated, unregistered email

    login_page.open_login_page()
    login_page.fill_login_form(user)
    login_page.click_on_login_button()

    assert login_page.get_modal_title() == "Login failed"
    assert "Login or Password incorrect" in login_page.get_modal_text()
    login_page.close_modal()
    assert not login_page.is_sign_out_displayed()
