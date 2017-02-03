from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from core.helper import track
from core.helper import get_file

class TemperatureView(ViewSet):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    def list(self, *args, **kwargs):

        address = self.request.GET.get('address', None)
        if not address:
            return Response('Invalid address', status=status.HTTP_400_BAD_REQUEST)

        data = {}

        track('192.168.0.1', address, data)

        return Response(data)


class ExportView(ViewSet):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    def list(self, *args, **kwargs):

        ALLOWED_FORMATS = ['csv', 'json']

        file_type = self.request.GET.get('file_type', None)
        if file_type not in ALLOWED_FORMATS:
            return Response('Invalid file type', status=status.HTTP_400_BAD_REQUEST)

        ip_addres = self.request.GET.get('ip_address', None)
        if not ip_addres:
            return Response('Invalid IP address', status=status.HTTP_400_BAD_REQUEST)

        data = get_file(file_type, ip_addres)

        return Response(data)