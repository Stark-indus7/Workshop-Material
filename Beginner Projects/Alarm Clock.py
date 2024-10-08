# Alarm Clock

import time
import datetime
import winsound  # Note: This works on Windows. For other OS, alternative libraries are needed.

def play_alarm_sound():
    """Play an alarm sound."""
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 1000   # Set Duration To 1000 ms == 1 second
    for _ in range(5):  # Play sound 5 times
        winsound.Beep(frequency, duration)

def set_alarm():
    """Set the alarm time."""
    print("Set the alarm time.")
    while True:
        alarm_time = input("Enter time in 24-hour format (HH:MM): ")
        try:
            alarm_datetime = datetime.datetime.strptime(alarm_time, "%H:%M").time()
            return alarm_datetime
        except ValueError:
            print("Invalid time format. Please try again.")

def main():
    """Main function to run the Alarm Clock."""
    alarm_time = set_alarm()
    print(f"Alarm set for {alarm_time.strftime('%H:%M')}. Waiting...")

    while True:
        now = datetime.datetime.now().time()
        if now.hour == alarm_time.hour and now.minute == alarm_time.minute:
            print("Time to wake up!")
            play_alarm_sound()
            break
        time.sleep(30)  # Check every 30 seconds

if __name__ == "__main__":
    main()