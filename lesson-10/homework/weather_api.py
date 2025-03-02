import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Use 'metric' to get temperature in Celsius
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        print(f"City: {city_name}")
        print(f"Temperature: {main['temp']}°C")
        print(f"Humidity: {main['humidity']}%")
        print(f"Weather: {weather['description']}")
    else:
        print(f"Error: {response.status_code}, {response.text}")

# Replace 'your_api_key' with your actual OpenWeatherMap API key
api_key = '33fbfa9a19d42bf1a9100941c937d846'
city_name = 'Tashkent'
get_weather(city_name, api_key)