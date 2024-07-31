# This program sends a automated email every monday to myself, containing a random dad joke.
# 7/17/2024 Trevor Childs
import smtplib
import datetime as dt
import random

my_email = 'projecttestinngemail123@gmail.com'
password = 'ivfbbvvwmgbfdjti'
jokes = []

with open('dadjokes.txt', 'r') as file:
    dadJokes = [jokes.append((joke.replace("\n", ''))) for joke in file]

now = dt.datetime.now()
if (now.weekday() == 0):
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                        to_addrs='trevorchilds8@gmail.com',
                        msg=f'Subject:Happy Monday!\n\n{jokes[random.randrange(100)]}')