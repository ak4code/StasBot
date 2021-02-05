import os
import requests
from dotenv import load_dotenv
load_dotenv()

CITIES = [
    {'name': 'Краснодар', 'lat': '45.044173', 'lon': '38.973035'},
    {'name': 'Темрюк', 'lat': '45.282955', 'lon': '37.365044'},
    {'name': 'Волна', 'lat': '45.128057', 'lon': '36.711721'},
]

condition = {
    'clear': 'ясно ☀',
    'partly-cloudy': 'малооблачно 🌤',
    'cloudy': 'облачно с прояснениями ⛅',
    'overcast': 'пасмурно ☁',
    'drizzle': 'морось 🌦',
    'light-rain': 'небольшой дождь 🌦',
    'rain': 'дождь 🌧',
    'moderate-rain': 'умеренно сильный дождь 🌧',
    'heavy-rain': 'сильный дождь 🌧',
    'continuous-heavy-rain': 'длительный сильный дождь 🌧',
    'showers': 'ливень 🌧',
    'wet-snow': 'дождь со снегом 🌨 + 🌧',
    'light-snow': 'небольшой снег 🌨',
    'snow': 'снег ❄',
    'snow-showers': 'снегопад ❄',
    'hail': 'град 🌨',
    'thunderstorm': 'гроза 🌩',
    'thunderstorm-with-rain': 'дождь с грозой ⛈',
    'thunderstorm-with-hail': 'гроза с градом 🌩 + 🌨',
}

wind_dir = {
    'nw': 'северо-западное',
    'n': 'северное',
    'ne': 'северо-восточное',
    'e': 'восточное',
    'se': 'юго-восточное',
    's': 'южное',
    'sw': 'юго-западное',
    'w': 'западное',
    'с': 'штиль',
}

headers = {'X-Yandex-API-Key': os.getenv("YW_API_KEY")}


def get_weather():
    forecasts = []
    weather = 'По данным Яндекс.Погоды\n\n'
    for city in CITIES:
        url = f"https://api.weather.yandex.ru/v2/forecast?lat={city.get('lat')}&lon={city.get('lon')}&limit=1&hours=0"
        r = requests.get(url, headers=headers)
        forecasts.append(r.json())
    if not forecasts:
        return "Нет данных по погоде!"
    for forecast in forecasts:
        weather += f"{forecast.get('geo_object').get('locality').get('name')}: {forecast.get('fact').get('temp')}°C ощущается как {forecast.get('fact').get('feels_like')}°C {condition.get(forecast.get('fact').get('condition'))}, направление ветра {wind_dir.get(forecast.get('fact').get('wind_dir'))} скорость {forecast.get('fact').get('wind_speed')}м/с.\n\n"
    return weather

def get_forecast():
    forecasts = []
    weather = 'Утрений пргноз на завтра. По данным Яндекс.Погоды\n\n'
    for city in CITIES:
        url = f"https://api.weather.yandex.ru/v2/forecast?lat={city.get('lat')}&lon={city.get('lon')}&limit=2&hours=0"
        r = requests.get(url, headers=headers)
        forecasts.append(r.json())
    if not forecasts:
        return "Нет данных по погоде!"
    for forecast in forecasts:
        weather += f"{forecast.get('geo_object').get('locality').get('name')}: {forecast.get('forecasts')[1].get('parts').get('morning').get('temp_avg')}°C ощущается как {forecast.get('forecasts')[1].get('parts').get('morning').get('feels_like')}°C {condition.get(forecast.get('fact').get('condition'))}, направление ветра {wind_dir.get(forecast.get('forecasts')[1].get('parts').get('morning').get('wind_dir'))} скорость {forecast.get('forecasts')[1].get('parts').get('morning').get('wind_speed')}м/с.\n\n"
    return weather