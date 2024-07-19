import requests

def get_weather(city):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"
    location_response = requests.get(url)
    longitude = location_response.json()['results'][0]['longitude']
    latitude = location_response.json()['results'][0]['latitude']

    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()['current']["temperature_2m"]
    else:
        return None
