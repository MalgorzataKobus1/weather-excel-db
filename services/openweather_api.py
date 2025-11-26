from string.templatelib import convert

import requests
from datetime import datetime
from config import Config
from tools import  convert_to_celsius, ms_to_kmh


def fetch_weather():
    try:
        url=f"https://api.openweathermap.org/data/2.5/weather?q={Config.QUERY}&appid={Config.API_KEY}"
        res = requests.get(url)
        data = res.json()

        weather = {
            "temp" : convert_to_celsius(data["main"]["temp"]),
            "temp_feels_like" : convert_to_celsius(data["main"]["feels_like"]),
            "pressure" : data["main"]["pressure"],
            "humidity" : data["main"]["humidity"],
            "description" : data["weather"][0]["description"],
            "clouds" : data["clouds"]["all"],
            "place" : data["name"],
            "wind": ms_to_kmh(data["wind"]["speed"]),
            "cloudiness": data["clouds"]["all"],
            "timestamp": datetime.now().strftime("%H:%M:%S %d-%m-%Y")
        }
        return weather
    except Exception as e:
        print(e)


