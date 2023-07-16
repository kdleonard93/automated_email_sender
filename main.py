from email_sender import send_email


def main():
    receiver_email = "khorvath726@gmail.com"
    subject = "Love you baby ♥️"
    body = "Just testing my script and telling you i love you soooo much!!"

    # call the send_email function
    send_email(receiver_email, subject, body)


if __name__ == "__main__":
    main()
