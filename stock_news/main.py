import requests 
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
from twilio.rest import Client

load_dotenv()

STOCK_API_KEY = os.environ["STOCK_API_KEY"]
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK = "TSLA"
COMPANY_NAME = "Tesla"
NEWS_API_KEY = os.environ["NEWS_API_KEY"]
NEWS_ENDPOINT = "https://newsapi.org/v2/top-headlines"

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

now = datetime.now()
yesterday = (now - timedelta(days=1)).date()
two_days_ago =(now - timedelta(days=2)).date()
# If yesterday is weekend, go back to Friday
while yesterday.weekday() > 4:  # Monday=0, Sunday=6
    yesterday -= timedelta(days=1)
    
# If two days ago is weekend, go back to Friday  
while two_days_ago.weekday() > 4:
    two_days_ago -= timedelta(days=1)
    
# print(yesterday)
parameters_stock = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY, 
}
# response_stock = requests.get(url=STOCK_ENDPOINT, params=parameters_stock)
# response_stock.raise_for_status()
# stock_data = response_stock.json()
# print(stock_data)
# yesterday_price = float(stock_data["Time Series (Daily)"][str(yesterday)]["4. close"])
# two_days_price = float(stock_data["Time Series (Daily)"][str(two_days_ago)]["4. close"])
# price_change: float = ((yesterday_price - two_days_price) / two_days_price) * 100

parameters_news = {
    "q":COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
}
response_news = requests.get(url=NEWS_ENDPOINT, params=parameters_news)
response_news.raise_for_status()
print(response_news.json()["articles"][0]["content"])

# if round(price_change) >= 2 or round(price_change) <=5:
#     print(f"{price_change:.0f}")
#     message = client.messages.create(
#     body="it's going to rain today, Bring an umbrella.",
#     from_="+18782402177",
#     to="+2348076367660",
# )



## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

