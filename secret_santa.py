from dotenv import load_dotenv
import os
import random
import smtplib
import ssl

# Load variables from .env
load_dotenv()
sender = os.environ['EMAIL']
password = os.environ['PASSWORD']

def send_email(sender, receiver, recipient):
    body_msg = f"""\
From: {sender}
Subject: Your Secret Santa Present

Hi! Your Secret Santa is: {recipient}! 🎅
Remember to spend 10$-20$ on your gift, but don't stress about it being the perfect gift!
"""
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, body_msg)

names_and_emails = [
    ['Asiqur', 'asiqur@codedex.io'],
    ['Dharma', 'dharma@codedex.io'],
    ['Jerry', 'jerry@codedex.io'],
    ['Lillian', 'lillian@codedex.io'],
    ['Malcolm', 'malcolm@codedex.io'],
    ['Rose', 'rose@codedex.io'],
    ['Sonny', 'sonny@codedex.io'],
]

if len(names_and_emails) <= 1:
    print("Not enough participants to run Secret Santa.")
    quit()

first_name = names_and_emails[0][0]

while len(names_and_emails) >= 2:
    send_email(sender, names_and_emails[0][1], names_and_emails[1][0])
    names_and_emails.pop(0)
    random.shuffle(names_and_emails)

send_email(sender, names_and_emails[0][1], first_name)
