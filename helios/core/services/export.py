import datetime
import json
import csv

from core.models import Track
from core.helpers import is_valid_ipv4

class ExportTracking():

    def __init__(self, format, ip_addres):
        self.format = format
        self.ip_addres = ip_addres

    def __get_file_name(self, extension):
        prefix = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        return f'{prefix}({self.ip_addres}).{extension}'

    def __save_file(self, content, extension):
        filename = self.__get_file_name(extension)
        with open(filename, 'w') as f:
            f.write(content)

    def __to_csv(self, data):
        filename = self.__get_file_name('csv')
        fieldnames =list(data[0].keys())
        with open(filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            [writer.writerow(d) for d in data]
           
    def __to_json(self, data):
        self.__save_file(json.dumps(data), 'json')

    def run(self, ):
        '''
        sdfsd
        '''

        format_map = {
            'csv': self.__to_csv,
            'json': self.__to_json,
        }

        ALLOWED_FORMATS = list(format_map.keys())

        if self.format not in ALLOWED_FORMATS:
            raise Exception(f'The {self.format} format is no recognised')

        if not is_valid_ipv4(self.ip_addres):
            raise Exception(f'The IP address {self.ip_addres} is invalid')

        tracks = Track.objects.filter(ip_address=self.ip_addres)
        data = [track.as_report() for track in tracks]

        if len(data) == 0:
            raise Exception('No  tracking found')

        format_map[self.format](data)

