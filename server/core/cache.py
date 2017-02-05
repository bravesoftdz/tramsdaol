from core.models import Track, CacheResult, GeographicCoordinate, CacheValidResult

from core.services.geolocation import g
from core.services.weather import w


def find_cache_geographic_coordinate(address):
    """
      Bla
    """

    data = GeographicCoordinate.objects.filter(address__search=address).first()
    if data:
        return data.lat, data.lng, data.address

    return None, None, None


def store_cache_geographic_coordinate(lat, lng, address):
    """
      Bla
    """

    data = {
        'lat': lat,
        'lng': lng,
        'address': address,
    }

    GeographicCoordinate.objects.create(**data)


def find_cache_temperature(lat, lng):
    """
      Bla
    """

    data = CacheValidResult.objects.filter(lat=lat, lng=lng).first()
    if data:
        return data.result

    return None


def store_cache_temperature(lat, lng, data):
    """
    Bla
    """

    CacheResult.objects.update_or_create(lat=lat, lng=lng, defaults={'result': data})


def search_temperature_by_address(search_address):
    """
    ds
    """

    lat, lng, address = find_cache_geographic_coordinate(search_address)
    if not all((lat, lng, address)):
        lat, lng, address = g('google').get_geographic_coordinate(search_address)
        store_cache_geographic_coordinate(lat, lng, address)

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
