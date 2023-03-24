#How to use an API get to find the current ISS location

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

print(data)

#How to filter the data to get just the latitude and longitude

latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]

iss_position = (latitude, longitude)
print(iss_position)
