#!/usr/bin/env python3

from src.gpshelpers import *
from src.kleinanzeigenhelpers import *
from src.htmloutput import OutputSoup
import argparse

parser = argparse.ArgumentParser(
    description='durchsucht Kleinanzeigen nach Inseraten entlang einer Route')
parser.add_argument('--route', required=True, help='gpx-Datei')
parser.add_argument('--keywords', help='Suchstichworte')

args = parser.parse_args()

trackpoints = clean_trackpoints(extract_trackpoints(args.route))
postcodes = set()

for point in trackpoints:
    postcode = coords_to_postal(point['lat'], point['lon'])
    postcodes.add(postcode)

output = OutputSoup()

for postcode in sorted(postcodes):
    page = get_listings_page(args.keywords, postcode)
    items = extract_items(page)
    output.add_all_items(items, postcode)

print(output.prettify())
