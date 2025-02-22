#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 17:54:32 2025

@author: finlaymichael
"""
import folium
import pandas as pd
df_schemes = pd.read_csv("repd_operational_data_with_closest_city.csv", encoding="latin1")
df_cities = pd.read_csv("gb_bng.csv")


# Create a base map centered on the UK
uk_map = folium.Map(location=[54.5, -2.5], zoom_start=6)

# Add markers for cities
for _, row in df_cities.iterrows():
    folium.Marker(
        location=[row["lat"], row["lng"]],
        popup=f"City: {row['city']}",
        icon=folium.Icon(color="blue", icon="info-sign"),
    ).add_to(uk_map)

# Add markers for renewable energy schemes
for _, row in df_schemes.iterrows():
    folium.Marker(
        location=[row["lat"], row["lng"]],
        popup=f"Scheme ID: {row.get('Scheme_ID', 'N/A')}<br>Closest City: {row['Closest_City']}",
        icon=folium.Icon(color="green", icon="leaf"),
    ).add_to(uk_map)

# Save the map to an HTML file
uk_map.save("uk_renewable_energy_map.html")

print("Map created and saved to 'uk_renewable_energy_map.html'. Open this file in a browser to view the map.")
