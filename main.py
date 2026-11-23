
"""
Vehicle Rental Management System
Main Application
"""

from vehicle import Vehicle, Car, Bike, Truck

from exceptions import (
    VehicleNotAvailableError,
    InvalidRentalDaysError
)


# Create vehicle objects
vehicles = {

    "V101": Car(
        "V101", "Toyota", "Innova", 2500
    ),

    "V102": Bike(
        "V102", "Yamaha", "R15", 1000
    ),

    "V103": Truck(
        "V103", "Tata", "Ace", 3000
    ),

    "V104": Car(
        "V104", "Hyundai", "Creta", 2000
    )
}


def display_menu():
    """Display application menu."""

    print("\n" + "=" * 45)
    print("       VEHICLE RENTAL MANAGEMENT")
    print("=" * 45)

    print("1. View All Vehicles")
    print("2. Rent a Vehicle")
    print("3. Return a Vehicle")
    print("4. Exit")


def display_vehicles():
    """Display all available vehicles."""

    print("\n===== AVAILABLE VEHICLES =====")

    for vehicle in vehicles.values():

        if vehicle.is_available:

            vehicle.display_details()

            print("-" * 35)


def rent_vehicle():
    """Rent a selected vehicle."""

    vehicle_id = input(
        "Enter Vehicle ID: "
    ).strip().upper()

    if vehicle_id not in vehicles:

        print("Vehicle not found!")
        return

    try:

        days = int(
            input("Enter rental days: ")
        )

        vehicle = vehicles[vehicle_id]

        vehicle.rent_vehicle(days)

    except ValueError:
        print("Please enter a valid number of days.")

    except InvalidRentalDaysError as error:
        print("Rental Error:", error)

    except VehicleNotAvailableError as error:
        print("Availability Error:", error)


def return_vehicle():
    """Return a previously rented vehicle."""

    vehicle_id = input(
        "Enter Vehicle ID: "
    ).strip().upper()

    if vehicle_id not in vehicles:

        print("Vehicle not found!")
        return

    vehicles[vehicle_id].return_vehicle()


# Main application
while True:

    display_menu()

    choice = input("\nEnter your choice: ")

    if choice == "1":

        display_vehicles()

    elif choice == "2":

        rent_vehicle()

    elif choice == "3":

        return_vehicle()

    elif choice == "4":

        print("Thank you for using Vehicle Rental!")
        break

    else:

        print("Invalid choice. Try again.")
