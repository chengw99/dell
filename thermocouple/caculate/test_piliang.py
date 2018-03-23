# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 09:00:22 2017

@author: DELL
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir('e:\py')

a = pd.read_csv('A.csv')
data_1 = a.ix[:,34]  #突然发现pandas行索引和列索引是有区别的，行索引的时候结束索引是被包含的，而列索引的结束索引是不被包含的
data2 = a.ix[:,35]   #连续读出4列数据的时候，变成列表的时候，4列数据会变成一个元素，打印到csv的时候就会在一个单元格里，所以分开了，这是第一种方法
data3 = a.ix[:,36]
data4 = a.ix[:,37]

tem1 = []
for i in range(24):
    data_mean_1 = sum(data_1[60*i:60*i+60])/60.
    tem1.append(data_mean_1)
tem2 = []
for i in range(24):
    data_mean2 = sum(data2[60*i:60*i+60])/60.
    tem2.append(data_mean2)
tem3 = []
for i in range(24):
    data_mean3 = sum(data3[60*i:60*i+60])/60.
    tem3.append(data_mean3)
tem4 = []
for i in range(24):
    data_mean4 = sum(data4[60*i:60*i+60])/60.
    tem4.append(data_mean4)
    
time = []
for j in range(24):
    t = str(j) + ':00'
    time.append(t)

result = pd.DataFrame({'time':time,'Temperature30cm':tem1,'Temperature60cm':tem2,'Temperature90cm':tem3,'Temperature110cm':tem4})
columns = ['time','Temperature30cm','Temperature60cm','Temperature90cm','Temperature110cm']  #这样可以指定列的顺序
result.to_csv('T_average_perhour.csv',columns = columns)