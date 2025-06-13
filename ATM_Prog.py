# Smart ATM Simulator
# Author: Python Programmer
# Version: 1.0

def initialize_accounts():
    """Initialize and return the accounts dictionary"""
    return {
        1001: {"name": "John Doe", "pin": 1234, "balance": 5000.0},
        1002: {"name": "Jane Smith", "pin": 5678, "balance": 10000.0},
        1003: {"name": "Bob Johnson", "pin": 4321, "balance": 7500.0}
    }

def display_welcome():
    """Display the welcome message"""
    print("\nWelcome to Python ATM")
    print("-----------------------")

def login(accounts):
    """Handle the login process and return the account number if successful"""
    while True:
        try:
            acc_no = int(input("\nEnter account number: "))
            if acc_no not in accounts:
                print("Account not found. Please try again.")
                continue
                
            pin = int(input("Enter PIN: "))
            if accounts[acc_no]["pin"] != pin:
                print("Incorrect PIN. Please try again.")
                continue
                
            print("\nLogin successful!")
            return acc_no
            
        except ValueError:
            print("Invalid input. Please enter numbers only.")

def display_menu():
    """Display the ATM menu options"""
    print("\nPlease select an option:")
    print("1. View Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

def view_balance(account):
    """Display the current balance"""
    print(f"\nCurrent balance: Rs. {account['balance']:.2f}")

def deposit_money(account):
    """Handle money deposit"""
    try:
        amount = float(input("\nEnter deposit amount: Rs. "))
        if amount <= 0:
            print("Amount must be positive.")
        else:
            account['balance'] += amount
            print(f"Deposit successful. New balance: Rs. {account['balance']:.2f}")
    except ValueError:
        print("Invalid amount. Please enter a number.")

def withdraw_money(account):
    """Handle money withdrawal"""
    try:
        amount = float(input("\nEnter withdrawal amount: Rs. "))
        if amount <= 0:
            print("Amount must be positive.")
        elif amount > account['balance']:
            print("Insufficient balance.")
        else:
            account['balance'] -= amount
            print(f"Withdrawal successful. New balance: Rs. {account['balance']:.2f}")
    except ValueError:
        print("Invalid amount. Please enter a number.")

def main():
    """Main function to run the ATM simulator"""
    accounts = initialize_accounts()
    display_welcome()
    
    # Login process
    acc_no = login(accounts)
    current_account = accounts[acc_no]
    
    # Main menu loop
    while True:
        display_menu()
        
        try:
            option = int(input("\nChoose option (1-4): "))
        except ValueError:
            print("Invalid option. Please enter a number (1-4).")
            continue
            
        if option == 1:
            view_balance(current_account)
        elif option == 2:
            deposit_money(current_account)
        elif option == 3:
            withdraw_money(current_account)
        elif option == 4:
            print("\nThank you for using Python ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-4.")

if __name__ == "__main__":
    main()