import sqlite3
import matplotlib.pyplot as plt

def plot_temperature_trends():
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()

    cursor.execute("SELECT city, date, avg_temp FROM weather_summary ORDER BY date")
    rows = cursor.fetchall()
    
    data_by_city = {}
    for row in rows:
        city, date, avg_temp = row
        if city not in data_by_city:
            data_by_city[city] = {'dates': [], 'temps': []}
        data_by_city[city]['dates'].append(date)
        data_by_city[city]['temps'].append(avg_temp)
    
    # Plot data for each city
    for city, data in data_by_city.items():
        plt.plot(data['dates'], data['temps'], label=city)
    
    plt.xlabel('Date')
    plt.ylabel('Average Temperature (°C)')
    plt.title('Temperature Trends')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

plot_temperature_trends()
