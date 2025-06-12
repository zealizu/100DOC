import smtplib  # For sending emails
import random  # For selecting a random quote
import os  # For accessing environment variables
from dotenv import load_dotenv  # For loading environment variables from a .env file
import datetime as dt  # For working with dates and times

# Load environment variables from .env file (for email and password)
load_dotenv()

# Access the email and password from environment variables
my_email = os.getenv('MAIL')
password = os.getenv('PASSWORD')

# Get the current date and time
now = dt.datetime.now()

# Check if today is Tuesday (weekday() == 1 means Tuesday)
if now.weekday() == 0:
    # Open the quotes file and read all lines into a list
    with open("100DOC/birthday/quotes.txt", "r") as file:
        content = file.readlines()
        
    # Set up the SMTP connection to Gmail
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # Secure the connection
        connection.login(user=my_email, password=password)  # Log in to the email account
        # Send an email with a random quote as the message body
        connection.sendmail(
            from_addr=my_email,
            to_addrs="zealizu@gmail.com",
            msg=f"Subject:Monday Motivation\n\n{random.choice(content)}"
        )