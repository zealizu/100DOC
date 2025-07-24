from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
my_email = os.environ["MAIL"]
my_password = os.environ["PASSWORD"]
url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

header = {
    "User-Agent":(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/117.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en,en-US;q=0.9",
}

response = requests.get(url, headers=header)

webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
print(soup.prettify()[:1000])

price = soup.find(name="span", class_ = "aok-offscreen").getText()
price = price.split()[0]

price = float(price.replace("$", ""))
product_name = soup.find(name = "span", id = "productTitle").getText()
product_name = " ".join(product_name.split())  # Removes extra spaces/newlines
product_name=product_name.replace("Sauté", "Saute")
# print(product_name)
# product_name = product_name.encode("utf-8")

# print(product_name)

if price < 100:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password) 
        connection.sendmail(from_addr=my_email, to_addrs="zealizu@gmail.com", msg=f"Subject:Amazon Price Tracker\n\n{product_name} is now ${price} \n{url}")