from django.conf import settings

from inhoj.funcs import getni
from core.helpers import http_get, head_list


class WeatherOpenWeatherMapService():

    def __raise_for_invalid_result(self, data):
        if getni(data, 'cod') != 200:
            raise Exception(getni(data, 'message'))

    def get_temperature_by_geographic_coordinate(self, latitude, longitude):

        appid = settings.OPENWEATHERMAP_API_KEY
        url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={appid}'
        data = http_get(url)

        self.__raise_for_invalid_result(data)
        city, country, degrees = getni(data, 'name'), getni(data, 'sys.country'), getni(data, 'main.temp')
        return city, country, degrees

providers = {
    'openweathermap': WeatherOpenWeatherMapService
}


def w(provider): return providers[provider]()
