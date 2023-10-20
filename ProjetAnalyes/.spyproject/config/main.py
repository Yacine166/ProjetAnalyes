# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 11:51:58 2023

@author: alg16
"""

import pandas as pd
import calendar
import random

#we have to import matplotlib for create A graphique 
import matplotlib.pyplot as plt

#and add start year and end year 
start_year = 2020
end_year = 2022

file_name = 'My_Data.csv'
final_data = pd.read_csv(file_name)


#here start 
print("\n  ----------------- This is My Data ------------\n",final_data,"\n")


# Calculate the moving average
window_size = 5  # Adjust the window size as needed
final_data['Moving_Avg'] = final_data['Sales'].rolling(window=window_size).mean()

# Visualize the trend using the moving average
plt.figure(figsize=(13, 6))
for year in range(start_year, end_year+1):
    year_data = final_data[final_data['Year'] == year]
    plt.plot(year_data['Month'], year_data['Moving_Avg'], label=f'Moving Average for Year {year}')

plt.xlabel('Month')
plt.ylabel('Moving Average of Sales')
plt.title('Trend of Sales using Moving Average')
plt.legend()
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()
print(final_data)