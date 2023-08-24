[**Automated Email Sender 💌**](#automated-email-sender-)

[**Table of Contents**](#table-of-contents)

- [**Overview**](#overview)
- [**Features**](#features)
- [**Prerequisites**](#prerequisites)
- [**Installation**](#installation)
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

## **Installation**

1. **Clone the Repository**

   ```python
   bashCopy codegit clone https://github.com/YourUsername/automated_email_sender.git
   ```

2. **Navigate to the Project Directory**

   ```python
   bashCopy codecd automated_email_sender
   ```

3. **Create a Virtual Environment (Optional)**

   ```python
   Copy codevirtualenv venv
   ```

4. **Activate the Virtual Environment**

   - On Windows:
     ```python
     Copy code.\venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```python
     bashCopy codesource venv/bin/activate
     ```

5. **Install Required Packages**

   ```python
   Copy codepip install -r requirements.txt
   ```

## **Usage**

### **Configuration**

1. Populate `email_data.csv` with recipient email addresses, subjects, and body texts.
2. Create a `.env` file to store environment variables. (See [**Environment Variables**](https://chat.openai.com/c/da875d12-1b74-4244-aec1-801cde1b1ae6#environment-variables))

### **Environment Variables**

Create a `.env` file in the root directory and add the following variables:

```python
makefileCopy codeEMAIL_PASSWORD=YourEmailPassword
SENDER_EMAIL=YourSenderEmail
SMTP_SERVER=YourSMTPServer
SMTP_PORT=YourSMTPPort
```

### **Running the Application**

To run the application:

```python
cssCopy codepython main.py
```

## **Scheduling**

To set up a schedule for automated email sending, modify the `email_schedule()` function in `email_sender.py`.

## **Logging**

The application logs all the email sending activity. You can find the log file at `logs/email.log`.

## **Testing**

See the `tests` folder for testing scripts. To run tests, execute:

```python
Copy codepython -m unittest discover tests
```

## **Contributing**

If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcome.

## **License**

Distributed under the MIT License. See `LICENSE` for more information.

## **Acknowledgements**

- Python
- smtplib
- schedule
