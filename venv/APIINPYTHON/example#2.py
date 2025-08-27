import requests

# Mumbai coordinates
latitude = 19.0760
longitude = 72.8777

# Open-Meteo API endpoint
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

# Send GET request
response = requests.get(url)
data = response.json()

# Extract and print weather info
current = data.get("current_weather", {})
print(f"Temperature: {current.get('temperature')}°C")
print(f"Windspeed: {current.get('windspeed')} km/h")
print(f"Weather Code: {current.get('weathercode')}")
print(f"Time: {current.get('time')}")