# **Automated Email Sender 💌**

## **Table of Contents**

- [**Automated Email Sender 💌**](#automated-email-sender-)
  - [**Table of Contents**](#table-of-contents)
  - [**Overview**](#overview)
  - [**Features**](#features)
  - [**Prerequisites**](#prerequisites)
  - [**Usage**](#usage)
    - [**Configuration**](#configuration)
    - [**Environment Variables**](#environment-variables)
    - [**Running the Application**](#running-the-application)
  - [**Scheduling**](#scheduling)
  - [**Logging**](#logging)
  - [**Testing**](#testing)
  - [**Contributing**](#contributing)
  - [**License**](#license)
  - [**Acknowledgements**](#acknowledgements)

## **Overview**

Automated Email Sender is a Python-based application designed to automate the process of sending multiple emails. The application is ideal for sending batch emails, newsletters, and alerts.

## **Features**

- Send emails to multiple recipients with one command.
- Scheduling options for automated email sending.
- Environment variable support for secure password management.
- Detailed logs for tracking email sending activity.

## **Prerequisites**

- Python 3.x
- pip
- Virtualenv (optional but recommended)

1. **Clone the Repository**

   ```bash
   git clone https://github.com/YourUsername/automated_email_sender.git
   ```

2. **Navigate to the Project Directory**

   ```bash
   cd automated_email_sender
   ```

3. **Create a Virtual Environment (Optional)**

   ```bash
   virtualenv venv
   ```

4. **Activate the Virtual Environment**

   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

5. **Install Required Packages**

   ```bash
   pip install -r requirements.txt
   ```

## **Usage**

### **Configuration**

1. Populate `email_data.csv` with recipient email addresses, subjects, and body texts.
2. Create a `.env` file to store environment variables. (See [**Environment Variables**])

### **Environment Variables**

Create a `.env` file in the root directory and add the following variables:

```bash
EMAIL_PASSWORD=YourEmailPassword
SENDER_EMAIL=YourSenderEmail
SMTP_SERVER=YourSMTPServer
SMTP_PORT=YourSMTPPort
```

### **Running the Application**

To run the application:

```bash
python main.py
```

## **Scheduling**

To set up a schedule for automated email sending, modify the `email_schedule()` function in `email_sender.py`.

## **Logging**

The application logs all the email sending activity. You can find the log file at `logs/email.log`.

## **Testing**

See the `tests` folder for testing scripts. To run tests, execute:

```bash
python -m unittest discover tests
```

## **Contributing**

If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcome.

## **License**

Distributed under the MIT License. See `LICENSE` for more information.

## **Acknowledgements**

- Python
- smtplib
- schedule
