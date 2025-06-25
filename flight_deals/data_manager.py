import requests
import os
from dotenv import load_dotenv

load_dotenv()


class DataManager:
    def __init__(self):
        self.api_key = os.environ["SHEETY_API"]
        self.auth = os.environ["SHEETY_AUTH"]
        self.header = {
            "Authorization": self.auth
        }
    
    def get_data(self):
        response = requests.get(url= self.api_key, headers=self.header)
        response.raise_for_status()
        return response.json()["prices"]
    
    def update_sheet(self, sheet_data:list):
        sheet_data = sheet_data
        for i in sheet_data:
            payload = {
                "price":{
                    "iataCode": i["iataCode"]
                }
            }
            response = requests.put(url=f"{self.api_key}/{i["id"]}", json= payload, headers=self.header)
            response.raise_for_status()
            # print(response.text)