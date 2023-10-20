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

# Descriptive analysis of monthly sales
monthly_stats = final_data.groupby('Month')['Sales'].describe()
print('\n  --------------- Analyse des ventes------------- \n')
print("Descriptive statistics for monthly sales:\n", monthly_stats,"\n")


# Time series plot for monthly sales
plt.figure(figsize=(12, 6))
for year in range(start_year, end_year+1):
    year_data = final_data[final_data['Year'] == year]
    plt.plot(year_data['Month'], year_data['Sales'], label=f'Year {year}')

plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales Over Time')
plt.legend()
plt.xticks(rotation=30)
plt.yticks(rotation=30)
plt.tight_layout()
plt.show()
