#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 17:24:52 2025

@author: finlaymichael
"""

import pandas as pd
from pyproj import Transformer

# Load the CSV file
df = pd.read_csv('repd_operational_data.csv')

# Define the transformer for converting BNG (EPSG:27700) to WGS84 (EPSG:4326)
transformer = Transformer.from_crs("EPSG:27700", "EPSG:4326", always_xy=True)

# Function to convert BNG to latitude/longitude
def convert_to_lat_lng(easting, northing):
    longitude, latitude = transformer.transform(easting, northing)
    return latitude, longitude

# Apply the conversion to each row
df[['lat', 'lng']] = df.apply(lambda row: pd.Series(convert_to_lat_lng(row['X-coordinate'], row['Y-coordinate'])), axis=1)

# Save the updated DataFrame to a new CSV file
df.to_csv('repd_operational_data_latlng.csv', index=False)

print("Conversion complete. Data saved to 'repd_operational_data_latlng.csv'.")