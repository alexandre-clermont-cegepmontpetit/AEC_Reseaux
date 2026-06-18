import requests
import datetime

# Coordinates for Longueuil, Quebec
LATITUDE = 45.5391
LONGITUDE = -73.5186

# Open-Meteo API URL
url = "https://open-meteo.com"

# Request parameters for current weatherd
params = {
    "latitude": LATITUDE,
    "longitude": LONGITUDE,
    "current": "temperature_2m,precipitation,weather_code",
    "timezone": "America/Montreal"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    temp = data["current"]["temperature_2m"]
    precip = data["current"]["precipitation"]
    time = data["current"]["time"]
    
    print(f"Weather Report for Longueuil (Coordinates: {LATITUDE}, {LONGITUDE})")
    print(f"Time: {time}")
    print(f"Temperature: {temp}°C")
    print(f"Precipitation: {precip} mm")
else:
    print("Failed to fetch data.")
