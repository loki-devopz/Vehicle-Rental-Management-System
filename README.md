# Vehicle Rental Management System

A simple console-based vehicle rental application written in Python. It demonstrates object-oriented programming concepts, including inheritance, polymorphism, custom exceptions, and instance methods.

## Features

- View all currently available vehicles
- Rent a vehicle by vehicle ID
- Return a rented vehicle
- Validate rental duration
- Handle unavailable vehicles and invalid input
- Apply vehicle-specific rental calculations

## Vehicle Types and Pricing

| Vehicle type | Base calculation | Additional pricing rule |
| --- | --- | --- |
| Car | Price per day x rental days | Add Rs. 500 service charge |
| Bike | Price per day x rental days | Apply 10% discount |
| Truck | Price per day x rental days | Add Rs. 1,000 loading fee |

The system starts with these vehicles:

| ID | Type | Brand | Model | Price per day |
| --- | --- | --- | --- | --- |
| V101 | Car | Toyota | Innova | Rs. 2,500 |
| V102 | Bike | Yamaha | R15 | Rs. 1,000 |
| V103 | Truck | Tata | Ace | Rs. 3,000 |
| V104 | Car | Hyundai | Creta | Rs. 2,000 |

## Project Structure

```text
VehicleRental/
  main.py       # Console menu and application flow
  vehicle.py    # Vehicle base class and vehicle subclasses
  exceptions.py # Custom application exceptions
```

## Requirements

- Python 3.x

No third-party packages are required.

## Getting Started

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Run the application:

```bash
python VehicleRental/main.py
```

## Using the Application

The application shows an interactive menu:

```text
1. View All Vehicles
2. Rent a Vehicle
3. Return a Vehicle
4. Exit
```

### Renting a Vehicle

Choose option `2`, enter a valid vehicle ID (for example, `V101`), and enter the number of rental days.

Rental days must be a positive integer. If a vehicle is already rented, the application reports that it is unavailable.

### Returning a Vehicle

Choose option `3` and enter the ID of the vehicle being returned.
