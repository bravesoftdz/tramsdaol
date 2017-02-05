from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from ipware.ip import get_ip

from core.cache import search_temperature_by_address
from core.helpers import track


class TemperatureView(ViewSet):

    def __tracking(self, search_address, data):
        ip_address = get_ip(self.request)
        track(ip_address, search_address, data)

    def list(self, *args, **kwargs):
        '''
            Endpoint to call service to find temperature by address.

            The API responds with a match of the results including: 
                City;
                country;
                Full address;
                Temperature;
                Longitude;
                Latitude;

            It is necessary to inform the address

            Endpoint: /tempetarure?address="Any Address City"
        '''

        search_address = self.request.GET.get('address', None)
        if not search_address:
            return Response('Invalid address', status=status.HTTP_400_BAD_REQUEST)

        data = search_temperature_by_address(search_address)

        self.__tracking(search_address, data)

        return Response(data)
