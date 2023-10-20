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

# check messing value 
messing_value = final_data.isnull().sum()
print('\n\n number of messing value is\n')V
print(messing_value)

#using info() 
print("\n  ------------------ Information -------------------\n")
final_data.info()
