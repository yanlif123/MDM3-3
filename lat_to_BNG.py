#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pandas as pd
from pyproj import Transformer

# Load the CSV file
df = pd.read_csv('gb.csv')

# Define the transformer for converting WGS84 (lat/lon) to BNG
transformer = Transformer.from_crs("EPSG:4326", "EPSG:27700", always_xy=True)

# Function to convert lat/lon to BNG
def convert_to_bng(lat, lng):
    easting, northing = transformer.transform(lng, lat)
    return easting, northing

# Apply the conversion to each row
df[['easting', 'northing']] = df.apply(lambda row: pd.Series(convert_to_bng(row['lat'], row['lng'])), axis=1)

# Save the updated DataFrame to a new CSV file
df.to_csv('gb_bng.csv', index=False)

print("Conversion complete. Data saved to 'gb_bng.csv'.")