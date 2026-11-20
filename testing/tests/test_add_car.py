"""Tests for adding a new car ('Let the car work' functionality)"""

from pages.add_car_page import AddCarPage
from utils.data_generator import generate_car


def test_add_car_success(authenticated):
    """Verify successful creation of a new car with valid required fields."""
    add_car_page = AddCarPage(authenticated)
    car = generate_car()

    add_car_page.open_add_car_page()
    add_car_page.fill_car_form(car)
    add_car_page.submit_car_form()

    assert add_car_page.get_manufacture_value() == ""

