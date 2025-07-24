import os  # For accessing environment variables
from dotenv import load_dotenv  # For loading environment variables from a .env file
import requests  # For making HTTP requests
from datetime import datetime  # For working with dates and times

load_dotenv()  # Load environment variables from .env file

# Retrieve Nutritionix API credentials and endpoints from environment variables
NUTRIX_APP_ID = os.environ["NUTRIX_APP_ID"]
NUTRIX_API_KEY = os.environ["NUTRIX_API_KEY"]
NUTRIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]
SHEETY_BEARER = os.environ["SHEETY_BEARER"]

today = datetime.now()  # Get the current date and time

# Prompt the user to enter the exercise(s) they did
exercise = input("Tell me what exerrcise you did: ").strip().lower()

# Parameters to send to the Nutritionix API
nutrix_parameters = {
    "query": exercise,
} 

# Headers for the Nutritionix API request
headers = {
    "Content-Type": "application/json",
    "x-app-id": NUTRIX_APP_ID,
    "x-app-key": NUTRIX_API_KEY,
}

# Send a POST request to Nutritionix API to analyze the exercise input
response = requests.post(url=NUTRIX_ENDPOINT, json=nutrix_parameters, headers=headers)
response.raise_for_status()  # Raise an error if the request was unsuccessful

# Extract the list of exercises from the API response
workout_done = response.json()["exercises"]

# Loop through each exercise returned by Nutritionix
for workout in workout_done:
    # Prepare the payload to send to the Sheety API for logging the workout
    workout_payload = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),  # Format the date as DD/MM/YYYY
            "time": today.strftime("%H:%M:%S"),  # Format the time as HH:MM:SS
            "exercise": workout["name"].title(),  # Capitalize the exercise name
            "duration": workout["duration_min"],  # Duration in minutes
            "calories": workout["nf_calories"]    # Calories burned
        }
    }
    # Headers for the Sheety API request, including authorization
    workout_headers = {
        "Content-Type": "application/json",
        "Authorization": SHEETY_BEARER,
    }

    # Send a POST request to Sheety API to log the workout
    response = requests.post(url=SHEETY_ENDPOINT, json=workout_payload, headers=workout_headers)
    # (Optional) You can check response.status_code or response.json() here for confirmation





