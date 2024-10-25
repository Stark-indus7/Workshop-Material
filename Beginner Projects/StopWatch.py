import time

def format_time(seconds):
    """Format seconds into H:M:S."""
    hrs = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    return f"{hrs:02}:{mins:02}:{secs:02}"

def stopwatch():
    """Run the stopwatch."""
    print("Simple Stopwatch")
    print("Press 's' to start, 'p' to pause, 'r' to reset, and 'q' to quit.")

    start_time = 0
    elapsed_time = 0
    running = False

    while True:
        command = input("Enter command (s/p/r/q): ").lower()

        if command == 's':
            if not running:
                running = True
                start_time = time.time() - elapsed_time
                print("Stopwatch started.")
            else:
                print("Stopwatch is already running.")
        elif command == 'p':
            if running:
                elapsed_time = time.time() - start_time
                running = False
                print(f"Stopwatch paused at {format_time(elapsed_time)}.")
            else:
                print("Stopwatch is not running.")
        elif command == 'r':
            elapsed_time = 0
            if running:
                start_time = time.time()
            print("Stopwatch reset.")
        elif command == 'q':
            print("Exiting stopwatch. Goodbye!")
            break
        else:
            print("Invalid command.")

        if running:
            current_time = time.time() - start_time
            print(f"Elapsed Time: {format_time(current_time)}", end='\r')
        else:
            print(f"Elapsed Time: {format_time(elapsed_time)}")

def main():
    """Main function to run the stopwatch."""
    stopwatch()

if __name__ == "__main__":
    main()

