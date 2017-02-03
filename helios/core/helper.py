import requests
import json

from django.conf import settings
from inhoj.funcs import getni

from core.models import Track


def http_get(url: str) -> dict:
    
    response = requests.get(url)
    if not response.ok:
        response.raise_for_status()

    return json.loads(response.content.decode('utf-8'))


def find_address(address: str) -> str:
    
    url = f'http://maps.google.com/maps/api/geocode/json?address={address}'
    data = http_get(url)
    
    result = (data['results'] or [None])[0]
    
    return getni(result, 'formatted_address', fallback='')


def get_temperature(address: str) -> (str, str, float):
    
    appid = settings.OPENWEATHERMAP_API_KEY

    url = f'http://api.openweathermap.org/data/2.5/weather?q={address}&appid={appid}'
    data = http_get(url)
    
    if getni(data, 'cod') != 200:
        raise Exception(getni(data, 'message'))

    return getni(data, 'name'), getni(data, 'sys.country'), getni(data, 'main.temp') 

def to_csv(data: list):
    pass

def to_json(data: list):
    pass


def get_file_format(format: str, ip_addres: str) -> str:
    # TODO Indice por IP 
    tracks = Track.objects.filter(ip_address=ip_addres)
    return [ track.as_dict() for track in tracks]


def track(ip_address: str, term: str, result: str):
    Track.objects.create(ip_address=ip_address, term=term, result=result)
