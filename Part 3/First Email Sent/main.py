import smtplib

my_email = 'projecttestinngemail123@gmail.com'
password = 'ivfbbvvwmgbfdjti'

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs='trevorchilds8@gmail.com',
                        msg="Subject:Hello\n\nThis is the body of my email.")
