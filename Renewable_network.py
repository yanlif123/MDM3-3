#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 16:10:12 2025

@author: finlaymichael
"""

import pandas as pd
import numpy as np
import folium
#import networkx as nx


df_schemes = pd.read_csv("repd_operational_data_latlng.csv", encoding="latin1")

#print(df.head())

df_cities = pd.read_csv("gb_bng.csv")
#extract relevant columns
df_cities = df_cities[["city","lat","lng"]] 

# Convert to a dictionary for easy access
cities = df_cities.set_index("city").to_dict(orient="index")

def find_closest_city(scheme_row, cities):
    """
    Find the closest city for a given renewable energy scheme.
    :param scheme_row: A row from the DataFrame representing a scheme.
    :param cities: Dictionary of cities with BNG coordinates.
    :return: Name of the closest city.
    """
    min_distance = float("inf")
    closest_city = None
    
    for city, coords in cities.items():
        distance = np.sqrt(
            (scheme_row["lng"] - coords["lng"]) ** 2 +
            (scheme_row["lat"] - coords["lat"]) ** 2
        )
        if distance < min_distance:
            min_distance = distance
            closest_city = city
    
    return closest_city

# Add a column for the closest city
df_schemes["Closest_City"] = df_schemes.apply(find_closest_city, cities=cities, axis=1)

df_schemes.to_csv("repd_operational_data_with_closest_city.csv", index=False)
























