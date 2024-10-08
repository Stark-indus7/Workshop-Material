# Prime Number Checker

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    """Main function to run the Prime Number Checker."""
    print("Prime Number Checker")
    
    while True:
        try:
            number = int(input("Enter a number to check (or 'q' to quit): "))
        except ValueError:
            print("Exiting the Prime Number Checker. Goodbye!")
            break
        
        if is_prime(number):
            print(f"{number} is a prime number.\n")
        else:
            print(f"{number} is not a prime number.\n")
        
        again = input("Do you want to check another number? (yes/no): ").lower()
        if again != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
