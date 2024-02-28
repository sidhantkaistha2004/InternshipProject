import json
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, description, category):
        expense = {
            "amount": amount,
            "description": description,
            "category": category,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.expenses.append(expense)
        print("Expense added successfully!")

    def show_expenses(self):
        for expense in self.expenses:
            print(f"{expense['date']} - {expense['category']}: ${expense['amount']} ({expense['description']})")

    def show_summary(self):
        categories = {}
        total_expense = 0

        for expense in self.expenses:
            total_expense += expense['amount']
            category = expense['category']
            categories[category] = categories.get(category, 0) + expense['amount']

        print("\nMonthly Summary:")
        print(f"Total Expense: ${total_expense}")

        print("\nCategory-wise Expenditure:")
        for category, amount in categories.items():
            print(f"{category}: ${amount}")

def save_to_file(expenses, filename="expenses.json"):
    with open(filename, 'w') as file:
        json.dump(expenses, file)

def load_from_file(filename="expenses.json"):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

if __name__ == "__main__":
    expense_tracker = ExpenseTracker()
    expense_tracker.expenses = load_from_file()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Show Expenses")
        print("3. Show Summary")
        print("4. Save and Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            amount = float(input("Enter the amount spent: $"))
            description = input("Enter a brief description: ")
            category = input("Enter the expense category: ")
            expense_tracker.add_expense(amount, description, category)

        elif choice == "2":
            print("\nAll Expenses:")
            expense_tracker.show_expenses()

        elif choice == "3":
            expense_tracker.show_summary()

        elif choice == "4":
            save_to_file(expense_tracker.expenses)
            print("Data saved. Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
