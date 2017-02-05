'''
This module implement a server side cache mechanisms to store API responses using databases

More details in: https://en.wikipedia.org/wiki/Cache_(computing)
'''

from core.models import Track, CacheResult, GeographicCoordinate, CacheValidResult
from django.contrib.postgres.search import SearchVector
from core.services.geolocation import g
from core.services.weather import w


def find_cache_geographic_coordinate(address):

    data = GeographicCoordinate.objects.annotate(search=SearchVector('address', 'search_address')).filter(search=address).first()
    if data:
        return data.lat, data.lng, data.address

    return None, None, None


def store_cache_geographic_coordinate(lat, lng, address, search_address):

    data = {
        'lat': lat,
        'lng': lng,
        'address': address,
        'search_address': search_address,
    }

    GeographicCoordinate.objects.create(**data)


def find_cache_temperature(lat, lng):

    data = CacheValidResult.objects.filter(lat=lat, lng=lng).first()
    if data:
        return data.result

    return None


def store_cache_temperature(lat, lng, data):
    CacheResult.objects.update_or_create(lat=lat, lng=lng, defaults={'result': data})


def search_temperature_by_address(search_address):
    """
    Search the temperature for a given address 

    Main rules
        Geographic Coordinate
            All known geographic coordinates are cached in the GeographicCoordinate table.
            Using Full Text Search the first step is to check if the address exists in the cache.
            If there is no, the Geolocation Service as called to search the new geographic 
            coordinates of a given address and store it in cache.
            
        Temperature 
            The operation is the same as the geographical coordinate, the result is cached in CacheResult table.
            The Weather Service is used to find the temperature data of the new address.
            The temperature caching is time-base check the seetings "CACHE_VALIDATION_TIME_MINUTES".

    """
    lat, lng, address = find_cache_geographic_coordinate(search_address)
    if not all((lat, lng, address)):
        lat, lng, address = g('google').get_geographic_coordinate(search_address)
        store_cache_geographic_coordinate(lat, lng, address, search_address)

    data = find_cache_temperature(lat, lng)
    if not data:
        city, country, degrees = w('openweathermap').get_temperature_by_geographic_coordinate(lat, lng)

        data = {
            'city': city,
            'country': country,
            'address': address,
            'degrees': degrees,
            'lat': lat,
            'lng': lng,
        }

        store_cache_temperature(lat, lng, data)

    return data
