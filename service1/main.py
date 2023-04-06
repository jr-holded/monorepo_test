from lib.common_methods import handle_response
import requests

req = requests.get("https://api.kanye.rest/")

handle_response(req.json())

