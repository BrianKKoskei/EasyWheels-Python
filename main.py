from car import Car
from dealership import Dealership
from customer import Customer
from transaction import Transaction

# Initialize
my_dealership = Dealership("EasyWheels")

def main():
    while True:
        print("\n--- EasyWheels Menu ---")
        print("1. Add Car\n2. Show Inventory\n3. Remove Car\n4. Exit")
        
        try:
            choice = input("Select an option: ")
            
            if choice == '1':
                vin = input("Enter VIN: ")
                make = input("Enter Make: ")
                model = input("Enter Model: ")
                price = float(input("Enter Price: "))
                my_dealership.add_car(Car(vin, make, model, price))
                
            elif choice == '2':
                my_dealership.show_inventory()
                
            elif choice == '3':
                vin = input("Enter VIN to remove: ")
                my_dealership.remove_car(vin)
                
            elif choice == '4':
                print("Exiting. Goodbye!")
                break
            else:
                print("Invalid choice.")
                
        except ValueError:
            print("Error: Invalid input! Please enter a number for the price.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()