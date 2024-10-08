# Simple Contact Book

import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    """Load contacts from the JSON file."""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            try:
                contacts = json.load(file)
                return contacts
            except json.JSONDecodeError:
                return {}
    return {}

def save_contacts(contacts):
    """Save contacts to the JSON file."""
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    """Add a new contact."""
    name = input("Enter contact name: ").strip()
    if name in contacts:
        print("Contact already exists.")
        return
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    contacts[name] = {'phone': phone, 'email': email}
    print(f"Contact '{name}' added.")

def view_contacts(contacts):
    """View all contacts."""
    if not contacts:
        print("No contacts found.")
    else:
        print("\nContacts:")
        for name, info in contacts.items():
            print(f"Name: {name}")
            print(f"  Phone: {info['phone']}")
            print(f"  Email: {info['email']}\n")

def search_contact(contacts):
    """Search for a contact by name."""
    name = input("Enter the contact name to search: ").strip()
    if name in contacts:
        info = contacts[name]
        print(f"\nName: {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}\n")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    """Delete a contact by name."""
    name = input("Enter the contact name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print("Contact not found.")

def main():
    """Main function to run the Contact Book application."""
    contacts = load_contacts()

    while True:
        print("\nContact Book")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            view_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
            save_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
            save_contacts(contacts)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
