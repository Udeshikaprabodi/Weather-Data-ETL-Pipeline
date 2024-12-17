import json
import pandas as pd

def transform_data():
    with open('/tmp/weather_data.json', 'r') as f:
        weather_data = json.load(f)

    transformed_data = {
        'city': weather_data['name'],
        'temperature': round(weather_data['main']['temp'] - 273.15, 2),  # Convert Kelvin to Celsius
        'humidity': weather_data['main']['humidity'],
        'weather_description': weather_data['weather'][0]['description'],
        'timestamp': weather_data['dt']
    }

    df = pd.DataFrame([transformed_data])
    df.to_csv('/tmp/transformed_weather_data.csv', index=False)
    print("Weather data transformed successfully.")
