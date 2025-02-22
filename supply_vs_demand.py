#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 14:38:54 2025

@author: finlaymichael
"""

import pandas as pd

df = pd.read_csv('repd_operational_data_latlng.csv')

demand_data = {
    'Eastern': 23526500,  
    'East Midlands': 18683700,
    'London': 34641800,
    'North East': 9905500,
    'North West': 27196900,
    'South East': 34544200,
    'South West': 20994500,
    'West Midlands': 21383800,
    'Yorkshire and Humber': 20549800,
    'Scotland': 21420600,
    'Wales': 13114100,
    'Northern Ireland': 7141000
} #doesnt include unallocated consumption data

region_supply = df.groupby('Region')['Installed Capacity (MWelec)'].sum()

print(region_supply.sum())

total_demand_mwh = sum(demand_data.values())

print(f"Total Energy Demand: {total_demand_mwh}")