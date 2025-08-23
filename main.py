import csv
import os

# Store all expenses in a list
expenses = []

def load_expenses():
    """Load expenses from CSV file if it exists."""
    if os.path.exists("expenses.csv"):
        with open("expenses.csv", mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                amount = float(row[0])
                category = row[1]
                expenses.append({"amount": amount, "category": category})
        print("Previous expenses loaded.\n")

def save_expenses():
    """Save all expenses to a CSV file."""
    with open("expenses.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        for expense in expenses:
            writer.writerow([expense["amount"], expense["category"]])
    print("Expenses saved successfully!")

def add_expense():
    """Add a new expense to the list."""
    amount = float(input("Enter amount spent: ₹"))
    category = input("Enter category (e.g., food, travel, shopping): ")
    expenses.append({"amount": amount, "category": category})
    print("Expense added successfully!\n")

def view_expenses():
    """Display all expenses."""
    if not expenses:
        print("No expenses recorded yet.\n")
        return
    print("\n--- Expense List ---")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. ₹{expense['amount']} - {expense['category']}")
    print()

# ------------------ Main Program ------------------
print("Welcome to Personal Expense Tracker!")
load_expenses()  # Load data when program starts

while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Save & Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        save_expenses()
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")
