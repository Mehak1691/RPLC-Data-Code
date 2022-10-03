# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 10:27:12 2021

@author: 60199
"""

import glob
import cv2
import math
import numpy as np
from PIL import Image
from tqdm import tqdm
import json
import os
import pandas as pd

lis=[]

def maximum(a, b, c): 
  
    if (a >= b) and (a >= c): 
        largest = 'D'
  
    elif (b >= a) and (b >= c): 
        largest = 'S'
    else: 
        largest = 'B'
          
    return largest 


path = glob.glob('C:/Users/Manzoor2/Desktop/1Kimages/*/*')
#C:\Users\Manzoor2\Desktop\1Kimages


print("The paths have been globbed")
for name in tqdm(path):
    # print(f'Name is:{name}')
    img = cv2.imread(name)
    img=cv2.resize(img,(100,100))
    B,G,R = cv2.split(img)

    Barr = np.asarray(B)
    Garr = np.asarray(G)
    Rarr = np.asarray(R)
    
    dark = 0
    semidark = 0
    bright = 0
    
    Luminance = (((Rarr * 0.2126) + (Garr * 0.7152) + (Barr * 0.0722)) /255 )
    print(f'Luminance is:{Luminance.shape}')
    new_arr = []
    for arr in tqdm(Luminance):
        new_arr.extend(arr)

    for i in new_arr:
        if(i<=0.09):
            dark+=1
        
        if(i >0.09) and (i<=0.47):
            semidark+=1
        
        if(i>0.47) and (i <=1):
            bright+=1
            
#         print(f'The Luminance is:{new_arr[i]}'
    label = maximum(dark,semidark,bright)



    lavg = np.mean(Luminance)
    print(f'Average luminance is:{lavg}')
    
    print(f'Dark count is:{dark}')
    print(f'Semi Dark count is:{semidark}')
    print(f'Bright count is:{bright}')
    print(f'Label is: {label}')
    
    # lis.append(lavg)
    dic={'Image Name':os.path.basename(name), 'Dark Count': dark, 'Semi Dark Count': semidark , 'Bright Count':bright, 'Label':label}
    lis.append(dic)
df = pd.DataFrame(lis)
print(df.columns)

#df.to_csv("/content/gdrive/My Drive//Luminosity_Iteration4.csv", header=True)
df.to_csv('Luminosity_Iteration1k-100by100.csv', header=True)