"""Base Page Object containing shared Selenium helper methods"""

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """Base class for all Page Objects. Wraps common WebDriver interactions"""

    # Common UI elements shared across pages (header & modal dialogs)
    SIGN_OUT_BUTTON = (By.CSS_SELECTOR, "button.navigation-link.linklike")
    MODAL_BOX = (By.CSS_SELECTOR, "div[role='dialog']")
    MODAL_TITLE = (By.CSS_SELECTOR, "div.modal-content h3")
    MODAL_TEXT = (By.CSS_SELECTOR, "div.modal-content p")
    MODAL_OK_BUTTON = (By.CSS_SELECTOR, "div[role='dialog'] .btn--primary")
    FIELD_ERROR = (By.CSS_SELECTOR, "div.error")

    def __init__(self, driver: WebDriver, timeout: int = 10):
        """Stores WebDriver instance and creates a reusable explicit wait object"""
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find(self, locator):
        """Waits until the element is visible on the page and returns it"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        """Waits until the element is clickable and performs a click"""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def fill(self, locator, value: str):
        """Clears an input field and types the given text"""
        element = self.find(locator)
        element.clear()
        element.send_keys(value)

    def is_visible(self, locator, timeout: int = 5) -> bool:
        """Safely checks if an element becomes visible within timeout without raising an exception"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def is_button_disabled(self, locator) -> bool:
        """Checks if a button has the 'disabled' attribute"""
        element = self.find(locator)
        return element.get_attribute("disabled") is not None

    def get_field_error_text(self) -> str:
        """Returns the validation error text displayed under an input field"""
        return self.find(self.FIELD_ERROR).text

    def get_modal_title(self) -> str:
        """Returns the header text of the popup modal dialog"""
        return self.find(self.MODAL_TITLE).text

    def get_modal_text(self) -> str:
        """Returns the full text content of the popup modal dialog"""
        return self.find(self.MODAL_BOX).text

    def close_modal(self):
        """Clicks 'OK' on the modal dialog and waits until it disappears"""
        self.click(self.MODAL_OK_BUTTON)
        self.wait.until(EC.invisibility_of_element_located(self.MODAL_BOX))

    def is_sign_out_displayed(self, timeout: int = 5) -> bool:
        """Checks if the 'Log out' button is visible in the navigation bar"""
        return self.is_visible(self.SIGN_OUT_BUTTON, timeout=timeout)
