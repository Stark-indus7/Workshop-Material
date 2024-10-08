# Fibonacci Sequence Generator

def fibonacci_sequence(n):
    """Generate Fibonacci sequence up to n terms."""
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

def main():
    """Main function to run the Fibonacci Sequence Generator."""
    print("Fibonacci Sequence Generator")
    
    while True:
        try:
            n = int(input("Enter the number of terms to generate: "))
            if n <= 0:
                print("Please enter a positive integer.")
                continue
        except ValueError:
            print("Please enter a valid integer.")
            continue
        
        sequence = fibonacci_sequence(n)
        print(f"\nFibonacci Sequence ({n} terms):")
        print(sequence, "\n")
        
        again = input("Do you want to generate another sequence? (yes/no): ").lower()
        if again != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
