# Simple Address Book GUI

import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

CONTACTS_FILE = "address_book.json"

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

def add_contact_gui():
    """Add a new contact via GUI."""
    name = simpledialog.askstring("Input", "Enter contact name:", parent=root)
    if not name:
        return
    phone = simpledialog.askstring("Input", "Enter phone number:", parent=root)
    if not phone:
        return
    email = simpledialog.askstring("Input", "Enter email address:", parent=root)
    if not email:
        return
    
    if name in contacts:
        messagebox.showerror("Error", "Contact already exists.")
        return
    
    contacts[name] = {'phone': phone, 'email': email}
    save_contacts(contacts)
    update_contact_list()
    messagebox.showinfo("Success", f"Contact '{name}' added.")

def delete_contact_gui():
    """Delete the selected contact."""
    selected = listbox_contacts.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Please select a contact to delete.")
        return
    name = listbox_contacts.get(selected[0])
    confirm = messagebox.askyesno("Confirm", f"Are you sure you want to delete '{name}'?")
    if confirm:
        del contacts[name]
        save_contacts(contacts)
        update_contact_list()
        messagebox.showinfo("Success", f"Contact '{name}' deleted.")

def view_contact_gui():
    """View details of the selected contact."""
    selected = listbox_contacts.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Please select a contact to view.")
        return
    name = listbox_contacts.get(selected[0])
    info = contacts[name]
    info_text = f"Name: {name}\nPhone: {info['phone']}\nEmail: {info['email']}"
    messagebox.showinfo("Contact Details", info_text)

def update_contact_list():
    """Update the listbox with current contacts."""
    listbox_contacts.delete(0, tk.END)
    for name in sorted(contacts.keys()):
        listbox_contacts.insert(tk.END, name)

def main():
    """Initialize the GUI application."""
    global root, listbox_contacts, contacts
    contacts = load_contacts()
    
    root = tk.Tk()
    root.title("Simple Address Book")
    root.geometry("400x300")
    
    # Listbox to display contacts
    listbox_contacts = tk.Listbox(root, font=("Arial", 12))
    listbox_contacts.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # Frame for buttons
    frame_buttons = tk.Frame(root)
    frame_buttons.pack(pady=5)
    
    btn_add = tk.Button(frame_buttons, text="Add Contact", width=12, command=add_contact_gui)
    btn_add.grid(row=0, column=0, padx=5)
    
    btn_view = tk.Button(frame_buttons, text="View Contact", width=12, command=view_contact_gui)
    btn_view.grid(row=0, column=1, padx=5)
    
    btn_delete = tk.Button(frame_buttons, text="Delete Contact", width=12, command=delete_contact_gui)
    btn_delete.grid(row=0, column=2, padx=5)
    
    update_contact_list()
    
    root.mainloop()

if __name__ == "__main__":
    main()
