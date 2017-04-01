"""
Calculate the optimal mapping of trucks to positions choosing the least distance

Note: The algorithm calculate and sum the smallest distance between the position of the truck and the original cargo and the smallest distance between the position of the original cargo and destination cargo

Python version: 3.6
"""

from google_maps import DistanceGoogleMaps
from helper import loadfile, chunkfy


if __name__ == '__main__':

    def get_distances(origins, destinations):
        distance = DistanceGoogleMaps()
        return distance.calculate(origins, destinations)

    def get_distances_truck_location_cargo_origin(items):

        origins = [o['truck_location'] for o in items]
        destinations = [d['cargo_origin'] for d in items]

        return get_distances(origins, destinations)

    def get_distances_cargo_origin_cargo_destination(items):

        origins = [o['cargo_origin'] for o in items]
        destinations = [d['cargo_destination'] for d in items]

        return get_distances(origins, destinations)

    def get_trucks_locations_x_cargo():
        """
        Return a map of truck location x cargo origin
        """
        result = []
        for truck in trucks:
            for cargo in cargos:
                result.append({
                    'truck_location': {'lat': truck['lat'], 'lng': truck['lng']},
                    'cargo_origin': {'lat': cargo['origin_lat'], 'lng': cargo['origin_lng']},
                    'cargo_destination': {'lat': cargo['destination_lat'], 'lng': cargo['destination_lng']},
                    'truck_display': truck['truck'],
                })
        return result

    cargos = loadfile('cargo.csv')
    trucks = loadfile('trucks.csv')

    # Map of all cargo routes and truck positions
    trucks_locations_x_cargo = get_trucks_locations_x_cargo()

    # In develpments mode send '3' record because the
    # Google Maps API return the OVER_QUERY_LIMIT error
    items = trucks_locations_x_cargo[:3]

    # Calculates the distance between the position of the truck and the origin
    # cargo
    distances_truck_location_to_cargo_origin = get_distances_truck_location_cargo_origin(
        items)
    # Calculates the distance between the position of the origin cargo and the
    # destination cargo
    distances_cargo_origin_cargo_destination = get_distances_cargo_origin_cargo_destination(
        items)

    for item, truck_location, cargo_distance in zip(
            items, distances_truck_location_to_cargo_origin, distances_cargo_origin_cargo_destination):

        truck = item['truck_display']
        cargo_origin = cargo_distance['origin']
        cargo_destination = cargo_distance['destination']
        distance = truck_location['distance'] + cargo_distance['distance']

        print(f'Ideal mapping for the {truck} truck')
        print(f'   Cargo: {cargo_origin} to {cargo_destination}')
        print(f'   Distance: {distance}')
        print('\n')
