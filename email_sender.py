import smtplib
import ssl
import csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import time
from os import environ

PASSWORD = environ.get("EMAIL_PASSWORD")
SENDER_EMAIL = environ.get("SENDER_EMAIL")
SMTP_SERVER = environ.get("SMTP_SERVER")  # Set up the SMTP server and port
SMTP_PORT = int(environ.get("SMTP_PORT, 465"))  # For SSL


def read_email_data(filename="email_data.csv"):
    email_data = []
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            email_data.append(row)
    return email_data


def send_email(email_data, SENDER_EMAIL):
    # Create email headers and body
    message = MIMEMultipart()
    message["From"] = SENDER_EMAIL
    message["To"] = email_data["recipient_email"]
    message["Subject"] = email_data["subject"]
    message.attach(MIMEText(email_data["body"], "plain"))

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to the server and send the email
    try:
        server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context)
        server.login(SENDER_EMAIL, PASSWORD)
        server.sendmail(
            SENDER_EMAIL, email_data["recipient_email"], message.as_string())
    except Exception as e:
        print(f"An error occurred while sending the email: {e}")
    finally:
        server.quit()


def send_multi_emails(filename="email_data.csv"):
    email_data_list = read_email_data(filename)
    for data in email_data_list:
        send_email(email_data=data)


def job():
    """Define the job to be executed at a scheduled time."""
    send_multi_emails()


def email_schedule(interval):
    """Schedules the email sending job."""
    schedule.every(interval).minutes.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
