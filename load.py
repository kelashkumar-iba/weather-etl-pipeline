import psycopg2
from psycopg2.extras import execute_values

DB_CONFIG = {
    "host": "localhost",
    "database": "weather_db",
    "user": "postgres",
    "password": "kelash123"
}

def load_weather(df):
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()

    rows = [
        (
            row["city"],
            row["country"],
            row["temperature"],
            row["feels_like"],
            row["humidity"],
            row["weather_description"],
            row["wind_speed"],
            row["recorded_at"]
        )
        for row in df.to_dict(orient="records")
    ]

    execute_values(cursor, """
        INSERT INTO weather_data 
        (city, country, temperature, feels_like, humidity, weather_description, wind_speed, recorded_at)
        VALUES %s
    """, rows)

    conn.commit()
    cursor.close()
    conn.close()
    print(f"Loaded {len(rows)} rows into PostgreSQL")
