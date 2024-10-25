# This is the main Python file for the Personal Diary Application with Encryption project.
from cryptography.fernet import Fernet

def load_key():
    try:
        with open("secret.key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
        return key

def encrypt_message(message):
    key = load_key()
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message):
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message

while True:
    print("1. Write Diary Entry\n2. Read Diary Entry\n3. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        entry = input("Enter your diary entry: ")
        encrypted_entry = encrypt_message(entry)
        with open("diary.txt", "wb") as file:
            file.write(encrypted_entry)
    elif choice == 2:
        try:
            with open("diary.txt", "rb") as file:
                encrypted_entry = file.read()
            print("Your diary entry:", decrypt_message(encrypted_entry))
        except FileNotFoundError:
            print("No diary entry found.")
    elif choice == 3:
        break
