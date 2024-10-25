# This is the main Python file for the Password Generator and Manager project.
import random
import string
import json

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def save_password(site, password):
    try:
        with open('passwords.json', 'r') as f:
            passwords = json.load(f)
    except FileNotFoundError:
        passwords = {}

    passwords[site] = password

    with open('passwords.json', 'w') as f:
        json.dump(passwords, f)

site = input("Enter site name: ")
password = generate_password()
print(f"Generated password for {site}: {password}")
save_password(site, password)
