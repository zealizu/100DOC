import requests  # Import the requests library for making HTTP requests
from datetime import datetime

MY_LAT = 9.0579
MY_LONG = 7.4951

# # Send a GET request to the ISS location API
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()  # Raise an error if the request was unsuccessful

# # Parse the response as JSON
# data = response.json()

# # Extract the longitude and latitude of the ISS from the JSON data
# latitude = data["iss_position"]["latitude"]
# longitude = data["iss_position"]["longitude"]

# # Store the ISS position as a tuple (latitude, longitude)
# position = (longitude, latitud e)
# print(position)  # Print the current position of the ISS

parameters = {
    "lat": MY_LAT ,
    "lng": MY_LONG ,
    "formatted": 0, 
}



response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters) 
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)

time_now = datetime.now()

