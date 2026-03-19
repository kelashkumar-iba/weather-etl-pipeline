import requests

API_KEY = "747d678a2ecfbc83d73437f85bcd602f"

CITIES = ["Karachi", "Lahore", "Islamabad"]

def extract_weather():
    all_data = []

    for city in CITIES:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        all_data.append(data)
        print(f"Extracted data for {city}")

    return all_data
