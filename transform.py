import pandas as pd
from datetime import datetime

def transform_weather(raw_data):
    transformed = []

    for item in raw_data:
        row = {
            "city": item["name"],
            "country": item["sys"]["country"],
            "temperature": item["main"]["temp"],
            "feels_like": item["main"]["feels_like"],
            "humidity": item["main"]["humidity"],
            "weather_description": item["weather"][0]["description"],
            "wind_speed": item["wind"]["speed"],
            "recorded_at": datetime.utcnow()
        }
        transformed.append(row)

    df = pd.DataFrame(transformed)
    print(df)
    return df
