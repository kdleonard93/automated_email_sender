# email_sender.py

import os
import smtplib
import csv
import schedule
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(email_data, sender_email="myemail@gmail.com"):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    password = os.getenv("EMAIL_PASSWORD")

    server.login(sender_email, password)

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = email_data["recipient_email"]
    message["Subject"] = email_data["subject"]
    message.attach(MIMEText(email_data["body"], "plain"))

    text = message.as_string()
    server.sendmail(sender_email, email_data["recipient_email"], text)
    server.quit()


def send_multi_emails(filename="email_data.csv"):
    with open(filename, "r") as file:
        email_data_list = csv.DictReader(file)
        for email_data in email_data_list:
            send_email(email_data)


def email_schedule(time_interval, filename="email_data.csv"):
    schedule.every(time_interval).minutes.do(
        send_multi_emails, filename=filename)

    while True:
        schedule.run_pending()
        time.sleep(1)
