import requests
import json

# List of all objects (Get)
# URL = "https://api.restful-api.dev/objects/1"
# List of objects by ids (Get)
# URL = "https://api.restful-api.dev/objects?id=3&id=5&id=10"
# Single object (Get)
URL = "https://api.restful-api.dev/objects/7"

# Add object (Post)
# URL = "https://api.restful-api.dev/objects"

# Update object (Put)
# URL = "https://api.restful-api.dev/objects/7"

# Partially update object (Patch)
# URL = "https://api.restful-api.dev/objects/7"

# Delete object (Delete)
# URL = "https://api.restful-api.dev/objects/6"


r = requests.get(URL)
r_json = r.json()
data = json.dumps(r_json, indent=4)
print(data)
