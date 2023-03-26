import random
import requests


# Task 1. ====================================
sites = [
        'https://www.google.com/',
        'https://www.facebook.com/',
        'https://twitter.com/',
        'https://www.amazon.com/',
        'https://www.apple.com/'
        ]

def get_random_site(lst):
    return random.choice(lst)

res = requests.get(get_random_site(sites))
print(f'Status code: {res.status_code}, url: {res.url}, HTML length: {len(res.text)}')


# Task 2. ====================================
def get_city_coordinates(location):
    coords_url = 'https://geocoding-api.open-meteo.com/v1/search'
    city_coords = requests.get(f'{coords_url}?name={location}&count=1')
    data = city_coords.json()
    return data

def get_and_round_latitude(city_coordinates):
    return round(city_coordinates['results'][0].get('latitude'), 2)

def get_and_round_longitude(city_coordinates):
    return round(city_coordinates['results'][0].get('longitude'), 2)

def get_current_weather_data():
    meteo_url = 'https://api.open-meteo.com/v1/forecast'
    current_weather = requests.get(meteo_url, params={
        'latitude': latitude,
        'longitude': longitude,
        'current_weather': 'true',
        'timezone': 'auto'
        })
    return current_weather.json()

try:
    city = input('Enter your city: ')
    coords = get_city_coordinates(city)
    latitude = get_and_round_latitude(coords)
    longitude = get_and_round_longitude(coords)
except KeyError:
    print('The city you entered is not available. Enter correct name next time.')
else:
    current_weather_json = get_current_weather_data()

    print(f'Current weather in {city} is: ')
    for key, value in current_weather_json['current_weather'].items():
        print(f'{key}: {value}')
