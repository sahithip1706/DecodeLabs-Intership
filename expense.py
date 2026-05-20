print("===================================")
print("      DAILY EXPENSE TRACKER")
print("===================================")

total_expense = 0
expense_count = 0

while True:

    print("\n1. Add Expense")
    print("2. View Total Expense")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        category = input("Enter expense category: ")

        amount = float(input("Enter expense amount: ₹"))

        total_expense = total_expense + amount
        expense_count = expense_count + 1

        print("Expense Added Successfully")
        print("Category:", category)
        print("Amount Added: ₹", amount)

    elif choice == "2":

        print("\n------ Expense Summary ------")
        print("Total Entries:", expense_count)
        print("Total Expense: ₹", total_expense)

    elif choice == "3":

        print("Closing Expense Tracker...")
        print("Final Expense: ₹", total_expense)
        break

    else:
        print("Invalid Choice. Please try again.")