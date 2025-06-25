import requests
from datetime import datetime

USERNAME = "zealizu"
TOKEN = "12345678"
today = datetime.now()


pixela_endpoint = "https://pixe.la/v1/users"
user_params= {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)

# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    'unit' : "Min",
    "type": "float",
    "color": "momiji",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers= headers)


pixel_creation_endpoint = f"{graph_endpoint}/graph1"

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10"
}

# response = requests.post(url= pixel_creation_endpoint, json=pixel_data, headers= headers)
# print(response.text)

update_pixel_endpoint = f"{pixel_creation_endpoint}/{today.strftime('%Y%m%d')}"

update_data = {
    "quantity": "100"
}
# response = requests.put(url=update_pixel_endpoint, json=update_data, headers=headers)
response = requests.delete(url=update_pixel_endpoint, json=update_data, headers=headers)
print(response.text)