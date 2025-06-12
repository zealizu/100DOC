# import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

# my_email = os.getenv("MAIL")
# password = os.getenv("PASSWORD")

# with smtplib.SMTP("smtp.gmail.com")as connection:
#     connection.starttls() #secures the connection
#     connection.login(user=my_email, password= password)
#     connection.sendmail(from_addr= my_email, to_addrs="zealizu@gmail.com", msg="Subject:Hello\n\nThis is the body of my email")

import datetime as dt

now = dt.datetime.now()
print(now)
