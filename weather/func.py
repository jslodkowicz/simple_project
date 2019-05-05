from weather.url_requests import *
from weather.measurements import *

# pokazuje temperaturę, ciśnienie i zachmurzenie w mieście


def city_temp(city):
    data = city_weather(city)
    main = data['main']
    return '\nCurrent temperature in {} is {}°C, preassure: {} hPa, humidity: {}%'.format(city, main['temp'], main['pressure'], main['humidity'], key=KEY)
    return ['temp']


def rectangle_temp(city, x=1):
    data = rectangle_weather(city, x)
    dict = data['list']
    dict = {v['name']: v['main']['temp'] for v in data['list']}
    ma = ''.join([max(dict.items(), key=operator.itemgetter(1))[0]])
    mi = ''.join([min(dict.items(), key=operator.itemgetter(1))[0]])
    print(city_temp(city) + '\n')
    print(
        f'The warmest spot around is {ma}: {dict[ma]}°C, the coolest is {mi}: {dict[mi]}°C')


def rain_or_no(city):
    data = city_weather(city)
    data = data['weather'][0]['main'], data['weather'][0]['description']
    return f'Today in your city is {data[0]}, ({data[1]})'


def ask_for_temp():
    city = input('What city do you want to check?\n')
    return city_temp(city)


def ask_for_rectangle():
    city = input('Gdzie jesteś?\n\n>>> ')
    return rectangle_temp(city)


def forecast_weather(city):
    data = forecast_data(city)['list']
