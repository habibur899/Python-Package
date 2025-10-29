import requests
import json

URL = "https://api.genderize.io"
myName = input("Enter name: ")
data = {
    "name": myName
}
r = requests.get(url=URL, params=data)
gender = r.json()
mygen = gender["gender"]
myProba = gender["probability"]
print(f"Gender of {myName} is {mygen} with probability {myProba}")
