import requests
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
import json
load_dotenv()

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        # Your API credentials
        self.client_id = os.environ["AMADEUS_API_KEY"]
        self.client_secret = os.environ["AMADEUS_SECRET"]
        self.access_token = None
    
    def refresh_token(self):
        # API endpoint
        url = "https://test.api.amadeus.com/v1/security/oauth2/token"

        # Headers
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        # Data payload
        data = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }
        
        response = requests.post(url=url, data=data, headers=headers)
        response.raise_for_status()
        response_data = response.json()
        access_token = response_data["access_token"]
        return access_token
    
    def check_flight(self):
        self.access_token = self.refresh_token()
        
    def update_sheet(self, sheet_data:list):
        sheet_data = sheet_data
        url = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        self.access_token = self.refresh_token()
        header = {
            "Authorization": f"Bearer {self.access_token}"
        }
        # print(header)
        # print(sheet_data)
        for i in sheet_data:
            param = {
                "keyword": str(i["city"]).upper(),
                "max": 1,
                
            }
            response = requests.get(url=url, params=param, headers=header)
            response.raise_for_status
            data = response.json()["data"][0]
            i["iataCode"] = data["iataCode"]
            # print(response.text)
        return sheet_data
    
    def search_flight(self, sheet_data:list):
        sheet_data = sheet_data
        url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        
        self.access_token = self.refresh_token()
        
        header = {
            "Authorization": f"Bearer {self.access_token}"
        }
        data = {}
        for i in sheet_data:
            today = datetime.now()
            date = today + timedelta(days= 1)
            six_months_today = today + timedelta(days=(6 * 30))
            params = {
                "originLocationCode": "LON",
                "destinationLocationCode": f"{i["iataCode"]}",
                "departureDate": f"{date.strftime("%Y-%m-%d")}",
                "returnDate": f"{six_months_today.strftime("%Y-%m-%d")}",
                "adults": 1,
                "nonStop": "true",
                "currencyCode": "GBP",
                "max": 10
            }
            
            response = requests.get(url=url, params= params, headers=header)
            # print(response.text)
            response.raise_for_status()
            data[f"{i["city"]}"] = response.json()["data"]
            # print(response.text)
        with open("data.json", "w") as file:
            json.dump(data, file)
        return data