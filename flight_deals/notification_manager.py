import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

class NotificationManager:
    def __init__(self):
        self.account_sid = os.environ["TWILIO_ACCOUNT_SID"]
        self.auth_token = os.environ["TWILIO_AUTH_TOKEN"]
        self.client = Client(self.account_sid, self.auth_token)
    
    def send_message(self, data):
        message = self.client.messages.create(
            body=f"Low price alert! Only £{data["price"]}, to fly from {data["depature_airport_code"]}, to {data["arrival_airport_code"]}, on {data["depature_time"]} at {data["depature_date"]}, until {data["return_date"]}",
            from_="+18782402177",
            to="+2348076367660",
        )
        print(message.body)