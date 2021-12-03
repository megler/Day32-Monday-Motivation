# mondayMotivation.py
#
# Python Bootcamp Day 32 - Monday Motivation Mini Project
# Usage:
#      Use the smtplib library to send motivational emails on chosen day of the
# week. (Monday)
#
# Marceia Egler December 2, 2021
import os, sys, smtplib, random
import datetime as dt
from dotenv import load_dotenv


def read_quotes():
    with open("quotes.txt") as quotes:
        lines = quotes.readlines()
        random_quote = random.choice(lines)

        return random_quote


def check_day():
    now = dt.datetime.now()
    weekday = now.weekday()
    return weekday


def send_mail(message):
    MY_EMAIL = os.getenv("MY_EMAIL")
    MY_PASSWORD = os.getenv("MY_PASSWORD")
    SMTP = os.getenv("SMTP")
    with smtplib.SMTP(SMTP, 587) as connection:
        connection.set_debuglevel(1)
        connection.ehlo()
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="example.email.com",  # CHANGE TO EMAIL YOU WANT TO SEND TO
            msg=f"From: {MY_EMAIL}\nSubject: Monday Motivation\n\n{message}",
        )


def main():
    load_dotenv()

    if check_day() == 0:
        msg = read_quotes()
        send_mail(msg)


if __name__ == "__main__":
    sys.exit(main())
