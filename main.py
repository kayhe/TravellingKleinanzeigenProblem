#!/usr/bin/env python3

from src.gpshelpers import *
from src.kleinanzeigenhelpers import *
import argparse
import sys

parser = argparse.ArgumentParser(
        description='durchsucht Kleinanzeigen nach Inseraten entlang einer Route')
parser.add_argument('--route', required=True, help='gpx-Datei')
parser.add_argument('--keywords', help='Suchstichworte')

args = parser.parse_args()

trackpoints = clean_trackpoints(extract_trackpoints(args.route))
postcodes = set()

for point in trackpoints:
    postcode = coords_to_postal(point['lat'],point['lon'])
    postcodes.add(postcode)

for postcode in postcodes:
    print('Results for {}\n'.format(postcode))
    page = get_listings_page(args.keywords,postcode)
    items = extract_items(page)

    for item in items:
        print(item['title'] + " " + item['price'] + " -> " + item['url'])
    print('\n')
