import requests

req = requests.get("https://api.kanye.rest/")
print(req.json())


