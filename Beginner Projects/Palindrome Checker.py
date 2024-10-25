# Palindrome Checker

def is_palindrome(s):
    """Check if the given string is a palindrome."""
    # Remove spaces and convert to lowercase for accurate comparison
    s_clean = ''.join(s.lower().split())
    return s_clean == s_clean[::-1]

def main():
    """Main function to run the Palindrome Checker."""
    print("Palindrome Checker")
    
    while True:
        s = input("Enter a word, phrase, or number to check (or 'q' to quit): ").strip()
        if s.lower() == 'q':
            print("Goodbye!")
            break
        if is_palindrome(s):
            print(f"'{s}' is a palindrome!\n")
        else:
            print(f"'{s}' is not a palindrome.\n")
        
        again = input("Do you want to check another? (yes/no): ").lower()
        if again != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
