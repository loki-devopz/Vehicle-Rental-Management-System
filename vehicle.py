
"""
Vehicle Module
Demonstrates classes, inheritance, instance methods,
and polymorphism.
"""

from exceptions import (
    VehicleNotAvailableError,
    InvalidRentalDaysError
)


# Base Class
class Vehicle(object):

    def __init__(self, vehicle_id, brand, model, price_per_day):

        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.price_per_day = price_per_day

        self.is_available = True

    def display_details(self):
        """Display vehicle information."""

        print(f"Vehicle ID : {self.vehicle_id}")
        print(f"Brand      : {self.brand}")
        print(f"Model      : {self.model}")
        print(f"Price/Day  : Rs. {self.price_per_day}")
        print(f"Available  : {self.is_available}")

    def calculate_rental(self, days):
        """Calculate basic rental cost."""

        if days <= 0:
            raise InvalidRentalDaysError(
                "Rental days must be greater than zero."
            )

        return self.price_per_day * days

    def rent_vehicle(self, days):
        """Rent an available vehicle."""

        if not self.is_available:
            raise VehicleNotAvailableError(
                "This vehicle is already rented."
            )

        amount = self.calculate_rental(days)

        self.is_available = False

        print("\nVehicle rented successfully!")

        print(f"Rental Duration: {days} days")
        print(f"Total Amount: Rs. {amount:.2f}")

    def return_vehicle(self):
        """Return a rented vehicle."""

        if self.is_available:
            print("This vehicle has not been rented.")
            return

        self.is_available = True

        print("Vehicle returned successfully!")


# Child Class 1
class Car(Vehicle):

    def calculate_rental(self, days):
        """Calculate car rental with additional service charge."""

        if days <= 0:
            raise InvalidRentalDaysError(
                "Rental days must be greater than zero."
            )

        return (self.price_per_day * days) + 500


# Child Class 2
class Bike(Vehicle):

    def calculate_rental(self, days):
        """Calculate bike rental with a 10% discount."""

        if days <= 0:
            raise InvalidRentalDaysError(
                "Rental days must be greater than zero."
            )

        return (self.price_per_day * days) * 0.90


# Child Class 3
class Truck(Vehicle):

    def calculate_rental(self, days):
        """Calculate truck rental with a fixed loading fee."""

        if days <= 0:
            raise InvalidRentalDaysError(
                "Rental days must be greater than zero."
            )

        return (self.price_per_day * days) + 1000
