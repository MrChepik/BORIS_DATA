#-*-coding: utf-8 -*-

import pandas as pd
import numpy as np

crime_df = pd.read_csv('/home/boris/Downloads/Police_Department_Incidents_-_Previous_Year__2016_.csv') 

crime_df.head(10)

crime_df.rename(columns={'PdDistrict': 'Neighbors'}, inplace=True)

total_crime_df = crime_df['Neighbors'].value_counts().to_frame()

total_crime_df.rename(columns={'Neighbors': 'Total'}, inplace=True)
total_crime_df.index.name = 'Neighbors'

total_crime_df.head(100)


