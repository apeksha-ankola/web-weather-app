# Real-Time Weather Monitoring System

## Overview
This project is a Real-Time Weather Monitoring System that fetches weather data for multiple cities using the OpenWeatherMap API. It aggregates and summarizes weather data daily, calculating metrics such as average temperature, maximum temperature, minimum temperature, and the dominant weather condition. The results are stored in a SQLite database for further analysis.

## Technologies Used
- Python
- Requests library for API calls
- SQLite for database management
- dotenv for environment variable management

## Installation

### Prerequisites
- Python 3.x
- SQLite
- Required Python packages:
  - requests
  - python-dotenv

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
2. Install the required packages:
   ```
   pip install -r requirements.txt
   pip install python-dotenv
   ```
3. Create a .env file in the root directory and add your OpenWeatherMap API key:
   ``` OPENWEATHER_API_KEY=your_api_key_here  ```
   also add the api key in main.js which is in the folder static.
   
5. Run the application in 2 different terminals
  ```
  python weather_monitor.py
  python app.py 
  ```
# Frontend Installation Steps: Open index.html from templates folder, in your preferred web browser.

# Database Schema
# The database consists of a single table named weather_summary with the following columns:

```id ```: Auto-incremented primary key.
```city ```: Name of the city.
```date```: Date of the weather data.
```avg_temp```: Average temperature for the day.
```max_temp```: Maximum temperature for the day.
```min_temp```: Minimum temperature for the day.
```dominant_condition```: The most frequent weather condition for the day.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
