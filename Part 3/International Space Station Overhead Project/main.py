# This Program is to notify yourself whenever the ISS is overhead
# 7/22/2024 Trevor Childs

import requests
from datetime import datetime
import smtplib
import time

my_email = 'projecttestinngemail123@gmail.com'
password = 'ivfbbvvwmgbfdjti'

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

my_lat = 40.534271
my_lng = -112.298447

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# iss_latitude = 38
# iss_longitude = -110
# time_now = 5

# Your position is within +5 or -5 degrees of the ISS position.
def inRange():
    # if ISS is within 4 degrees of my lat and lon then return true
    if (my_lat - 4) <= iss_latitude <= (my_lat + 4) and (my_lng -4) <= iss_longitude <= (my_lng + 4):
        # Within a range of 4 less or greater than my lat and lng.
        return True
    else:
        return False


parameters = {
    'lat': my_lat,
    'lng': my_lng,
    'formatted' : '0',
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour

#If the ISS is close to my current position

if(inRange() and time_now >= sunset and time_now <= sunrise):
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,to_addrs='trevorchilds8@gmail.com',msg="Subject:The ISS Is Over Utah!🛰️☝️\n\nThe International Space Station is over Tooele Utah! See if you can spot it! Good luck!")
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



