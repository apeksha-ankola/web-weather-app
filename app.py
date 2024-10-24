from flask import Flask, jsonify, render_template, request
import requests
import time
from dotenv import load_dotenv
import os
load_dotenv()


app = Flask(__name__)

API_KEY = os.getenv('OPENWEATHER_API_KEY')

# Simulated daily summary data
daily_summary = {
    'average_temp': 24,
    'max_temp': 30,
    'min_temp': 20
}

cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/weather/<city>')
def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather = {
            'city': city,
            'temp': round(data['main']['temp'] - 273.15, 2),  # Convert from Kelvin to Celsius
            'feels_like': round(data['main']['feels_like'] - 273.15, 2),
            'condition': data['weather'][0]['description'],
            'timestamp': time.time()
        }
        return jsonify(weather)
    else:
        return jsonify({'message': 'City not found', 'cod': '404'}), 404


@app.route('/api/daily-summary')
def get_daily_summary():
    return jsonify(daily_summary)


if __name__ == '__main__':
    app.run(debug=True)
