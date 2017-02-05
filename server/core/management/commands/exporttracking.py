from optparse import make_option
from django.core.management.base import BaseCommand, CommandError

from core.services.export import ExportTracking

from core.helpers import head_list


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('format', nargs='+', type=str, help='file format to export')
        parser.add_argument('ip', nargs='+', type=str, help='IP address filter')

    help = 'Export the tracking data to a file format of a given IP address'

    def handle(self, **options):
        ip_address = head_list(options['ip'])
        format_file = head_list(options['format'])

        export = ExportTracking(format_file, ip_address)
        export.run()

        print('Export Completed!')
