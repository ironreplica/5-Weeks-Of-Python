import requests
# Why does it need to be so complicated to install pip on windows
response = requests.get(url='http://api.open-notify.org/iss-now.json')
response.raise_for_status()

lon = response.json()['iss_position']['longitude']
lat = response.json()['iss_position']['latitude']

iss_position = (lon, lat)
print(iss_position)