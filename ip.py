import requests
import json

base_url = "https://ipinfo.io/"
ip = "101.80.78.10"
end_url = "/geo"

r = requests.get(base_url + ip + end_url)
print(r.url)
print(r.json())
print(r.text)
