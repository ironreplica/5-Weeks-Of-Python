import requests

api_key = '88fb0fd3e11e9beae5f671edf1d41502'
lat = '40.534271'
lon = '-112.298447'
apistring = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}'
params = {
    'cnt': 4,
}

response = requests.get(url=apistring, params=params)
response.raise_for_status()
weather_data = response.json()

weather_lists = weather_data['list']

will_rain = False
for list in weather_lists:
    weather_id = list['weather'][0]['id']
    if(weather_id < 700):
        will_rain = True
print(f'Will rain: {will_rain}')
#
# If the id is less than 500-700, print that you need an umbrella
