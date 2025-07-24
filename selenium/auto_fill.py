from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://secure-retreat-92358.herokuapp.com/")

firstname = driver.find_element(By.NAME, "fName")

firstname.send_keys("Zeal", Keys.TAB, "Izu", Keys.TAB, "ze@gmail.com", Keys.TAB, Keys.ENTER)


# driver.quit()