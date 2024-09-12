import requests
from .models import WeatherData

API_KEY = 'd2333cbebe134b32b2b65545241209 '
BASE_URL = 'http://api.weatherapi.com/v1/current.json'

def get_weather_data(city):
    params = {'q': city, 'key': API_KEY, 'lang': 'uz'}
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    if response.status_code == 200:
        weather_data = {
            'city': city,
            'temperature': data['current']['temp_c'],
            'humidity': data['current']['humidity'],
            'description': data['current']['condition']['text'],
            'timezone': data['location']['tz_id'],
        }
        WeatherData.objects.create(**weather_data)
    else:
        print(f"Error fetching data for {city}: {data['error']['message']}")
