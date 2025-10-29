import requests
import json

URL = "https://api.nationalize.io/?name=johnson"
name = input("Enter name: ")
data = {
    "name": name
}
r = requests.get(URL, params=data)
all_datas = r.json()
print(f"Name: ",all_datas["name"])
all_countris = all_datas["country"]
for all_country in all_countris:
    print(f"Country Name: ",all_country["country_id"],f"Probability: ", all_country["probability"])
