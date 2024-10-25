# This project schedules and executes tasks at specified times.
# Implement the code here

import time
from datetime import datetime

def schedule_task(task, run_time):
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        if current_time == run_time:
            task()
            break
        time.sleep(1)

def my_task():
    print("Task executed!")

if __name__ == "__main__":
    run_time = input("Enter time to run task (HH:MM:SS): ")
    schedule_task(my_task, run_time)
