"""Car data model"""

from dataclasses import dataclass


@dataclass
class Car:
    """Data model representing a car entity for the 'Let the car work' form"""

    city: str
    manufacture: str
    model: str
    year: str
    fuel: str
    gear: str
    wheels_drive: str
    doors: str
    seats: str
    car_class: str
    serial_number: str
    price_per_day: str
    about: str = ""
    image: str = ""
