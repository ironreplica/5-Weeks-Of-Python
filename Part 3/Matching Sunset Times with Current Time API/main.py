# Sunset Times with API
# Trevor Childs 7/17/2024
import requests
from datetime import datetime

api_key = 'https://api.sunrise-sunset.org/json'

# Lat and long for Tooele
# https://tooeletech.udemy.com/course/100-days-of-code/learn/lecture/21214136#overview
# 5:07
parameters = {
    'lat': '40.534271',
    'lng': '-112.298447',
    'formatted' : '0',
}

response = requests.get(api_key, params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']

sunrise_hour = sunrise.split('T')[1].split(":")[0]
sunset_hour = sunset.split('T')[1].split(":")[0]

cur_time = datetime.now()

print(f'Sunrise Hour: {sunrise_hour} Sunset Hour: {sunset_hour}')