from datetime import datetime
from database.database import insert_weather_summary

def calculate_daily_summary(weather_data_collection):
    daily_summaries = {}
    
    for data in weather_data_collection:
        city = data['city']
        temp = data['temp']
        condition = data['condition']
        date = datetime.utcfromtimestamp(data['timestamp']).strftime('%Y-%m-%d')

        if city not in daily_summaries:
            daily_summaries[city] = {
                'total_temp': 0,
                'count': 0,
                'max_temp': temp,
                'min_temp': temp,
                'condition_count': {}
            }
        
        summary = daily_summaries[city]
        summary['total_temp'] += temp
        summary['count'] += 1
        summary['max_temp'] = max(summary['max_temp'], temp)
        summary['min_temp'] = min(summary['min_temp'], temp)
        summary['condition_count'][condition] = summary['condition_count'].get(condition, 0) + 1

    # Calculate and store daily averages and dominant conditions
    for city, summary in daily_summaries.items():
        avg_temp = summary['total_temp'] / summary['count']
        max_temp = summary['max_temp']
        min_temp = summary['min_temp']
        dominant_condition = max(summary['condition_count'], key=summary['condition_count'].get)

        # Store the daily summary in the database
        insert_weather_summary(city, date, avg_temp, max_temp, min_temp, dominant_condition)
        print(f"Stored summary for {city} on {date}: Avg: {avg_temp}, Max: {max_temp}, Min: {min_temp}, Condition: {dominant_condition}")
