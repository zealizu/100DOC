from selenium import webdriver
from selenium.webdriver.common.by import By

#keep chrome browser open after the code finishes running

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/dp/B075CYMYK6?th=1")

button = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[3]/div/div/form/div/div/span/span/button")
#click button 
button.click()

price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
print(price_dollar)

#get elements by xpath
product_title = driver.find_element(By.XPATH, value='//*[@id="productTitle"]')

print(product_title.text)

# #closes the active tab 
# driver.close()

#quit closes the entire browser

driver.quit()