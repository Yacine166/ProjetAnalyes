# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 11:51:58 2023

@author: alg16
"""

import pandas as pd
import calendar
import random

start_year = 2020
end_year = 2022

# Generate data for each year
data_all_year = []
for year in range(start_year,end_year + 1 ):
    print(f"------------------- this for year {year}----------------")

    # Generate monthly sales data for the year
    months = [calendar.month_name[i] for i in range(1, 13)]
    sales = [random.randint(5000, 20000) for _ in range(12)]  # Random sales for each month

    # Create a DataFrame for the year
    yearly_data = pd.DataFrame({'Year': [year] *12, 'Month': months, 'Sales': sales})
    data_all_year.append(yearly_data)
    print(yearly_data)
    
# Concatenate data for the specified years
final_data = pd.concat(data_all_year, ignore_index=True)
file_name = 'My_Data.csv'
final_data.to_csv(file_name, index=False)
print("The data has been saved to '", file_name,"'\n\n")
