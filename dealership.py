from car import Car

class Dealership:
    """Manages a collection of Car objects for EasyWheels."""

    def __init__(self, name):
        """Initializes the dealership with a name and an empty inventory."""
        self.name = name
        self.inventory = []  # This list will hold our Car objects

    def add_car(self, car):
        """Adds a new Car object to the inventory list."""
        self.inventory.append(car)
        print(f"✅ Added: {car.make} {car.model} to {self.name} inventory.")
        
    def remove_car(self, vin):
        """Removes a car from the inventory by its VIN."""
        for car in self.inventory:
            if car.vin == vin:
                self.inventory.remove(car)
                print(f"Vehicle with VIN {vin} has been removed.")
                return
        print(f"Error: Car with VIN {vin} not found.")

    def show_inventory(self):
        """Displays all cars currently in the dealership."""
        print(f"\n--- {self.name} Current Inventory ---")
        if not self.inventory:
            print("The inventory is currently empty.")
        else:
            for car in self.inventory:
                print(car.get_details())
        print("-----------------------------------\n")