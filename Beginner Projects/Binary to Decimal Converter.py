def binary_to_decimal(binary_str):
    """Convert a binary string to its decimal equivalent."""
    try:
        decimal = int(binary_str,2)
        return decimal
    except ValueError:
        return None

def main():
    """Main function to run the Binary to Decimal Converter."""
    print("Binary to Decimal Converter")
    
    while True:
        binary_str = input("Enter a binary number (or 'q' to quit): ").strip()
        if binary_str.lower() == 'q':
            print("Exiting converter. Goodbye!")
            break
        
        if all(char in '01' for char in binary_str):
            decimal = binary_to_decimal(binary_str)
            print(f"Binary: {binary_str} -> Decimal: {decimal}\n")
        else:
            print("Invalid binary number. Please enter only 0s and 1s.\n")

if __name__ == "__main__":
    main()
