"""
This module defines the Car class for the EasyWheels dealership system.
It complies with PEP 8 standards.
"""

class Car:
    """Represents an individual vehicle in the dealership inventory."""

    def __init__(self, vin, make, model, price):
        """
        Initializes a new Car object.
        
        :param vin: String, Unique Vehicle Identification Number
        :param make: String, Manufacturer of the car (e.g., Toyota)
        :param model: String, Model of the car (e.g., Camry)
        :param price: Float, Selling price of the car
        """
        self.vin = vin
        self.make = make
        self.model = model
        self.price = float(price)
        self.status = "Available"  # Default status for new inventory

    def apply_discount(self, percentage):
        """Reduces the car's price by a given percentage."""
        if 0 < percentage < 100:
            discount_amount = self.price * (percentage / 100)
            self.price -= discount_amount
            print(f"Success: New price for {self.make} {self.model} is ${self.price:,.2f}")
        else:
            print("Error: Invalid discount percentage.")

    def mark_as_sold(self):
        """Changes the vehicle availability status to Sold."""
        self.status = "Sold"

    def get_details(self):
        """Returns a user-friendly summary string of the car's details."""
        return f"[{self.status}] VIN: {self.vin} | {self.make} {self.model} | Price: ${self.price:,.2f}"