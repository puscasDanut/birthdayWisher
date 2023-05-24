import os
import pandas as pd
import smtplib
import datetime as dt
from random import randint

my_email = "test5242023@gmail.com"
password = "fswawynrbqtdfejn"

main_dir = os.path.dirname(__file__)


def send_mail(message, mail):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=mail, msg=f"Subject:Happy Birthday\n\n{message}")
        print("Email Sent")


def generate_letter(name):
    switch_letters = {
        0: main_dir + "./letter_1.txt",
        1: main_dir + "./letter_2.txt",
        2: main_dir + "./letter_3.txt",
    }
    letter_model = switch_letters[randint(0, 2)]
    with open(letter_model, mode="r") as letter_file:
        letter_contains = letter_file.read()
        letter_to_send = letter_contains.replace('[NAME]', name)
    return letter_to_send


def check_if_birthday(now):
    birthdays = pd.read_csv(main_dir + "./birthdays.csv")
    birthdays_dictionary = birthdays.to_dict(orient="records")
    this_month = now.month
    this_day = now.day
    for person in birthdays_dictionary:
        if person['month'] == this_month and person['day'] == this_day:
            send_mail(generate_letter(person['name']), person['email'])


while True:
    now = dt.datetime.now()
    if now.hour == 0 and now.second == 0:
        check_if_birthday(now)


