
"""
Custom Exception Classes
"""


class VehicleNotAvailableError(Exception):
    """Raised when a vehicle is already rented."""
    pass


class InvalidRentalDaysError(Exception):
    """Raised when rental days are invalid."""
    pass


class VehicleNotFoundError(Exception):
    """Raised when the requested vehicle does not exist."""
    pass
