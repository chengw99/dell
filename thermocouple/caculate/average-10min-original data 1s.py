# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 21:10:58 2019

@author: DELL
"""

import numpy as np
import pandas as pd

ipath = r'E:\py_data\thermo'
opath = r'E:\py_output'
# data = pd.read_csv(ipath+'\\'+'data.csv',names=range(62)) #还奇怪为什么不能使用data.loc获取数据，之超声的程序就可以直接获取，才发现data读取的
#时候没有指定列的名字为数字， loc参数是标签名
# 注意 loc和iloc切片获取数据时有所不同，iloc是左闭右开的
data = pd.read_csv(ipath+'\\'+'data.csv')

l=[] # 仪器采集数据的间隔是3s，此处列表获取每分钟（最后一秒）对应的位置
for i in range(data.shape[0]):
    if i < (data.shape[0]-1):
        if data.iloc[i,1][11:16] == data.iloc[i+1,1][11:16]: # 相等即在同一分钟内，不相等则意味着出现了下一分钟
            pass
        else:
            l.append(i)
    else:
        pass

h=[] # 60个通道的平均温度数据
f=[] # 60个通道的通道号
for k in range(2,62):
    
    p=[] # 储存10min平均值
    for j in range(276):
        if j == 0:
            s = data.iloc[:l[9]+1,k]
            data_mean = np.sum(s.values)/np.float(len(s))
            p.append(data_mean)
        if 0<j<= 274:
            s = data.iloc[l[10*(j-1)+9]+1:l[10*j+9]+1,k]
            data_mean = np.sum(s.values)/np.float(len(s))
            p.append(data_mean)
        if j == 275:
            s = data.iloc[l[2749]+1:,k]
            data_mean = np.sum(s.values)/np.float(len(s))
            p.append(data_mean)  
    h.append(p)
    
    if 2<= k <=21:
        u = 100+k-1
        f.append(str(u))
    if 22<= k <=41:
        u = 200+k-21
        f.append(str(u))
    if 42<= k <=61:
        u = 300+k-41
        f.append(str(u))
    
t = np.array(h)
result = pd.DataFrame(t.T,columns=f)
result.to_csv(opath+'\\'+'10min-average temperature.csv')
    
   

'''
    # 分别生成60个通道的10min平均数据    
    
    result = pd.DataFrame({'Temperature':p})
    if 2<= k <=21:
        u = 100+k-1
        result.to_csv(opath+'\\'+str(u)+'.csv')
    if 22<= k <=41:
        u = 200+k-21
        result.to_csv(opath+'\\'+str(u)+'.csv')
    if 42<= k <=61:
        u = 300+k-41
        result.to_csv(opath+'\\'+str(u)+'.csv')
'''  



'''
# 此处是取1min平均的算法
p=[]
for j in range(len(l)+1):
    if j ==0:
        s = data.iloc[0:l[0]+1,2]
        data_mean = np.sum(s.values)/np.float(len(s))
        p.append(data_mean)
    if 0< j <= (len(l)-1):
        s = data.iloc[l[j-1]+1:l[j]+1,2]
        data_mean = np.sum(s.values)/np.float(len(s))
        p.append(data_mean)
    if j == len(l):
        s = data.iloc[l[-1]+1:,2]
        data_mean = np.sum(s.values)/np.float(len(s))
        p.append(data_mean)
    '''
'''
# 此处是取10min平均的算法
p=[]
for j in range(276):
    if j == 0:
        s = data.iloc[:l[9]+1,2]
        data_mean = np.sum(s.values)/np.float(len(s))
        p.append(data_mean)
    if 0<j<= 274:
        s = data.iloc[l[10*(j-1)+9]+1:l[10*j+9]+1,2]
        data_mean = np.sum(s.values)/np.float(len(s))
        p.append(data_mean)
    if j == 275:
        s = data.iloc[l[2749]+1:,2]
        data_mean = np.sum(s.values)/np.float(len(s))
        p.append(data_mean)
        '''