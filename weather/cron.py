from .services import get_weather_data

def fetch_weather_data():
    cities = ['Tashkent']  
    for city in cities:
        get_weather_data(city)
