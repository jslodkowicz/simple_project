import requests

API_URL = 'http://api.openweathermap.org/data/2.5/'
KEY = open('.private.txt', 'r').read()[:-1]

CITY_URL = API_URL + 'weather?q={city_name}&APPID={key}&units=metric'
CIRCLE_URL = API_URL + 'find?lat={}&lon={}&cnt=10&APPID={key}'
RECTANGLE_ZONE_URL = API_URL + 'box/city?bbox={},{},{},{},{}&APPID={key}'
FORECAST_URL = API_URL + 'forecast?id={}&APPID={key}'

# zwraca aktualną pogodę we wskazanym mieście


def city_weather(city):
    data = requests.get(CITY_URL.format(city_name=city, key=KEY))
    return data.json()

# zwraca pogodę w 10 najbliższych miastach


def city_circle(coords):
    data = requests.get(CIRCLE_URL.format(*coords, key=KEY))
    return data.json()

# zwraca dane pogodowe w miastach w określonym promieniu


def rectangle_zone(coords):
    data = requests.get(RECTANGLE_ZONE_URL.format(
        *coords, 10, key=KEY))
    return data.json()

# zwraca dane pogodowe na najbliższe 5 dni w odstępach 3 godzinowych dla miasta


def forecast(id):
    data = requests.get(FORECAST_URL.format(
        id, key=KEY))
    return data.json()
