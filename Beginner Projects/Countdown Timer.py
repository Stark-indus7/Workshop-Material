import time

def format_time(seconds):
    """Format seconds into H:M:S."""
    hrs = seconds // 3600
    mins = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hrs:02}:{mins:02}:{secs:02}"

def countdown_timer():
    """Run the countdown timer."""
    print("Countdown Timer")
    
    while True:
        try:
            hours = int(input("Enter hours: "))
            minutes = int(input("Enter minutes: "))
            seconds = int(input("Enter seconds: "))
            total_seconds = hours * 3600 + minutes * 60 + seconds
            if total_seconds <= 0:
                print("Please enter a positive time duration.")
                continue
            break
        except ValueError:
            print("Please enter valid integers for time.")
    
    print(f"\nTimer set for {format_time(total_seconds)}. Starting countdown...\n")
    
    while total_seconds:
        hrs = total_seconds // 3600
        mins = (total_seconds % 3600) // 60
        secs = total_seconds % 60
        timer = f"{hrs:02}:{mins:02}:{secs:02}"
        print(timer, end='\r')
        time.sleep(1)
        total_seconds -= 1
    
    print("\nTime's up! 🔔")

def main():
    """Main function to run the Countdown Timer."""
    while True:
        countdown_timer()
        again = input("Do you want to set another timer? (yes/no): ").lower()
        if again != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
