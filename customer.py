class Customer:
    """Manages customer information and purchase history."""
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.purchase_history = []

    def update_contact(self, new_email):
        """Updates the customer's email address."""
        self.email = new_email
        print(f"Contact updated for {self.name}.")

    def view_purchase_history(self):
        """Displays list of cars purchased."""
        return self.purchase_history

    def get_details(self):
        """Returns string summary of the customer."""
        return f"Customer: {self.name} ({self.email})"