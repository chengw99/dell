# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 21:51:56 2018

@author: DELL
"""

#对热电偶取10分钟平均

import pandas as pd
import numpy as np



data = pd.read_csv(r'e:\py_data\thermo\A-20170511.csv')

a = data.ix[:,32]

tem = []
for i in range(144):
    
    data_mean = sum(a[10*i:10*i+10])/10.
    tem.append(data_mean)

time = []
for i in range(24):
    for j in np.linspace(0,60,num = 6,endpoint = False):
        if j == 0:
            time.append(str(int(i))+':0'+str(int(j)))
        else:
            time.append(str(int(i))+':'+str(int(j)))
            
result = pd.DataFrame({'time':time,'Temperature':tem})
columns = ['time','Temperature']
result.to_csv('e:\py_output\T_average_10min-A20170511.csv',columns = columns)