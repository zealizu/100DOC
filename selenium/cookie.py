from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://ozh.github.io/cookieclicker/")
time.sleep(10)
language = driver.find_element(By.ID, "langSelect-EN")
language.click()
time.sleep(10)
cookie = driver.find_element(By.ID, "bigCookie")

def get_unlocked():
    unlocked = driver.find_elements(By.CSS_SELECTOR, "div .enabled")
    # print(unlocked)
    if len(unlocked)>1:
        unlocked[len(unlocked)-1].click()
    else:
        for i in unlocked:
            print(i.text)

# Set overall start time
overall_start_time = time.time()
run_duration = 300  # 5 minutes in seconds

while True:
    
    if time.time() - overall_start_time > run_duration:
        per_second = driver.find_element(By.ID, "cookiesPerSecond")
        print(per_second.text)
        break
    overall_start_time = time.time()
    while time.time() - overall_start_time < 5:
        cookie.click()
        time.sleep(0.2)
    try:
        get_unlocked()
    except IndexError:
        print("pass")
    