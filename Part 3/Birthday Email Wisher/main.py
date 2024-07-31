# This program sends an automated birthday email to all of the contacts in the birthdays.csv when it is their birthday.
# 7/17/2024 Trevor Childs
import smtplib
import datetime as dt
import random
import os, os.path
import pandas as pd

my_email = 'projecttestinngemail123@gmail.com'
password = 'ivfbbvvwmgbfdjti'

today = dt.datetime.now()
todaysTuple = (today.month, today.day)

# * Generating a random email
def generateEmail(name):
    # Grab the list of available templates
    try:
        emailsList = os.listdir('emails/')
    except:
        print('Error')
    else:
        try:
            activeEmailFile = open(f'emails/{emailsList[random.randrange(len(emailsList))]}', 'r') # Generate a random index and grab a random email
        except FileNotFoundError:
            print('Error, cannot find the files your are looking for.')
        else:
            print(activeEmailFile)
            try:
                emailText = ''.join(activeEmailFile.readlines()).replace('[NAME]', name)
            except TypeError:
                print('Error, please pass in a string.')
            else:
                return emailText # Return the new email
def sendEmail(text):
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                        to_addrs='trevorchilds8@gmail.com',
                        msg=f'Subject:Happy Birthday!\n\n{text}')
# * Logic for checking for birthday
try:
    data_file = pd.read_csv('birthdays.csv')
    data_dictionary = data_file.to_dict('split')
    birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data_file.iterrows()}
except FileNotFoundError:
    print('File does not exist, or cannot be found.')
except KeyError:
    print('A Key error has occurred.')

    if todaysTuple in birthdays_dict:
        name = birthdays_dict[todaysTuple]['name']
        email = birthdays_dict[todaysTuple]['email']
        sendEmail(generateEmail(name))
