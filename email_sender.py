import smtplib
import ssl
import csv
from getpass import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def read_email_data(filename="email_data.csv"):
    email_data = []
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            email_data.append(row)
    return email_data


def send_email(receiver_email, sender_email="kdleo93@gmail.com"):
    password = getpass("Type your password and hit enter: ")

    # Create email headers and body
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = email_data["recipient_email"]
    message["Subject"] = email_data["subject"]
    message.attach(MIMEText(email_data["body"], "plain"))

    # Set up the SMTP server and port
    smtp_server = "smtp.gmail.com"
    port = 465  # For SSL

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to the server and send the email
    try:
        server = smtplib.SMTP_SSL(smtp_server, port, context=context)
        server.login(sender_email, password)
        server.sendmail(
            sender_email, email_data["recipiebnt_email"], message.as_string())
    except Exception as e:
        print(e)
    finally:
        server.quit()


def send_multi_emails(filename="email_data.csv"):
    email_data = read_email_data(filename)
    for data in email_data:
        send_email(email_data)
