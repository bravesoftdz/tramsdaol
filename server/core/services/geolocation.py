from inhoj.funcs import getni
from core.helpers import http_get, head_list


class GeoLocationGoogleService():

    def __raise_zero_results_(self, data):
        if getni(data, 'status') == 'ZERO_RESULTS':
            raise Exception('Address not found')
        
    def get_geographic_coordinate(self, address):
        url = f'http://maps.google.com/maps/api/geocode/json?address={address}'
        data = http_get(url)
        self.__raise_zero_results_(data)
        
        result = head_list(data['results'])
        φ, λ, full_address  = getni(result, 'geometry.location.lat'), getni(result, 'geometry.location.lng'), getni(result, 'formatted_address')
        return φ, λ, full_address
    

providers = {
    'google': GeoLocationGoogleService
}

def g (provider): return providers[provider]()