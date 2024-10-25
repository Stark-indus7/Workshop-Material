# This is the main Python file for the Weather Dashboard project.
import requests

def get_weather(city):
    api_key = "your_api_key"
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    data = response.json()

    if data["cod"] == 200:
        weather = data["main"]
        description = data["weather"][0]["description"]
        temp = weather["temp"]
        humidity = weather["humidity"]
        return f"Weather: {description}\nTemperature: {temp}°C\nHumidity: {humidity}%"
    else:
        return "City not found."

city = input("Enter city name: ")
print(get_weather(city))
