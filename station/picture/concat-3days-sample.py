# -*- coding: utf-8 -*-
"""
Created on Fri May  4 10:52:03 2018

@author: DELL
"""

#此程序用于整个气象站连续三天的温度 -- 作为背景温度日循环画图数据
#先处理一个样例
import os
import numpy as np
import pandas as pd

fpath = r'C:\Users\DELL\Desktop\处理数据\按日期排序\station\north station\201705'
file = os.listdir(fpath)
os.chdir(fpath)
data1 = pd.read_csv(file[1])
data2 = pd.read_csv(file[2])
data3 = pd.read_csv(file[3])

y1 = data1.loc[:,'T_AIR']
y2 = data2.loc[:,'T_AIR']
y3 = data3.loc[:,'T_AIR']

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
            
result.to_csv(r'e:\py_output\test.csv',columns = columns)
        