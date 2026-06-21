class Transaction:
    """Handles the sale of a vehicle."""

    def __init__(self, customer, car, amount):
        self.customer = customer
        self.car = car
        self.amount = amount

    def process_payment(self):
        """Logic to process payment."""
        print(f"Processing ${self.amount} for {self.car.make}...")
        return True

    def generate_receipt(self):
        """Returns a formatted receipt string."""
        return f"Receipt: {self.customer.name} bought {self.car.model} for ${self.amount}."

    def cancel_transaction(self):
        """Voids the transaction."""
        print(f"Transaction for {self.car.model} has been cancelled.")
        
    def get_transaction_details(self):
        """Returns a summary of the transaction."""
        return f"Sale: {self.customer.name} -> {self.car.make} {self.car.model}"