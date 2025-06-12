from dotenv import load_dotenv  # For loading environment variables from a .env file
import os  # For accessing environment variables
import requests  # For making HTTP requests
import smtplib  # For sending emails
from datetime import datetime  # For working with dates and times

load_dotenv()  # Load environment variables from .env file

my_email = os.getenv("MAIL")  # Get sender email from environment variable
password = os.getenv("PASSWORD")  # Get sender email password from environment variable

MY_LAT = 9.0579  # Your latitude
MY_LONG = 7.4951  # Your longitude

# Get the current position of the ISS from the API
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()  # Raise an error if the request was unsuccessful
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])  # Extract ISS latitude
iss_longitude = float(data["iss_position"]["longitude"])  # Extract ISS longitude

# Function to check if the ISS is within +5 or -5 degrees of your position
def within_ISS():
    if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5):
        return True
    else:
        return False

# Function to check if it is currently dark (after sunset or before sunrise)
def is_dark():
    # global sunrise, sunset, time_now
    if time_now.hour >= 17 or time_now.hour <= 5:
        return True
    else:
        return False 

# Parameters for the sunrise-sunset API
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

# Get sunrise and sunset times for your location
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
# Extract the hour part from the sunrise and sunset times (in UTC)
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
print(sunrise)  # Print sunrise hour for debugging

time_now = datetime.now()  # Get the current local time

# If the ISS is overhead and it is dark, send an email notification
if within_ISS() and is_dark():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # Secure the connection
        connection.login(user=my_email, password=password)  # Log in to the email account
        # Send an email notification
        connection.sendmail(
            from_addr=my_email,
            to_addrs="zealizu@gmail.com",
            msg="Subject:LOOK UP\n\nTHE SATELLITE IS ABOVE YOU"
        )

