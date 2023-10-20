# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 11:51:58 2023

@author: alg16
"""


import pandas as pd
from seasonal import decompose



#we have to import matplotlib for create A graphique 
import matplotlib.pyplot as plt

#and add start year and end year 
start_year = 2020
end_year = 2022

file_name = 'My_Data.csv'
final_data = pd.read_csv(file_name)


#here start 
print("\n  ----------------- This is My Data ------------\n",final_data,"\n")

# Calcul de la moyenne mensuelle des ventes 
monthly_mean = final_data.groupby('Month')['Sales'].mean()

# Visualisation de la moyenne mensuelle des ventes
plt.figure(figsize=(10, 6))
plt.bar(monthly_mean.index, monthly_mean.values, color='skyblue')
plt.xlabel('Month')
plt.ylabel('Average Sales')
plt.title('Average Sales per Month')
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()