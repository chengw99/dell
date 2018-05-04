# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 14:51:44 2018

@author: DELL
"""

import os
import numpy as np
import pandas as pd

file = os.listdir(r'C:\Users\DELL\Desktop\处理数据\picture\thermo\日循环\20170518-20170520\Initial data\90cm\F')
os.chdir(r'C:\Users\DELL\Desktop\处理数据\picture\thermo\日循环\20170518-20170520\Initial data\90cm\F')
data1 = pd.read_csv(file[0])
data2 = pd.read_csv(file[1])
data3 = pd.read_csv(file[2])
y1 = data1.iloc[:,2]
y2 = data2.iloc[:,2]
y3 = data3.iloc[:,2]
            
y = pd.concat([y1,y2,y3])
time=[]
for i in range(72):
    for j in np.linspace(0,60,num = 6,endpoint = False):
        if j == 0:
            time.append(str(int(i))+':0'+str(int(j)))
        else:
            time.append(str(int(i))+':'+str(int(j)))

result = pd.DataFrame({'Temperature':y,'time':time})
columns = ['time','Temperature']
            
result.to_csv(r'e:\py_output\F-90.csv',columns = columns)
        