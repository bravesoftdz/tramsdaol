import json
import requests

from django.conf import settings

from core.models import Track


class DictToObject:
    '''

        http://stackoverflow.com/questions/1305532/convert-python-dict-to-object
    '''

    def __init__(self, **entries):
        self.__dict__.update(entries)


def http_get(url):
    '''
        blblbl
    '''
    response = requests.get(url)
    if not response.ok:
        response.raise_for_status()

    return json.loads(response.content.decode('utf-8'))


def head_list(value):
    '''
        blblbl
    '''
    return (value or [None])[0]


def track(ip_address, term, result):
    '''
        blblbl
    '''
    if settings.ENABLED_DATA_TRACKING:
        Track.objects.create(ip_address=ip_address, term=term, result=result)


def is_valid_ipv4(ip):
    '''
        Validates IPv4 addresses
        This function was based in thread:
            - http://stackoverflow.com/questions/319279/how-to-validate-ip-address-in-python
    '''
    import re
    m = re.match(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)
    return bool(m) and all(map(lambda n: 0 <= int(n) <= 255, m.groups()))
