import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

API_KEY = os.environ["API_KEY"]
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

parameters = {
    "lat" : 9.0579,
    "lon" : 7.4951,
    "appid" : API_KEY,
    "cnt" : 4
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for data in weather_data["list"]:
    if data["weather"][0]["id"] < 700:
        will_rain = True
    else:
        will_rain = True

if will_rain:
    message = client.messages.create(
    body="it's going to rain today, Bring an umbrella.",
    from_="+18782402177",
    to="+2348076367660",
)
    print("Bring an umbrella.")
