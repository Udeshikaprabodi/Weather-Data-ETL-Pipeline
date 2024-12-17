import pandas as pd
import psycopg2
import json

def load_data():
    with open('/path/to/config/db_config.json', 'r') as f:
        db_config = json.load(f)

    df = pd.read_csv('/tmp/transformed_weather_data.csv')

    connection = psycopg2.connect(
        host=db_config['host'],
        database=db_config['database'],
        user=db_config['user'],
        password=db_config['password']
    )
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather_data (
            city TEXT,
            temperature FLOAT,
            humidity INT,
            weather_description TEXT,
            timestamp BIGINT
        );
    ''')

    for _, row in df.iterrows():
        cursor.execute('''
            INSERT INTO weather_data (city, temperature, humidity, weather_description, timestamp)
            VALUES (%s, %s, %s, %s, %s);
        ''', (row['city'], row['temperature'], row['humidity'], row['weather_description'], row['timestamp']))

    connection.commit()
    cursor.close()
    connection.close()
    print("Weather data loaded into PostgreSQL successfully.")
