import tkinter as tk
from tkinter import ttk
import sqlite3
import matplotlib.pyplot as plt

# Database setup
conn = sqlite3.connect('expenses.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS expenses
             (id INTEGER PRIMARY KEY, category TEXT, amount REAL, description TEXT)''')
conn.commit()

# Functions
def add_expense():
    category = category_var.get()
    amount = float(amount_var.get())
    description = description_var.get()
    c.execute("INSERT INTO expenses (category, amount, description) VALUES (?, ?, ?)",
              (category, amount, description))
    conn.commit()
    update_treeview()
    clear_fields()

def update_treeview():
    for row in tree.get_children():
        tree.delete(row)
    c.execute("SELECT * FROM expenses")
    for row in c.fetchall():
        tree.insert('', 'end', values=row)

def clear_fields():
    category_var.set('')
    amount_var.set('')
    description_var.set('')

def show_summary():
    c.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    data = c.fetchall()
    categories, amounts = zip(*data)
    plt.pie(amounts, labels=categories, autopct='%1.1f%%')
    plt.title('Expenses by Category')
    plt.show()

# GUI setup
root = tk.Tk()
root.title("Expense Tracker")

# Input fields
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Category:").grid(row=0, column=0)
category_var = tk.StringVar()
category_entry = ttk.Combobox(frame, textvariable=category_var)
category_entry['values'] = ('Food', 'Transport', 'Entertainment', 'Utilities', 'Other')
category_entry.grid(row=0, column=1)

tk.Label(frame, text="Amount:").grid(row=1, column=0)
amount_var = tk.StringVar()
amount_entry = tk.Entry(frame, textvariable=amount_var)
amount_entry.grid(row=1, column=1)

tk.Label(frame, text="Description:").grid(row=2, column=0)
description_var = tk.StringVar()
description_entry = tk.Entry(frame, textvariable=description_var)
description_entry.grid(row=2, column=1)

tk.Button(frame, text="Add Expense", command=add_expense).grid(row=3, column=0, columnspan=2, pady=10)
tk.Button(root, text="Show Summary", command=show_summary).pack()

# Treeview for displaying expenses
tree = ttk.Treeview(root, columns=('ID', 'Category', 'Amount', 'Description'), show='headings')
tree.heading('ID', text='ID')
tree.heading('Category', text='Category')
tree.heading('Amount', text='Amount')
tree.heading('Description', text='Description')
tree.pack(pady=10)

update_treeview()
root.mainloop()

conn.close()
