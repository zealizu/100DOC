from flask import Flask, render_template, request
import random
from datetime import datetime
import requests

app = Flask(__name__)

@app.route("/")
def home():
    random_number = random.randint(1,10)
    now = datetime.now()
    return render_template("index.html", num=random_number, year=now.year, name="Chidubem")

@app.route("/guess/<name>")
def guess(name):
    params={
        "name":name
    }
    gender_response = requests.get(url="https://api.genderize.io", params=params)
    gender = gender_response.json()["gender"]
    age_response = requests.get(url="https://api.agify.io", params=params)
    age = age_response.json()["age"]
    return render_template("guess.html", age=age, gender=gender, name=name)

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        return render_template("login.html", username=request.form["username"], password=request.form["password"])
    else:
        return "not logged in"

if __name__ =="__main__":
    app.run(debug=True)