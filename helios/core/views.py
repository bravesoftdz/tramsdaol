from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from core.services.geolocation import g
from core.services.weather import w

from core.helpers import track
# from core.helper import get_file

class TemperatureView(ViewSet):
    """
    """

    def list(self, *args, **kwargs):

        address = self.request.GET.get('address', None)
        if not address:
            return Response('Invalid address', status=status.HTTP_400_BAD_REQUEST)

        # Verifica se existe longitue de latiure para o endereós espeficidao
        # se nao tiver consulta e atualiza
    
        verifica se para a longitue e latirue existe chahe de 1 hora na temperaute
        
        lat, lng, address =  g('google').get_geographic_coordinate(address)
        city, country, degrees = w('openweathermap').get_temperature_by_geographic_coordinate(lat, lng)
        
        data = {
            'city': city,
            'country': country,
            'address': address,
            'degrees': degrees,
            'lat': lat,
            'lng': lng,
        } 

        # track('192.168.0.1', address, data)

        return Response(data)
