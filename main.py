#functions to add and view expense
expenses = {}

def add_expense():
    amount = float(input("Enter your expense amount : $ "))
    category = input("Enter the category of the expense : ")
    expenses[amount] = category
    print()
    print("Expense added succesfully.")

def view_expense():
    if not expenses:
        print()
        print("There are no expenses")
    else:
        print()
        for x,y in expenses.items():
            print(x, y)
    print()

# # START

print("Welcome to the Personal Expense Tracker!")

userName = input("Enter your name: ")
print(f"Hello, {userName}! Let's track your expenses today.")

while True:
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Exit")

    choice  = input("Enter the digit as per requirement : ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expense()
    elif choice == "3":
        print()
        print("Thank you !!")
        exit()
    else:
        print("invalid input. Try again")