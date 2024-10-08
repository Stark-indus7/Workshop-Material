import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    """Generate a random password based on the specified criteria."""
    character_pool = ''
    if use_upper:
        character_pool += string.ascii_uppercase
    if use_lower:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation
    
    if not character_pool:
        raise ValueError("At least one character type must be selected.")
    
    # Ensure the password contains at least one character from each selected type
    password = []
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice(string.punctuation))
    
    # Fill the rest of the password length
    while len(password) < length:
        password.append(random.choice(character_pool))
    
    # Shuffle to prevent predictable sequences
    random.shuffle(password)
    
    return ''.join(password)

def get_user_preferences():
    """Get password preferences from the user."""
    while True:
        try:
            length = int(input("Enter desired password length (e.g., 12): "))
            if length < 4:
                print("Password length should be at least 4 for better security.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    use_upper = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_lower = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    use_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'
    
    if not any([use_upper, use_lower, use_digits, use_symbols]):
        print("At least one character type must be selected. Please try again.")
        return get_user_preferences()
    
    return length, use_upper, use_lower, use_digits, use_symbols

def main():
    """Main function to run the Password Generator."""
    print("Secure Password Generator")
    
    while True:
        length, use_upper, use_lower, use_digits, use_symbols = get_user_preferences()
        try:
            password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
            print(f"\nGenerated Password: {password}\n")
        except ValueError as ve:
            print(ve)
            continue
        
        again = input("Generate another password? (yes/no): ").lower()
        if again != 'yes':
            print("Password generation complete. Stay secure!")
            break

if __name__ == "__main__":
    main()
