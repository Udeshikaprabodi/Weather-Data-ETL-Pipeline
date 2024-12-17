import requests
import json

def extract_data():
    api_key = "f7d841544b4010a3a1f90b056b68ae0d"
    city = "London"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        with open('/tmp/weather_data.json', 'w') as f:
            json.dump(weather_data, f)
        print("Weather data extracted successfully.")
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")



