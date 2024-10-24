import sqlite3

def create_connection():
    conn = sqlite3.connect('weather_data.db')  # Creates the database file if it doesn't exist
    return conn

def create_table():
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()

    # Create weather_summary table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather_summary (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT NOT NULL,
            date TEXT NOT NULL,
            avg_temp REAL,
            max_temp REAL,
            min_temp REAL,
            dominant_condition TEXT
        )
    ''')

    conn.commit()
    conn.close()

def insert_weather_summary(city, date, avg_temp, max_temp, min_temp, dominant_condition):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''INSERT INTO weather_summary (city, date, avg_temp, max_temp, min_temp, dominant_condition)
                      VALUES (?, ?, ?, ?, ?, ?)''', (city, date, avg_temp, max_temp, min_temp, dominant_condition))
    
    conn.commit()
    conn.close()
