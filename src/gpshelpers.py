from bs4 import BeautifulSoup
import math
import requests

def coords_to_postal(lat,lon):
    req = requests.get('https://nominatim.openstreetmap.org/reverse',
            {'format' : 'jsonv2', 'lat' : str(lat), 'lon' : str(lon)})
    if req.status_code != requests.codes.ok:
        raise Exception('failed to convert coordinates to postal codes')

    return req.json()['address']['postcode']

def coords_distance(lat1, lon1, lat2, lon2):
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlamb = math.radians(lon2 - lon1)

    a = math.sin(dphi/2) * math.sin(dphi/2) + math.cos(phi1) * math.cos(phi2) \
        * math.sin(dlamb/2) * math.sin(dlamb/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    distance = 6371 * c
    return distance

def extract_trackpoints(gpxfile):
    trackpoints = []
    soup = BeautifulSoup(open(gpxfile).read(),'xml')
    for trackpoint in soup.find_all('trkpt'):
        point = { 'lat' : float(trackpoint.attrs['lat']),
                  'lon' : float(trackpoint.attrs['lon']) }
        trackpoints.append(point)
    
    if len(trackpoints) == 0:
        raise ValueError('No trackpoints found in gpx file')
    return trackpoints

def clean_trackpoints(trackpoints):
    new_trackpoints = [trackpoints[0]]
    for point in trackpoints:
        reference = new_trackpoints[-1]
        if coords_distance(point['lat'], point['lon'], reference['lat'], reference['lon']) < 10:
            pass
        else:
            new_trackpoints.append(point)

    return new_trackpoints
