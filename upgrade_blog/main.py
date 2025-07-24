from flask import Flask, render_template, request
import requests 
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()



app = Flask(__name__)
blog_url = "https://gist.githubusercontent.com/gellowg/389b1e4d6ff8effac71badff67e4d388/raw/fc31e41f8e1a6b713eafb9859f3f7e335939d518/data.json"
response = requests.get(blog_url)
blog_posts = response.json()
my_email = os.environ["MAIL"]
my_password = os.environ["PASSWORD"]

@app.route('/')
def home():
    return render_template("index.html", blog_posts=blog_posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method =="GET":
        return render_template("contact.html", contact_text="Contact Me")
    else:
        data = request.form
        name = data["name"]
        email = data["email"]
        phone = data["phone"]
        message = data["message"]
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password) 
            connection.sendmail(from_addr=my_email, to_addrs="zealizu@gmail.com", msg=f"Subject:Contact Us\n\nName:{name}\nEmail:{email} \nPhone Number:{phone}\nMessage: {message}")
        print(name)
        return render_template("contact.html", contact_text="Successfully Sent Your Message")

@app.route("/post/<id>")
def post(id):
    return render_template("post.html", id=int(id), blog_posts=blog_posts)

if __name__ == "__main__":
    app.run(debug=True)

