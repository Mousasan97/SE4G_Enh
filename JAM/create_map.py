# -*- coding: utf-8 -*-
"""
Created on Sat May 29 01:09:04 2021

@author: Juanfra
"""
import pandas as pd
import geopandas as gpd
import folium
from folium.plugins import MarkerCluster
from get_data_ep5 import update_req_ep5


def map_():
    
    data_geodf=update_req_ep5()
    
    m = folium.Map(location=[45.46, 9.19], zoom_start=13)
    
    marker_cluster = MarkerCluster().add_to(m)
    
    for indice, row in data_geodf.iterrows():
        folium.Marker(
            location=[row["lon"], row["lat"]],
            popup=row['7_Classify_the_distr'],
            icon=folium.map.Icon(color='red')
        ).add_to(marker_cluster)
    
    tiles = ['stamenwatercolor', 'cartodbpositron', 'openstreetmap', 'stamenterrain']
    
    for tile in tiles:
        
        folium.TileLayer(tile).add_to(m)
    
    #########            fill_color="YlGnBu",
             ####            ).add_to(m)
    
    folium.LayerControl().add_to(m)

    m.save('templates/map_outp.html')