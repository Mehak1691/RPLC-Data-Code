# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 10:43:20 2021

@author: 60199
"""

import pandas as pd
import numpy as np
df = pd.read_csv('C:/Users/60199/Desktop/Annotated Data/Luminosity_Iteration900_HUNDERED.csv')

    
df['Comparison']=df['Label(Machine)']== df['Label(Human)']
df.to_csv('Luminosity_Iteration900_HUNDERED.csv', header=True)
#print(df['comparison1'][1])

TotalTrueCount=0
for i in range(0,300):
    if(df['Comparison'][i]==True):
        print("true inside")
        TotalTrueCount= TotalTrueCount+1
totalnumber=len((df['Label(Machine)']))    
TotalEfficiency=TotalTrueCount/totalnumber*100

print(f'The total efficiency is :{TotalEfficiency}')

total_matching_D = len(df[(df['Label(Machine)'] == 'D') & (df['Label(Human)'] =='D')])
total_dark = len(df[(df['Label(Human)'] =='D')])

# print(f"Total matching: {total_matching_D}")
# print(f"Total dark: {total_dark}")

D_Efficiency = (total_matching_D / total_dark) * 100  
print(f'The Dark efficiency is :{D_Efficiency}')
# print(df['Label(Human) Converted'].values)'



total_matching_S = len(df[(df['Label(Machine)'] == 'S') & (df['Label(Human)'] =='S')])
total_S = len(df[(df['Label(Human)'] =='S')])


S_Efficiency = (total_matching_S / total_S) * 100  

print(f'The Semi efficiency is :{S_Efficiency}')



total_matching_B = len(df[(df['Label(Machine)'] == 'B') & (df['Label(Human)'] =='B')])
total_B = len(df[(df['Label(Human)'] =='B')])


B_Efficiency = (total_matching_B / total_B) * 100  

print(f'The Bright efficiency is :{B_Efficiency}')