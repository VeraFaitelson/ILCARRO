"""Tests for user registration functionality (positive and negative scenarios)"""

from conftest import DEFAULT_USER
from pages.registration_page import RegistrationPage
from utils.data_generator import generate_user

# Test data constants for negative scenarios
INVALID_EMAIL = "testQAgmailcom"
INVALID_PASSWORD = "test"


def test_valid_registration_success(driver):
    """Verify successful registration with valid user data"""
    registration_page = RegistrationPage(driver)
    user = generate_user()

    registration_page.open_registration_page()
    registration_page.fill_registration_form(user)
    registration_page.click_on_terms_of_use()
    registration_page.click_on_registration_button()

    assert registration_page.get_modal_title() == "Registered"
    assert registration_page.get_modal_text() == "You are logged in success"
    registration_page.close_modal()
    assert registration_page.is_sign_out_displayed()


def test_invalid_registration_with_empty_name(driver):
    """Verify validation error when 'First Name' field is left empty"""
    registration_page = RegistrationPage(driver)
    user = generate_user()
    user.first_name = ""

    registration_page.open_registration_page()
    registration_page.fill_registration_form(user)
    registration_page.click_on_terms_of_use()

    assert registration_page.get_field_error_text() == "Name is required"
    assert registration_page.is_submit_button_disabled()


def test_registration_with_invalid_email_and_valid_password(driver):
    """Verify validation error when email format is invalid"""
    registration_page = RegistrationPage(driver)
    user = generate_user()
    user.email = INVALID_EMAIL

    registration_page.open_registration_page()
    registration_page.fill_registration_form(user)
    registration_page.click_on_terms_of_use()

    assert registration_page.is_submit_button_disabled()
    assert registration_page.get_field_error_text() == "Wrong email format"
    assert not registration_page.is_sign_out_displayed()


def test_registration_with_valid_email_and_invalid_password(driver):
    """Verify validation error when password does not meet security requirements"""
    registration_page = RegistrationPage(driver)
    user = generate_user()
    user.password = INVALID_PASSWORD

    registration_page.open_registration_page()
    registration_page.fill_registration_form(user)
    registration_page.click_on_terms_of_use()

    assert registration_page.is_submit_button_disabled()
    assert "password" in registration_page.get_field_error_text().lower()
    assert not registration_page.is_sign_out_displayed()


def test_registration_with_already_exist_email(driver):
    """Verify error modal appears when registering with an already registered email"""
    registration_page = RegistrationPage(driver)

    registration_page.open_registration_page()
    registration_page.fill_registration_form(DEFAULT_USER)
    registration_page.click_on_terms_of_use()
    registration_page.click_on_registration_button()

    assert registration_page.get_modal_title() == "Registration failed"
    assert "User already exists" in registration_page.get_modal_text()
    registration_page.close_modal()
    assert not registration_page.is_sign_out_displayed()
