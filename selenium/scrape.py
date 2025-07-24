from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome( options=chrome_options)


driver.get("https://www.python.org/")

times = driver.find_elements(By.CSS_SELECTOR, value=".menu li time")

names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget .shrubbery .menu li a")
print(names)
values = {}
for i in range(5):
    values[i] = {
        "time": times[i].text,
        "name": names[i].get_attribute("href")
    }

print(values)

driver.quit()