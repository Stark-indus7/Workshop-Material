# This project collects and analyzes IoT device data in real time.
# Implement the code here

import random
import time

def collect_iot_data():
    # Simulate IoT data collection
    temperature = random.uniform(20, 30)
    humidity = random.uniform(40, 60)
    return {'temperature': temperature, 'humidity': humidity}

def analyze_data(data):
    print(f"Temperature: {data['temperature']:.2f}°C, Humidity: {data['humidity']:.2f}%")

# Collect and analyze data every 5 seconds
while True:
    data = collect_iot_data()
    analyze_data(data)
    time.sleep(5)
