import requests


params={
        "name":"zeal"
    }
gender_response = requests.get(url="https://api.genderize.io", params=params)
gender = gender_response.json()["gender"]
age_response = requests.get(url="https://api.agify.io", params=params)
age = age_response.json()["age"]

print(age)