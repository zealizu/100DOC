import os  # For accessing environment variables
from dotenv import load_dotenv  # For loading environment variables from a .env file
import pandas  # For reading and handling CSV data
import smtplib  # For sending emails
import datetime as dt  # For working with dates and times
import random  # For selecting a random letter template

load_dotenv()  # Load environment variables from .env file

my_email = os.getenv("MAIL")  # Get sender email from environment variable
password = os.getenv("PASSWORD")  # Get sender email password from environment variable

# Read the birthdays CSV file into a pandas DataFrame
data = pandas.read_csv("100DOC/birthday/birthdays.csv")
birthday_data = data.to_dict(orient="records")  # Convert DataFrame to a list of dictionaries

now = dt.datetime.now()  # Get the current date and time

# Loop through each birthday entry
for i in birthday_data:
    # Check if today matches the birthday (month and day)
    if i["month"] == now.month and i["day"] == now.day:
        # Randomly select one of the letter templates
        letter = f"100DOC/birthday/letter_templates/{random.choice(['letter_1.txt','letter_2.txt','letter_3.txt'])}"
        # Open and read the selected letter template
        with open(letter, "r") as file:
            content = file.read()
        # Replace the placeholder [NAME] with the actual name from the CSV
        content = content.replace("[NAME]", i["name"])
        # Set up the SMTP connection and send the birthday email
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()  # Secure the connection
            connection.login(user=my_email, password=password)  # Log in to the email account
            # Send the email with subject and personalized content
            connection.sendmail(
                from_addr=my_email,
                to_addrs=i["email"],
                msg=f"Subject:Happy Birthday\n\n{content}"
            )






