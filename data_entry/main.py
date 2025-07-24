from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

prices = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
address = soup.select(selector=".StyledPropertyCardDataArea-anchor address")
property_links = soup.find_all(name="a", class_="StyledPropertyCardDataArea-anchor")
property_info = []

for i in range(len(prices)):
    property_info.append({
        "price": str(prices[i].text)[:6].strip(),
        "address": str(address[i].text).strip().replace("|", ""),
        "links":str(property_links[i].get('href')).strip()
    })

# print(property_info)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfDKDPPjhW1Jr6AoMhZy_0b07DamIedPlbEHsKap98D52pq-A/viewform?usp=header")




for i in property_info:
    input = driver.find_element(By.CLASS_NAME, "whsOnd")
    time.sleep(2)
    input.send_keys(i["price"], Keys.TAB, i["address"], Keys.TAB, i["links"], Keys.TAB, Keys.ENTER)
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Submit another response").click()
    
# print(soup)

