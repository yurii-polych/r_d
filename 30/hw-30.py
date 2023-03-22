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
try:
    city = input('Enter your city: ')
    coords_url = 'https://geocoding-api.open-meteo.com/v1/search'
    city_coords = requests.get(f'{coords_url}?name={city}&count=1')
    data = city_coords.json()

    latitude = round(data['results'][0].get('latitude'), 2)
    longitude = round(data['results'][0].get('longitude'), 2)
except KeyError:
    print('The city you entered is not available. Enter correct name next time.')
else:
    meteo_url = 'https://api.open-meteo.com/v1/forecast'
    current_weather = requests.get(f'{meteo_url}?latitude={latitude}&longitude={longitude}'
                                   '&current_weather=true&timezone=auto')
    current_weather_json = current_weather.json()

    print(f'Current weather in {city} is: ')
    for key, value in current_weather_json['current_weather'].items():
        print(f'{key}: {value}')
