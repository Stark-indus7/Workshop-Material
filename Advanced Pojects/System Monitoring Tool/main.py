# This project monitors CPU, memory, and network usage.
# Implement the code here

import psutil

def system_monitor():
    print(f"CPU Usage: {psutil.cpu_percent()}%")
    print(f"Memory Usage: {psutil.virtual_memory().percent}%")
    print(f"Disk Usage: {psutil.disk_usage('/').percent}%")
    print(f"Network Sent: {psutil.net_io_counters().bytes_sent}")
    print(f"Network Received: {psutil.net_io_counters().bytes_recv}")

if __name__ == "__main__":
    system_monitor()
