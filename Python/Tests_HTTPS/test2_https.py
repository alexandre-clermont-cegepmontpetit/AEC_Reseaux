import requests

response = requests.get("https://www.py4e.com/")
print(response.text)