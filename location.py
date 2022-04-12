import requests

# needs error handling - can't connect to server, invalid URL, invalid request, response unexpected format...

def get_location(city, country):

    # remove the key and read it from an environment variable, or your keys file 
    # A dictionary of query parameters is much more readable than one line line 
    response = requests.get(f'https://api.mapbox.com/geocoding/v5/mapbox.places/{city},{country}.json?access_token=pk.eyJ1IjoibWFuZGlibGVjbGF3IiwiYSI6ImNrNmxpcWJ4MzBhamozZXBiZzVoNm11cmgifQ.lt7or9puZArJpANdrnIrUg').json()

    return response
    # returns values as a tuple. city is element 0, country is 1

def get_longitude_latitude(location_data): # this is used for the other APIs  

    longitude = float(location_data['features'][0]['center'][0])

    latitude = float(location_data['features'][0]['center'][1])

    return longitude, latitude

def location_main(city, country):

    location_data = get_location(city, country)

    longitude, latitude = get_longitude_latitude(location_data)

    return longitude, latitude
