# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 11:51:58 2023

@author: alg16
"""

import pandas as pd
import calendar
import random


file_name = 'My_Data.csv'
final_data = pd.read_csv(file_name)


#here start 
print("\n  ----------------- This is My Data ------------\n",final_data,"\n")

# Descriptive analysis of monthly sales
monthly_stats = final_data.groupby('Month')['Sales'].describe()
print('\n  --------------- Analyse des ventes------------- \n')
print("Descriptive statistics for monthly sales:\n", monthly_stats)


#using info() 
print("\n  ------------------ Information -------------------\n")
final_data.info()