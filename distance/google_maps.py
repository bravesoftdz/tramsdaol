"""
Calculate the min driving distance between two coordinates using Google Distance Matrix API

Find out more at https://developers.google.com/maps/documentation/distance-matrix/

References:
    https://developers.google.com/maps/documentation/distance-matrix/intro
    http://stackoverflow.com/questions/6211127/to-calculate-driving-distance-between-two-coordinates-on-earth-in-php
"""

import time

from helper import http_get
from helper import loadfile
from helper import head_list, chunkfy
from inhoj.funcs import getni


class DistanceGoogleMaps():

    def __statis_is_valid(self, status):
        if status != 'OK':
            raise Exception(status)

    def __check_elements(self, elements):
        if len(elements) == 0:
            raise Exception('Zero results in elements')

    def __check_valid_elements(self, elements):
        if len(elements) == 0:
            raise Exception('Zero results in valid elements')

    def __get_elements(self, origins, destinations):

        mode = 'driving'
        sensor = 'false'

        origin = '|'.join([str(o['lat']) + ',' + o['lng'] for o in origins])
        destination = '|'.join([str(o['lat']) + ',' + o['lng']
                                for o in destinations])

        url = f'http://maps.googleapis.com/maps/api/distancematrix/json?origins={origin}&destinations={destination}&mode={mode}&sensor={sensor}'

        data = http_get(url)

        # Check if response contains a valid result
        self.__statis_is_valid(getni(data, 'status'))

        destination_addresses = getni(data, 'destination_addresses')
        origin_addresses = getni(data, 'origin_addresses')
        rows = getni(data, 'rows')

        elements = []

        for i, (d, o) in enumerate(
                zip(destination_addresses, origin_addresses)):

            # Group elements by index
            distances = [r['elements'][i] for r in rows]
            # Find shortest distance between multiple destinations
            best_distance = min(
                distances, key=lambda e: getni(
                    e, 'distance.value'))

            elements.append({
                'destination': d,
                'origin': o,
                'distance': getni(best_distance, 'distance.value'),
            })

        return elements

    def calculate(self, origins, destinations):
        """
        Given a list of latitude/longitude of locations returns information based on the recommended route between start and end points, as calculated by the Google Maps API

        Example:
            origins = [ {'lat': 23.4455, 'lng': 54.67567}, {'lat': 34.4455, 'lng': 87.67567} ]
            destination = [ {'lat': 1.4455, 'lng': 63.67567}, {'lat': 81.4455, 'lng': 98.67567} ]

            distance = DistanceGoogleMaps()
            distance.calculate(origins, destinations)

        Paramenters
            origins: list of latitude/longitude for origin locations


            destinations: list of latitude/longitude for destination locations
        """

        elements = self.__get_elements(origins, destinations)
        return elements
