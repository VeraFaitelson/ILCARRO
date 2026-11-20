"""Page Object for the 'Let the car work' (Add Car) page"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from models.car import Car
from pages.base_page import BasePage


class AddCarPage(BasePage):
    """Encapsulates locators and actions for adding a new car"""

    # Navigation
    LET_CAR_WORK_LINK = (By.XPATH, "//a[text()='Let the car work']")

    # Form Inputs & Selects
    CITY_INPUT = (By.ID, "city")
    MANUFACTURE_INPUT = (By.NAME, "manufacture")
    MODEL_INPUT = (By.NAME, "model")
    YEAR_INPUT = (By.NAME, "year")
    FUEL_SELECT = (By.NAME, "fuel")
    GEAR_SELECT = (By.NAME, "gear")
    WHEELS_DRIVE_SELECT = (By.NAME, "wheelsDrive")
    DOORS_INPUT = (By.NAME, "doors")
    SEATS_INPUT = (By.NAME, "seats")
    CLASS_INPUT = (By.NAME, "carClass")
    SERIAL_NUMBER_INPUT = (By.NAME, "serialNumber")
    PRICE_INPUT = (By.NAME, "pricePerDay")
    ABOUT_TEXTAREA = (By.NAME, "about")
    IMAGE_URL_INPUT = (By.NAME, "image")
    PHOTO_FILE_INPUT = (By.ID, "photo-file")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def open_add_car_page(self):
        """Navigates to the 'Let the car work' form"""
        self.click(self.LET_CAR_WORK_LINK)
        self.find(self.CITY_INPUT)

    def select_dropdown_by_text(self, locator, visible_text: str):
        """Selects an option from a <select> dropdown by its visible label"""
        select_element = self.find(locator)
        Select(select_element).select_by_visible_text(visible_text)

    def fill_city(self, city: str):
        """Types city name and clicks the matching autocomplete suggestion"""
        self.fill(self.CITY_INPUT, city)
        suggestion_locator = (By.XPATH, f"//div[contains(@style, 'position: absolute')]//*[contains(text(), '{city}')] | //li[contains(text(), '{city}')]")
        self.click(suggestion_locator)

    def fill_car_form(self, car: Car):
        """Fills all required and optional fields using a Car model"""
        self.fill_city(car.city)
        self.fill(self.MANUFACTURE_INPUT, car.manufacture)
        self.fill(self.MODEL_INPUT, car.model)
        self.fill(self.YEAR_INPUT, car.year)
        self.select_dropdown_by_text(self.FUEL_SELECT, car.fuel)
        self.select_dropdown_by_text(self.GEAR_SELECT, car.gear)
        self.select_dropdown_by_text(self.WHEELS_DRIVE_SELECT, car.wheels_drive)
        self.fill(self.DOORS_INPUT, car.doors)
        self.fill(self.SEATS_INPUT, car.seats)
        self.fill(self.CLASS_INPUT, car.car_class)
        self.fill(self.SERIAL_NUMBER_INPUT, car.serial_number)
        self.fill(self.PRICE_INPUT, car.price_per_day)

        if car.about:
            self.fill(self.ABOUT_TEXTAREA, car.about)
        if car.image:
            self.fill(self.IMAGE_URL_INPUT, car.image)

    def submit_car_form(self):
        """Clicks the Submit button and waits for the form to reset after submission"""
        self.click(self.SUBMIT_BUTTON)
        self.wait.until(lambda d: self.get_manufacture_value() == "")

    def is_submit_button_disabled(self) -> bool:
        """Checks if the Submit button is currently disabled"""
        return self.is_button_disabled(self.SUBMIT_BUTTON)

    def get_manufacture_value(self) -> str:
        """Returns the current value of the Make input field"""
        return self.find(self.MANUFACTURE_INPUT).get_attribute("value") or ""

