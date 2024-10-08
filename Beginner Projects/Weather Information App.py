# Weather Information App

import requests

def get_weather(api_key, city):
    """Fetch weather data for the specified city using OpenWeatherMap API."""
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    if response.status_code != 200:
        return None
    return response.json()

def display_weather(data):
    """Display weather information."""
    city = data['name']
    country = data['sys']['country']
    temp = data['main']['temp']
    description = data['weather'][0]['description'].capitalize()
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    
    print(f"\nWeather in {city}, {country}:")
    print(f"Temperature: {temp}°C")
    print(f"Condition: {description}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s\n")

def main():
    """Main function to run the Weather Information App."""
    print("Weather Information App")
    
    # Replace 'YOUR_API_KEY' with your actual API key from OpenWeatherMap
    api_key = '4c592226a0bafcb6ae33e94a23b39c3d'
    
    while True:
        city = input("Enter city name (or 'q' to quit): ").strip()
        if city.lower() == 'q':
            print("Goodbye!")
            break
        
        weather_data = get_weather(api_key, city)
        if weather_data:
            display_weather(weather_data)
        else:
            print("Could not retrieve weather data. Please check the city name and try again.\n")
        
        again = input("Do you want to check another city? (yes/no): ").lower()
        if again != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
