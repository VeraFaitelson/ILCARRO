"""Pytest fixtures for browser setup and user authentication"""

import pytest
from selenium import webdriver

from models.user import User
from pages.login_page import LoginPage

BASE_URL = "https://icarro-v1.netlify.app/"

DEFAULT_USER = User(
    first_name="Test",
    last_name="User",
    email="qa_icarro_user@gmail.com",
    password="TestPass!12345",
)


@pytest.fixture
def driver():
    """Initializes Chrome WebDriver before a test and closes it afterward"""
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(BASE_URL)

    yield browser

    browser.quit()


@pytest.fixture
def authenticated(driver):
    """Logs in as the default test user and returns the authenticated driver."""
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.fill_login_form(DEFAULT_USER)
    login_page.click_on_login_button()
    if login_page.is_visible(login_page.MODAL_OK_BUTTON, timeout=15):
        login_page.close_modal()

    assert login_page.is_sign_out_displayed(timeout=15), "Failed to log in inside 'authenticated' fixture"

    return driver
