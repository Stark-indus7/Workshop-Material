# This project helps manage personal finances by tracking income and expenses.
# Implement the code here

import csv

def add_expense(date, category, amount):
    with open('expenses.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

def view_expenses():
    with open('expenses.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

if __name__ == "__main__":
    while True:
        choice = input("1. Add Expense\n2. View Expenses\n3. Exit\nChoose an option: ")
        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            category = input("Enter the category: ")
            amount = input("Enter the amount: ")
            add_expense(date, category, amount)
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            break
