# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 16:55:05 2018

@author: DELL
"""

# 此程序用于计算超声风速仪数据
# 仪器1s内可能产生20左右个数据，需要用程序进行判断，然后对同一秒内的数据进行平均，获取得到的数据为秒平均数据

import numpy as np
import pandas as pd
import datetime

starttime = datetime.datetime.now()
ipath = r'e:\py_data\wind'
opath = r'e:\py_output'

data = pd.read_csv(ipath+'\\'+'20170511.csv',names=range(11))
l=[]
for i in range(data.shape[0]): # 72061对应的是 '01:00:00'，这里的数据范围只算了1个小时，做个测试
    
    
    if i < (data.shape[0]-1):
        if data.loc[i,1] == data.loc[i+1,1]:
            pass
        else:
            l.append(i)
            
    else:
        pass
    
p=[]
for j in range(len(l)+1):
    if j == 0:
        s = data.loc[0:l[0],3]
        data_mean = np.sum(s.values)/np.float(len(s))
        p.append(data_mean)
        print('Now is',data.loc[l[0],1])
    if 0< j <= (len(l)-1):
        s = data.loc[l[j-1]+1:l[j],3]
        data_mean = np.sum(s.values)/np.float(len(s))
        p.append(data_mean)
        print('Now is',data.loc[l[j],1])
    if j == len(l):
        s = data.loc[l[-1]+1:,3]
        data_mean = np.sum(s.values)/np.float(len(s))
        p.append(data_mean)
        print('Now is',data.loc[l[-1]+1,1])
result = pd.DataFrame(p)
result.to_csv(opath+'\\'+'wind speed-1s-20170511.csv')         
      
endtime = datetime.datetime.now()

print('The time you need is {0}s'.format((endtime - starttime).seconds)) # 此程序运行时间是 93s