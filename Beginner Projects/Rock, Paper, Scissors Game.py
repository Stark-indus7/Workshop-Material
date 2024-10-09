import random
import functools

# Decorator for decorations
def greet(func):
    """Decorator to run certain lines before and after the code!
    """
    @functools.wraps(func)
    def decorator(*args,**kwargs):
        print("Good Morning!")
        result = func(*args,**kwargs)
        print("Thanks for playing! Goodbye!")
        return result
    return decorator    

def get_user_choice():
    """Get the user's choice."""
    choices = ['rock', 'paper', 'scissors']
    while True:
        choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if choice in choices:
            return choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def get_computer_choice():
    """Randomly select the computer's choice."""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    """Determine the winner of the game."""
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    """Play one round of Rock, Paper, Scissors."""
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result + "\n")

@greet
def main():
    """Main function to run the Rock, Paper, Scissors game."""
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        play_game()
        again = input("Do you want to play again? (yes/no): ").lower()
        if again != 'yes':
            break

if __name__ == "__main__":
    main()
