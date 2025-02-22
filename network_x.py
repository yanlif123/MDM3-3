#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 18:27:44 2025

@author: finlaymichael
"""

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load the datasets
df_schemes = pd.read_csv("repd_operational_data_with_closest_city.csv", encoding="latin1")
df_cities = pd.read_csv("gb_bng.csv")

# Aggregate capacities for each city
city_capacities = df_schemes.groupby("Closest_City")["Installed Capacity (MWelec)"].sum().reset_index()
city_capacities.rename(columns={"Installed Capacity (MWelec)": "Total_Capacity"}, inplace=True)

# Merge capacities with the cities dataset
df_cities = pd.merge(df_cities, city_capacities, left_on="city", right_on="Closest_City", how="left")

# Fill NaN values with 0 (cities with no schemes) without using inplace=True
df_cities["Total_Capacity"] = df_cities["Total_Capacity"].fillna(0)

# Create a graph
G = nx.Graph()

# Add cities as nodes with capacity attributes
for _, row in df_cities.iterrows():
    G.add_node(
        row["city"],
        pos=(row["lng"], row["lat"]),  # Geographical position
        capacity=row["Total_Capacity"]  # Total capacity of schemes
    )

# Draw the graph
pos = nx.get_node_attributes(G, "pos")  # Get positions from node attributes
node_sizes = [G.nodes[city]["capacity"] * 10 for city in G.nodes]  # Scale node size for visibility
node_colors = [G.nodes[city]["capacity"] for city in G.nodes]  # Use capacity for node color

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=node_sizes,
    node_color=node_colors,
    cmap=plt.cm.Blues,  # Color map for node colors
    font_size=8,
    edge_color="gray"
)

# Add a color bar to show capacity values
sm = plt.cm.ScalarMappable(cmap=plt.cm.Blues, norm=plt.Normalize(vmin=min(node_colors), vmax=max(node_colors)))
sm.set_array([])
plt.colorbar(sm, label="Total Capacity (MWelec)")

# Show the graph
plt.title("Cities and Renewable Energy Scheme Capacities")
plt.show()