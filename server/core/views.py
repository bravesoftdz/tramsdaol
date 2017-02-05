from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from core.cache import search_temperature_by_address
from core.helpers import track


class TemperatureView(ViewSet):

    def list(self, *args, **kwargs):

        search_address = self.request.GET.get('address', None)
        if not search_address:
            return Response('Invalid address', status=status.HTTP_400_BAD_REQUEST)

        data = search_temperature_by_address(search_address)
        track('192.168.0.1', search_address, data)

        return Response(data)
