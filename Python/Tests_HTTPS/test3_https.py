import urllib.request

# Define a User-Agent header
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

url = "https://www.py4e.com/"

# Create a request object
req = urllib.request.Request(url, headers=headers)

# Open the request
with urllib.request.urlopen(req) as response:
    html = response.read().decode()
    print(html)