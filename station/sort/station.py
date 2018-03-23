# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 15:35:38 2018

@author: DELL
"""

#station
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

a = pd.read_csv(r'E:\py_data\station\20170511.csv')

data = a.ix[:,3]

tem = []
for i in range(24):
    data_mean = sum(data[i*6:i*6+6])/6.
    tem.append(data_mean)
    #原文件的时间序列不好提取，生成新的时间序列
time = []
for j in range(24):
    t = str(j) + ':00'
    time.append(t)
    
result = pd.DataFrame({'time':time,'Temperature':tem})
columns = ['time','Temperature']  #指定列的排列
result.to_csv('e:\\py_data\\station\\T_average_perhour_station.csv',columns = columns)