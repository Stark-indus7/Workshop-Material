# This is the main Python file for the To-Do List Application with SQLite project.
import sqlite3

def create_db():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task TEXT)''')
    conn.commit()
    conn.close()

def add_task(task):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    conn.commit()
    conn.close()

def show_tasks():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    conn.close()
    return tasks

create_db()
while True:
    print("1. Add Task\n2. Show Tasks\n3. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        task = input("Enter task: ")
        add_task(task)
    elif choice == 2:
        tasks = show_tasks()
        for task in tasks:
            print(task)
    elif choice == 3:
        break
