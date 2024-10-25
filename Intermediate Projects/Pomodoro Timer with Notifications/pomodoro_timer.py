# This is the main Python file for the Pomodoro Timer with Notifications project.
import time
import os

def pomodoro_timer(work_time=25, break_time=5):
    for i in range(1, 5):  # 4 Pomodoro cycles
        print(f"Pomodoro {i}: Work for {work_time} minutes")
        time.sleep(work_time * 60)  # Work time
        print("Time for a break!")
        time.sleep(break_time * 60)  # Break time
        print("Back to work!")

    print("Pomodoro sessions complete!")

pomodoro_timer()
