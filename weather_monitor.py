import requests
import time
from datetime import datetime
from weather_aggregator import calculate_daily_summary
from database.database import create_table, insert_weather_summary
create_table()
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.getenv('OPENWEATHER_API_KEY')
CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]
INTERVAL = 3000  # 5 minutes

# Function to fetch weather data from the OpenWeatherMap API
def fetch_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        weather_data = {
            'city': city,
            'temp': data['main']['temp'] - 273.15,  # Convert from Kelvin to Celsius
            'feels_like': data['main']['feels_like'] - 273.15,
            'condition': data['weather'][0]['main'],
            'timestamp': data['dt']
        }
        return weather_data
    else:
        print(f"Error fetching data for {city}: {response.status_code}")
        return None

# Job to run every 5 minutes
ALERT_THRESHOLD = 35  # Temperature threshold in Celsius
consecutive_alert_count = {city: 0 for city in CITIES}

def check_alert(city, temp):
    global consecutive_alert_count
    if temp > ALERT_THRESHOLD:
        consecutive_alert_count[city] += 1
        if consecutive_alert_count[city] >= 2:
            print(f"ALERT: {city} has exceeded {ALERT_THRESHOLD}°C for two consecutive updates!")
    else:
        consecutive_alert_count[city] = 0  # Reset alert count if condition isn't met

def job():
    weather_data_collection = []
    for city in CITIES:
        weather_data = fetch_weather_data(city)
        if weather_data:
            print(weather_data)
            weather_data_collection.append(weather_data)

            # Check alert condition
            check_alert(city, weather_data['temp'])

    # Calculate daily summary
    calculate_daily_summary(weather_data_collection)


# Continuous loop to fetch weather data at intervals
while True:
    job()
    time.sleep(INTERVAL)
