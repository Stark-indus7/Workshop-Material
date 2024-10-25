# This is the main Python file for the Personal Expense Tracker project.
import json

def load_expenses():
    try:
        with open('expenses.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    with open('expenses.json', 'w') as f:
        json.dump(expenses, f)

def add_expense(expense, amount):
    expenses = load_expenses()
    expenses.append({'expense': expense, 'amount': amount})
    save_expenses(expenses)

def show_expenses():
    expenses = load_expenses()
    for expense in expenses:
        print(f"Expense: {expense['expense']} | Amount: {expense['amount']}")

while True:
    print("1. Add Expense\n2. Show Expenses\n3. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        expense = input("Enter expense: ")
        amount = float(input("Enter amount: "))
        add_expense(expense, amount)
    elif choice == 2:
        show_expenses()
    elif choice == 3:
        break
