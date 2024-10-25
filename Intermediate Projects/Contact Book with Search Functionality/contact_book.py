# This is the main Python file for the Contact Book with Search Functionality project.
import sqlite3

def create_db():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS contacts 
                (id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT)''')
    conn.commit()
    conn.close()

def add_contact(name, phone, email):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
    conn.commit()
    conn.close()

def search_contact(search_term):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("SELECT * FROM contacts WHERE name LIKE ?", ('%' + search_term + '%',))
    results = c.fetchall()
    conn.close()
    return results

create_db()
while True:
    print("1. Add Contact\n2. Search Contact\n3. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        add_contact(name, phone, email)
    elif choice == 2:
        search_term = input("Enter name to search: ")
        results = search_contact(search_term)
        for contact in results:
            print(contact)
    elif choice == 3:
        break
