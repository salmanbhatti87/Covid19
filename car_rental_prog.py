# Car Rental System
# Author: Python Programmer
# Version: 1.0

def initialize_cars():
    """Initialize and return the cars dictionary"""
    return {
        "Honda Civic": {"available": True, "renter": None},
        "Toyota Corolla": {"available": True, "renter": None},
        "Suzuki Alto": {"available": True, "renter": None},
        "Hyundai Tucson": {"available": True, "renter": None},
        "Kia Sportage": {"available": True, "renter": None}
    }

def display_welcome():
    """Display the welcome message"""
    print("\nWelcome to Car Rental System")
    print("----------------------------")

def display_menu():
    """Display the main menu options"""
    print("\nMain Menu:")
    print("1. View Available Cars")
    print("2. Rent a Car")
    print("3. Return a Car")
    print("4. View All Rentals")
    print("5. Exit")

def view_available_cars(cars):
    """Display available cars"""
    available_cars = [car for car, details in cars.items() if details["available"]]
    if available_cars:
        print("\nAvailable Cars:")
        print(", ".join(available_cars))
    else:
        print("\nNo cars currently available")

def rent_car(cars):
    """Handle car rental process"""
    view_available_cars(cars)
    
    car_name = input("\nEnter car name: ")
    if car_name not in cars:
        print("Car not found in our fleet!")
        return
    
    if not cars[car_name]["available"]:
        print("Car is already rented!")
        return
    
    renter_name = input("Enter your name: ").strip()
    if not renter_name:
        print("Please enter a valid name!")
        return
    
    cars[car_name]["available"] = False
    cars[car_name]["renter"] = renter_name
    print(f"{car_name} rented successfully to {renter_name}")

def return_car(cars):
    """Handle car return process"""
    rented_cars = [car for car, details in cars.items() if not details["available"]]
    if not rented_cars:
        print("\nNo cars currently rented out")
        return
    
    print("\nCurrently Rented Cars:")
    print(", ".join(rented_cars))
    
    car_name = input("\nEnter car name to return: ")
    if car_name not in cars:
        print("Car not found in our fleet!")
        return
    
    if cars[car_name]["available"]:
        print("This car wasn't rented out!")
        return
    
    renter_name = cars[car_name]["renter"]
    cars[car_name]["available"] = True
    cars[car_name]["renter"] = None
    print(f"{car_name} returned successfully by {renter_name}")

def view_rentals(cars):
    """Display all current rentals"""
    rented_cars = {car: details["renter"] for car, details in cars.items() if not details["available"]}
    
    if not rented_cars:
        print("\nNo cars currently rented out")
    else:
        print("\n🔑 Rented Cars:")
        for car, renter in rented_cars.items():
            print(f"- {car} -> {renter}")

def main():
    """Main function to run the car rental system"""
    cars = initialize_cars()
    display_welcome()
    
    while True:
        display_menu()
        
        try:
            option = int(input("\nChoose option (1-5): "))
            
            if option == 1:
                view_available_cars(cars)
            elif option == 2:
                rent_car(cars)
            elif option == 3:
                return_car(cars)
            elif option == 4:
                view_rentals(cars)
            elif option == 5:
                print("\nThank you for using our Car Rental System. Goodbye!")
                break
            else:
                print("Invalid option. Please choose 1-5.")
                
        except ValueError:
            print("Please enter a valid number (1-5)!")

if __name__ == "__main__":
    main()