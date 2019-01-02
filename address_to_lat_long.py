from opencage.geocoder import OpenCageGeocode

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
