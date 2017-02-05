import json
import requests

from django.conf import settings

from core.models import Track


class DictToObject:
    '''
    Contert a dict structure to allow acesse the keys by dot notation

    How to use:
        data = DictToObject(**{ 'pool': 32, 'message': 'Okay' })
        print(data.pool)
        print(data.message)

    References:
    http://stackoverflow.com/questions/1305532/convert-python-dict-to-object
    '''

    def __init__(self, **entries):
        self.__dict__.update(entries)


def http_get(url):
    '''
    Wrappper function to call the GET HTTP Method
    '''
    response = requests.get(url)
    if not response.ok:
        response.raise_for_status()

    return json.loads(response.content.decode('utf-8'))


def head_list(value):
    '''
    Gets the first element of list
    Inspired in https://lodash.com/docs#head
    '''
    return (value or [None])[0]


def track(ip_address, term, result):
    '''
    Track all requests in a database 
    '''
    if settings.ENABLED_DATA_TRACKING:
        Track.objects.create(ip_address=ip_address, term=term, result=result)


def is_valid_ipv4(ip):
    '''
        Validates IPv4 address
        This function was based in thread:
            - http://stackoverflow.com/questions/319279/how-to-validate-ip-address-in-python
    '''
    import re
    m = re.match(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)
    return bool(m) and all(map(lambda n: 0 <= int(n) <= 255, m.groups()))
