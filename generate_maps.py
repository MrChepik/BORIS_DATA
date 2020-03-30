#!/usr/bin/env python3
#-*-coding: utf-8-*-





import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library

!conda install -c conda-forge folium=0.5.0 --yes
import folium

print('Folium installed and imported!')

# define the world map
world_map = folium.Map()

# display world map
world_map

# define the world map centered around Canada with a low zoom level
world_map = folium.Map(location=[56.130, -106.35], zoom_start=4)

# display world map
world_map

# define the world map centered around Canada with a higher zoom level
world_map = folium.Map(location=[56.130, -106.35], zoom_start=8)

# display world map
world_map

# create a Stamen Toner map of the world centered around Canada
world_map = folium.Map(location=[56.130, -106.35], zoom_start=4, tiles='Stamen Toner')

# display map
world_map

# create a Stamen Toner map of the world centered around Canada
world_map = folium.Map(location=[56.130, -106.35], zoom_start=4, tiles='Stamen Terrain')

# display map
world_map

# create a world map with a Mapbox Bright style.
world_map = folium.Map(tiles='Mapbox Bright')

# display the map
world_map

df_incidents = pd.read_csv('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/Police_Department_Incidents_-_Previous_Year__2016_.csv')

print('Dataset downloaded and read into a pandas dataframe!')

df_incidents.head(7)

#Let's find out how many entries there are in our dataset.
df_incidents.shape

# get the first 100 crimes in the df_incidents dataframe
limit = 100
df_incidents = df_incidents.iloc[0:limit, :]

#Commit first 100 rows from incidents
df_incidents.shape

# San Francisco latitude and longitude values
san_fr_lat = 37.77
san_fr_lon = -122.42

# create map and display it
san_fr_map = folium.Map(location=[san_fr_lat, san_fr_lon], zoom_start=12)

# display the map of San Francisco
san_fr_map

# instantiate a feature group for the incidents in the dataframe
incidents = folium.map.FeatureGroup()

# loop through the 100 crimes and add each to the incidents feature group
for lat, lng, in zip(df_incidents.Y, df_incidents.X):
    incidents.add_child(
        folium.features.CircleMarker(
            [lat, lng],
            radius=5, # define how big you want the circle markers to be
            color='yellow',
            fill=True,
            fill_color='blue',
            fill_opacity=0.6
        )
    )

# add incidents to map
san_fr_map.add_child(incidents)



from folium import plugins

# let's start again with a clean copy of the map of San Francisco
san_fr_map = folium.Map(location = [san_fr_lat, san_fr_lon], zoom_start = 12)

# instantiate a mark cluster object for the incidents in the dataframe
incidents = plugins.MarkerCluster().add_to(san_fr_map)

# loop through the dataframe and add each data point to the mark cluster
for lat, lng, label, in zip(df_incidents.Y, df_incidents.X, df_incidents.Category):
    folium.Marker(
        location=[lat, lng],
        icon=None,
        popup=label,
    ).add_to(incidents)

# display map
san_fr_map




