from email_sender import email_schedule
from dotenv import load_dotenv

load_dotenv()  # This will load environment variables from a .env file.


def main():
    # call the send_multi_emails function
    email_schedule(5)


if __name__ == "__main__":
    main()
