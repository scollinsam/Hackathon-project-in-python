from opencage.geocoder import OpenCageGeocode
from pprint import pprint


def address_to_coordinates(address):

    key = '4745929c7204418da8d7bd0b0b693a69'
    geocoder = OpenCageGeocode(key)

    query = address
    results = geocoder.geocode(query)

    # print(u'%f, %f' % (results[0]['geometry']['lat'],
    #                         results[0]['geometry']['lng']))

    latitude = results[0]['geometry']['lat']
    longitude = results[0]['geometry']['lng']

    return latitude, longitude


def coordinates_to_address(latitude, longitude):

    key = '4745929c7204418da8d7bd0b0b693a69'
    geocoder = OpenCageGeocode(key)

    results = geocoder.reverse_geocode(latitude, longitude)
    # pprint(results)
    return results

coordinates_to_address(27.1750151,78.0421552)