"""Helper functions to generate random test data"""

import uuid

from conftest import DEFAULT_USER
from models.car import Car
from models.user import User


def generate_unique_email() -> str:
    """Generates a unique email address"""
    random_part = uuid.uuid4().hex[:8]
    return f"qa_user_{random_part}@gmail.com"


def generate_user() -> User:
    """Creates a new valid User with a unique email"""
    return User(
        first_name=DEFAULT_USER.first_name,
        last_name=DEFAULT_USER.last_name,
        email=generate_unique_email(),
        password=DEFAULT_USER.password,
    )


def generate_car() -> Car:
    """Creates a valid Car object with a unique registration serial number"""
    unique_serial = f"12-{uuid.uuid4().hex[:3]}-89"
    return Car(
        city="Haifa",
        manufacture="Toyota",
        model="Corolla",
        year="2022",
        fuel="Petrol",
        gear="Automatic",
        wheels_drive="FWD",
        doors="4",
        seats="5",
        car_class="C",
        serial_number=unique_serial,
        price_per_day="150",
    )
