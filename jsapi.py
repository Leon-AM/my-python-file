import requests 
import json

response = requests.get("http://api.open-notify.org/astros.json")
print(response.status_code)

print()

json_data = response.json()
print(response.json())

print()

for this_people in json_data["people"]:
    print('NAME:',this_people["name"] , '\n SPACECRAFT NAME:', this_people["craft"], '\n')
