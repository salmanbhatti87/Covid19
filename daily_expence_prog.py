# Daily Expense Tracker
# Author: Python Programmer
# Version: 1.0

from collections import defaultdict
from datetime import datetime

def initialize_expenses():
    """Initialize and return an empty defaultdict for expenses"""
    return defaultdict(list)

def display_welcome():
    """Display the welcome message"""
    print("\nDaily Expense Tracker")
    print("----------------------")

def display_menu():
    """Display the main menu options"""
    print("\nMain Menu:")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View by Category")
    print("4. View by Date")
    print("5. Exit")

def validate_date(date_str):
    """Validate date format (YYYY-MM-DD)"""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def add_expense(expenses):
    """Handle adding a new expense"""
    print("\nAdd Expense")
    
    while True:
        date = input("Enter date (YYYY-MM-DD): ")
        if not validate_date(date):
            print("Invalid date format. Please use YYYY-MM-DD")
            continue
        break
    
    category = input("Enter category: ").strip().title()
    if not category:
        print("Category cannot be empty!")
        return
    
    try:
        amount = float(input("Enter amount: Rs. "))
        if amount <= 0:
            print("Amount must be positive!")
            return
    except ValueError:
        print("Invalid amount. Please enter a number!")
        return
    
    expenses[date].append({"category": category, "amount": amount})
    print("Expense added")

def view_all_expenses(expenses):
    """Display all expenses chronologically"""
    if not expenses:
        print("\nNo expenses recorded yet!")
        return
    
    print("\nAll Expenses:")
    total = 0
    for date in sorted(expenses.keys()):
        print(f"\n{date}:")
        for expense in expenses[date]:
            print(f"  - {expense['category']}: Rs. {expense['amount']:.2f}")
            total += expense['amount']
    
    print(f"\nTotal Expenses: Rs. {total:.2f}")

def view_by_category(expenses):
    """Display expenses grouped by category"""
    if not expenses:
        print("\nNo expenses recorded yet!")
        return
    
    category_totals = defaultdict(float)
    for date_expenses in expenses.values():
        for expense in date_expenses:
            category_totals[expense['category']] += expense['amount']
    
    print("\nExpenses by Category:")
    for category, total in sorted(category_totals.items()):
        print(f"  - {category}: Rs. {total:.2f}")
    
    while True:
        category = input("\nEnter category to view details (or 'back' to return): ").strip().title()
        if category.lower() == 'back':
            break
        
        if category not in category_totals:
            print("Category not found!")
            continue
        
        print(f"\nAll '{category}' Expenses:")
        found = False
        for date in sorted(expenses.keys()):
            for expense in expenses[date]:
                if expense['category'] == category:
                    print(f"  - {date}: Rs. {expense['amount']:.2f}")
                    found = True
        
        if found:
            print(f"Total spent on {category}: Rs. {category_totals[category]:.2f}")

def view_by_date(expenses):
    """Display expenses for a specific date"""
    if not expenses:
        print("\nNo expenses recorded yet!")
        return
    
    while True:
        date = input("\nEnter date to view (YYYY-MM-DD) or 'back' to return: ")
        if date.lower() == 'back':
            break
        
        if not validate_date(date):
            print("Invalid date format. Please use YYYY-MM-DD")
            continue
        
        if date not in expenses:
            print(f"No expenses recorded on {date}")
            continue
        
        print(f"\nExpenses on {date}:")
        total = 0
        for expense in expenses[date]:
            print(f"  - {expense['category']}: Rs. {expense['amount']:.2f}")
            total += expense['amount']
        print(f"Total: Rs. {total:.2f}")

def main():
    """Main function to run the expense tracker"""
    expenses = initialize_expenses()
    display_welcome()
    
    while True:
        display_menu()
        
        try:
            option = int(input("\nChoose option (1-5): "))
            
            if option == 1:
                add_expense(expenses)
            elif option == 2:
                view_all_expenses(expenses)
            elif option == 3:
                view_by_category(expenses)
            elif option == 4:
                view_by_date(expenses)
            elif option == 5:
                print("\nThank you for using Daily Expense Tracker. Goodbye!")
                break
            else:
                print("Invalid option. Please choose 1-5.")
                
        except ValueError:
            print("Please enter a valid number (1-5)!")

if __name__ == "__main__":
    main()