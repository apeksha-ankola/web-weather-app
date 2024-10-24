import pytest
from weather_monitor import fetch_weather_data
from weather_aggregator import calculate_daily_summary

# Test data retrieval from API
def test_fetch_weather_data():
    city = "Delhi"
    data = fetch_weather_data(city)
    assert data is not None
    assert 'temp' in data
    assert 'condition' in data

# Test temperature conversion (Kelvin to Celsius)
def test_temperature_conversion():
    data = fetch_weather_data("Delhi")
    kelvin_temp = data['temp'] + 273.15
    assert kelvin_temp - 273.15 == data['temp']

# Test daily weather summary calculation
def test_daily_summary():
    weather_data_collection = [
        {'city': 'Delhi', 'temp': 25, 'condition': 'Clear', 'timestamp': 1729714169},
        {'city': 'Delhi', 'temp': 28, 'condition': 'Clear', 'timestamp': 1729715169},
        {'city': 'Delhi', 'temp': 23, 'condition': 'Rain', 'timestamp': 1729716169},
    ]
    calculate_daily_summary(weather_data_collection)
