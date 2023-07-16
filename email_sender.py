import smtplib
import ssl
from getpass import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(receiver_email, subject, body, sender_email="kdleo93@gmail.com"):
    password = getpass("Type your password and hit enter: ")

    # Create email headers and body
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Set up the SMTP server and port
    smtp_server = "smtp.gmail.com"
    port = 465  # For SSL

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to the server and send the email
    try:
        server = smtplib.SMTP_SSL(smtp_server, port, context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    except Exception as e:
        print(e)
    finally:
        server.quit()
