import smtplib
import ssl
import csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import time
from os import environ
from dotenv import load_dotenv
import datetime

load_dotenv()  # This will load environment variables from a .env file.

PASSWORD = environ.get("EMAIL_PASSWORD")
SENDER_EMAIL = environ.get("SENDER_EMAIL")
SMTP_SERVER = environ.get("SMTP_SERVER")  # Set up the SMTP server and port
SMTP_PORT = int(environ.get("SMTP_PORT", 465))  # For SSL

# Check if necessary environment variables are set
if not (PASSWORD and SENDER_EMAIL and SMTP_SERVER):
    raise EnvironmentError("Required environment variables are missing!")


def read_email_data(filename="email_data.csv"):
    email_data = []
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            email_data.append(row)
    return email_data


def log_email(recipient, subject):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("email_log.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([recipient, subject, timestamp])


def send_email(email_data, sender_email=SENDER_EMAIL):
    # Create email headers and body
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = email_data["recipient_email"]
    message["Subject"] = email_data["subject"]
    message.attach(MIMEText(email_data["body"], "plain"))

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to the server and send the email
    try:
        server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context)
        server.login(sender_email, PASSWORD)
        server.sendmail(
            sender_email, email_data["recipient_email"], message.as_string())
        log_email(email_data["recipient_email"], email_data["subject"])
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


def email_schedule(interval_seconds):
    """Schedules the email sending job."""
    if interval_seconds % 60 == 0:
        print(f"Email job scheduled to run every {interval_seconds // 60} minute(s).")
    else:
        print(f"Email job scheduled to run every {interval_seconds} seconds.")

    schedule.every(interval_seconds).seconds.do(job)

    while True:
        # Check the time until the next scheduled job
        next_run = schedule.next_run()
        now = datetime.datetime.now()
        time_until_next = (next_run - now).total_seconds()

        # Print the message showing the next run time
        print(f"Next email job scheduled at {next_run.strftime('%Y-%m-%d %H:%M:%S')}.")
        print(f"Sleeping for {time_until_next:.0f} seconds...")

        while time_until_next > 0:
            sleep_interval = min(time_until_next, 5) 
            time.sleep(sleep_interval)
            time_until_next -= sleep_interval

        schedule.run_pending()