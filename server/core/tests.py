import unittest

from django.test import TestCase
from django.test.utils import override_settings

from core.cache import search_temperature_by_address
from core.helpers import head_list, is_valid_ipv4, track, DictToObject

from core.services.weather import w
from core.services.geolocation import g


class TestGeoLocationGoogleService(unittest.TestCase):

    @unittest.mock.patch('core.services.geolocation.http_get')
    def test_get_geographic_coordinate(self, http_get_method):

        data = {
            'status': 'OK',
            'results': [{
                'formatted_address': 'Sao Miguel do Oeste - SC, Brasil',
                'geometry': {
                    'location': {
                        'lat': -26.7246898,
                        'lng': -53.5167812,
                    }
                }
            }]
        }

        http_get_method.return_value = data

        lat, lng, full_address = g(
            'google').get_geographic_coordinate('Sao Miguel do Oeste')

        http_get_method.assert_called_with(
            'http://maps.google.com/maps/api/geocode/json?address=Sao Miguel do Oeste')

        self.assertEqual(lat, -26.7246898)
        self.assertEqual(lng, -53.5167812)
        self.assertEqual(full_address, 'Sao Miguel do Oeste - SC, Brasil')

    @unittest.mock.patch('core.services.geolocation.http_get')
    def test_get_geographic_coordinate_with_zero_results(self, http_get_method):

        data = {
            'status': 'ZERO_RESULTS',
            'results': [],
        }

        http_get_method.return_value = data

        with self.assertRaises(Exception) as ex:
            _, _, _ = g('google').get_geographic_coordinate('Guaratabarutata')

            http_get_method.assert_called_with(
                'http://maps.google.com/maps/api/geocode/json?address=Sao Miguel do Oeste')

        self.assertEqual(str(ex.exception), 'Address not found')


class TestWeatherOpenWeatherMapService(unittest.TestCase):

    @unittest.mock.patch('core.services.weather.http_get')
    @override_settings(OPENWEATHERMAP_API_KEY='1234567abcdefg')
    def test_get_weather(self, http_get_method):

        data = {
            'name': 'Barra Bonita',
            'cod': 200,
            'sys': {
                'country': 'BR',
            },
            'main': {
                'temp': 234.65
            }
        }

        http_get_method.return_value = data

        city, country, degrees = w(
            'openweathermap').get_temperature_by_geographic_coordinate(-23.53534345, -50.345345)
        http_get_method.assert_called_with(
            'http://api.openweathermap.org/data/2.5/weather?lat=-23.53534345&lon=-50.345345&appid=1234567abcdefg')

        self.assertEqual(city, 'Barra Bonita')
        self.assertEqual(country, 'BR')
        self.assertEqual(degrees, 234.65)

    @unittest.mock.patch('core.services.weather.http_get')
    @override_settings(OPENWEATHERMAP_API_KEY='1234567abcdefg')
    def test_get_weather_exception(self, http_get_method):

        data = {
            'message': 'City not found',
            'cod': 400,

        }

        http_get_method.return_value = data

        with self.assertRaises(Exception) as ex:
            _, _, _ = w(
                'openweathermap').get_temperature_by_geographic_coordinate(-3.23, -5.54)

            http_get_method.assert_called_with(
                'http://api.openweathermap.org/data/2.5/weather?lat=--3.23&lon=--5.54&appid=1234567abcdefg')

        self.assertEqual(str(ex.exception), 'City not found')


class TestHelperMethods(unittest.TestCase):

    def test_dict_to_object(self):
        object_data = DictToObject(**{'name': 'Veia do What', 'age': 98})
        self.assertEqual(object_data.name, 'Veia do What')
        self.assertEqual(object_data.age, 98)

    def test_head_list(self):
        list_numbers = [{'data': 12}, {'data': 22}, ]
        self.assertEqual(head_list(list_numbers), {'data': 12})

    def test_head_list_none_list(self):
        list_numbers = None
        self.assertEqual(head_list(list_numbers), None)

    def test_valid_ips(self):
        ips = [
            '1.6.7.8',
            '12.22.22.22',
            '123.122.98.76',
            '1.22.111.124',
        ]
        for ip in ips:
            self.assertTrue(is_valid_ipv4(ip), ip)

    def test_invalid_ips(self):
        ips = [
            '1222.6222.711.81',
            '1211.22.22.22',
            '123.666.234.076',
            '1777.22.111',
            '1777.22.',
            '1777.22.111.dede',
            '.0.0.0',
        ]
        for ip in ips:
            self.assertFalse(is_valid_ipv4(ip), ip)

    @unittest.mock.patch('core.models.Track.objects.create')
    def test_track_request(self, create_method):
        track('192.168.0.1', 'Palhoça', {'city': 'Palhoça', 'country': 'BR'})
        create_method.assert_called_with(ip_address='192.168.0.1', term='Palhoça',  result={
                                         'city': 'Palhoça', 'country': 'BR'})

    @unittest.mock.patch('core.models.Track.objects.create')
    @override_settings(ENABLED_DATA_TRACKING=False)
    def test_untrack_request(self, create_method):
        track('192.168.0.1', 'Palhoça', {'city': 'Palhoça', 'country': 'BR'})
        self.assertFalse(create_method.called)


class TestCacheRules(unittest.TestCase):

    @unittest.mock.patch('core.models.CacheResult.objects.create')
    @unittest.mock.patch('core.services.weather.WeatherOpenWeatherMapService.get_temperature_by_geographic_coordinate')
    @unittest.mock.patch('core.models.GeographicCoordinate.objects.create')
    @unittest.mock.patch('core.services.geolocation.GeoLocationGoogleService.get_geographic_coordinate')
    @unittest.mock.patch('core.models.GeographicCoordinate.objects.filter')
    @unittest.mock.patch('core.models.CacheValidResult.objects.filter')
    def test_full_cache(self, cache_filter_method, geo_filter_method, google_geo_method, goo_create_method, owm_weather_method, cache_create):
        """
            Temperatura e Corrdebas esta cahcedas
        """

        geo_data = DictToObject(
            **{'lat': -98.98, 'lng': -12.87, 'address': 'Campeche, Florianópolis'})
        geo_filter_method.return_value.first.return_value = geo_data

        cache_data = DictToObject(**{'result': {
            'city': 'Florianópolis',
            'country': 'BR',
            'address': 'Campeche, Florianópolis, Brazil',
            'degrees': 340.65,
            'lat': -98.98,
            'lng': -12.87,
        }})

        cache_filter_method.return_value.first.return_value = cache_data

        data = search_temperature_by_address('Campeche, FLorianópolis')

        cache_filter_method.assert_called_with(lat=-98.98, lng=-12.87)
        self.assertFalse(google_geo_method.called)
        self.assertFalse(goo_create_method.called)

        geo_filter_method.assert_called_with(
            address__search='Campeche, FLorianópolis')
        self.assertFalse(owm_weather_method.called)
        self.assertFalse(cache_create.called)

        self.assertDictEqual(cache_data.result, data)

    @unittest.mock.patch('core.models.CacheResult.objects.update_or_create')
    @unittest.mock.patch('core.services.weather.WeatherOpenWeatherMapService.get_temperature_by_geographic_coordinate')
    @unittest.mock.patch('core.models.GeographicCoordinate.objects.create')
    @unittest.mock.patch('core.services.geolocation.GeoLocationGoogleService.get_geographic_coordinate')
    @unittest.mock.patch('core.models.GeographicCoordinate.objects.filter')
    @unittest.mock.patch('core.models.CacheValidResult.objects.filter')
    def test_without_cache(self, cache_filter_method, geo_filter_method, google_geo_method, goo_create_method, owm_weather_method, cache_create):
        """
            Temperatura e Corrdebas esta cahcedas
        """

        expected_data = {
            'city': 'Florianópolis',
            'country': 'BR',
            'address': 'Jurerê, FLorianópolis, Brazil',
            'degrees': 89.12,
            'lat': -12.55,
            'lng': -90.54,
        }

        geo_filter_method.return_value.first.return_value = None
        cache_filter_method.return_value.first.return_value = None

        google_geo_method.return_value = (-12.55, -
                                          90.54, 'Jurerê, FLorianópolis, Brazil')
        owm_weather_method.return_value = ('Florianópolis', 'BR', 89.12)

        data = search_temperature_by_address('Jurerê, FLorianópolis')

        geo_filter_method.assert_called_with(
            address__search='Jurerê, FLorianópolis')
        google_geo_method.assert_called_with('Jurerê, FLorianópolis')
        goo_create_method.assert_called_with(
            lat=-12.55, lng=-90.54, address='Jurerê, FLorianópolis, Brazil')

        cache_filter_method.assert_called_with(lat=-12.55, lng=-90.54)
        owm_weather_method.assert_called_with(-12.55, -90.54)
        cache_create.assert_called_with(
            lat=-12.55, lng=-90.54, defaults={'result': expected_data})

        self.assertDictEqual(expected_data, data)

    @unittest.mock.patch('core.models.CacheResult.objects.update_or_create')
    @unittest.mock.patch('core.services.weather.WeatherOpenWeatherMapService.get_temperature_by_geographic_coordinate')
    @unittest.mock.patch('core.models.GeographicCoordinate.objects.create')
    @unittest.mock.patch('core.services.geolocation.GeoLocationGoogleService.get_geographic_coordinate')
    @unittest.mock.patch('core.models.GeographicCoordinate.objects.filter')
    @unittest.mock.patch('core.models.CacheValidResult.objects.filter')
    def test_geographic_coordinate_cache(self, cache_filter_method, geo_filter_method, google_geo_method, goo_create_method, owm_weather_method, cache_create):

        expected_data = {
            'city': 'Florianópolis',
            'country': 'BR',
            'address': 'Lagoa, Florianópolis, Brazil',
            'degrees': 103.12,
            'lat': -98.9812,
            'lng': -12.8721,
        }

        geo_data = DictToObject(
            **{'lat': -98.9812, 'lng': -12.8721, 'address': 'Lagoa, Florianópolis, Brazil'})
        geo_filter_method.return_value.first.return_value = geo_data
        cache_filter_method.return_value.first.return_value = None

        owm_weather_method.return_value = ('Florianópolis', 'BR', 103.12)

        data = search_temperature_by_address('Lagoa, FLorianópolis')

        geo_filter_method.assert_called_with(
            address__search='Lagoa, FLorianópolis')
        self.assertFalse(goo_create_method.called)
        self.assertFalse(google_geo_method.called)

        cache_filter_method.assert_called_with(lat=-98.9812, lng=-12.8721)
        owm_weather_method.assert_called_with(-98.9812, -12.8721)

        cache_create.assert_called_with(
            lat=-98.9812, lng=-12.8721, defaults={'result': expected_data})

        self.assertDictEqual(expected_data, data)

    @unittest.mock.patch('core.models.CacheResult.objects.create')
    @unittest.mock.patch('core.services.weather.WeatherOpenWeatherMapService.get_temperature_by_geographic_coordinate')
    @unittest.mock.patch('core.models.GeographicCoordinate.objects.create')
    @unittest.mock.patch('core.services.geolocation.GeoLocationGoogleService.get_geographic_coordinate')
    @unittest.mock.patch('core.models.GeographicCoordinate.objects.filter')
    @unittest.mock.patch('core.models.CacheValidResult.objects.filter')
    def test_temperature_cache(self, cache_filter_method, geo_filter_method, google_geo_method, goo_create_method, owm_weather_method, cache_create):

        geo_filter_method.return_value.first.return_value = None

        cache_data = DictToObject(**{'result': {
            'city': 'Florianópolis',
            'country': 'BR',
            'address': 'Pantanal, Florianópolis, Brazil',
            'degrees': 409.65,
            'lat': 2.9328,
            'lng': 32.46822,
        }})
        cache_filter_method.return_value.first.return_value = cache_data

        google_geo_method.return_value = (
            2.9328, 32.46822, 'Pantanal, FLorianópolis, Brazil')

        data = search_temperature_by_address('Pantanal, FLorianópolis')

        geo_filter_method.assert_called_with(
            address__search='Pantanal, FLorianópolis')
        google_geo_method.assert_called_with('Pantanal, FLorianópolis')
        goo_create_method.assert_called_with(
            lat=2.9328, lng=32.46822, address='Pantanal, FLorianópolis, Brazil')

        cache_filter_method.assert_called_with(lat=2.9328, lng=32.46822)
        self.assertFalse(owm_weather_method.called)
        self.assertFalse(cache_create.called)

        self.assertDictEqual(cache_data.result, data)


if __name__ == '__main__':
    unittest.main()
