import random

def roll_dice(num_dice, num_sides):
    """Roll the specified number of dice with given sides."""
    results = []
    for _ in range(num_dice):
        roll = random.randint(1, num_sides)
        results.append(roll)
    return results

def main():
    """Main function to run the Dice Rolling Simulator."""
    print("Dice Rolling Simulator")
    
    while True:
        try:
            num_dice = int(input("Enter the number of dice to roll: "))
            if num_dice <= 0:
                print("Number of dice must be positive.")
                continue
        except ValueError:
            print("Please enter a valid integer for the number of dice.")
            continue
        
        try:
            num_sides = int(input("Enter the number of sides per die: "))
            if num_sides <= 1:
                print("A die must have at least two sides.")
                continue
        except ValueError:
            print("Please enter a valid integer for the number of sides.")
            continue
        
        results = roll_dice(num_dice, num_sides)
        total = sum(results)
        print(f"\nYou rolled: {results}")
        print(f"Total: {total}\n")
        
        another = input("Do you want to roll again? (yes/no): ").lower()
        if another != 'yes':
            print("Thank you for using the Dice Rolling Simulator. Goodbye!")
            break

if __name__ == "__main__":
    main()
