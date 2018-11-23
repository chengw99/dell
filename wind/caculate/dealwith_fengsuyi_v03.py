# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 19:23:37 2018

@author: DELL
"""
# 此程序用于计算超声风速仪数据，获取24小时风速的秒平均（1秒有20个左右数据，对这20个数据进行平均，作为1秒的数据，但有时并不是1秒产生20个数据，需要进行判断
# 程序运行时间太长，在尝试速度变得更快,可以先处理一小时的数据，看哪种方式更快
# 将python内置函数sum修改为np.sum()，将ix修改为iloc,ix选择数据时效率比较低下

import numpy as np
import pandas as pd

import datetime

starttime = datetime.datetime.now()
#long running
#do something other
ipath = r'e:\py_data\wind'

data = pd.read_csv(ipath+'\\'+ '20170511.csv',names = range(11))


l=[] 
p=[]
for j in range(0,1):
    if j < 10:
        
        for k in range(0,60):
            if k < 10:
                for i in range(0,60):
                    if i < 10:
                        try:
                            a = '0' + str(j) + ':0' + str(k) + ':0' + str(i)
                            #print(a)
                            u = data[data.loc[:,1] == a].index.tolist()
                            #l.append(u) 如果将此命令放在这里，那l里面会增加空列表
                            #加上条件筛选后，可以去掉空列表
                            if len(u) == 0:
                                print('无数据:',a)
                            else:
                                l.append(u)
                                data_mean = np.sum(data.loc[u[0]:u[-1],3])/float(len(u))
                                p.append(data_mean)
                                print('Now is:',a)
                        except:
                            pass
                
                    else:
                        try:
                            b = '0' + str(j) + ':0' + str(k) + ':' + str(i)
                            #print(b)
                            u = data[data.loc[:,1] == b].index.tolist()
                        
                        
                            if len(u) == 0:
                                print('无数据',b)
                            
                            else:
                                l.append(u)
                                data_mean = np.sum(data.loc[u[0]:u[-1],3])/float(len(u))
                                p.append(data_mean)
                                print('Now is:',b)
                            
                        except:
                            pass
           
            
            else:
                for i in range(0,60):
                    if i < 10:
                        try:
                            a = '0' + str(j) + ':' + str(k) + ':0' + str(i)
                            #print(a)
                            u = data[data.loc[:,1] == a].index.tolist()
                        
                        
                            if len(u) == 0:
                                print('无数据',a)
                            else:
                                l.append(u)
                                data_mean = np.sum(data.loc[u[0]:u[-1],3])/float(len(u))
                                p.append(data_mean)
                                print('Now is:',a)
                            
                        except:
                            pass
                
                    else:
                        try:
                            b = '0' + str(j) + ':' + str(k) + ':' + str(i)
                            #print(b)
                            u = data[data.loc[:,1] == b].index.tolist()
                        
                        
                            if len(u) == 0:
                                print('无数据',b)
                            else:
                                l.append(u)
                                data_mean = np.sum(data.loc[u[0]:u[-1],3])/float(len(u))
                                p.append(data_mean)
                                print('Now is:',b)
                            
                        except:
                            pass
                        
                        
    else:
         for k in range(0,60):
            if k < 10:
                for i in range(0,60):
                    if i < 10:
                        try:
                            a = str(j) + ':0' + str(k) + ':0' + str(i)
                            #print(a)
                            u = data[data.loc[:,1] == a].index.tolist()
                            #l.append(u) 如果将此命令放在这里，那l里面会增加空列表
                            #加上条件筛选后，可以去掉空列表
                            if len(u) == 0:
                                print('无数据',a)
                            else:
                                l.append(u)
                                data_mean = np.sum(data.loc[u[0]:u[-1],3])/float(len(u))
                                p.append(data_mean)
                                print('Now is:',a)
                        except:
                            pass
                
                    else:
                        try:
                            b = str(j) + ':0' + str(k) + ':' + str(i)
                            #print(b)
                            u = data[data.loc[:,1] == b].index.tolist()
                        
                        
                            if len(u) == 0:
                                print('无数据',b)
                            
                            else:
                                l.append(u)
                                data_mean = np.sum(data.loc[u[0]:u[-1],3])/float(len(u))
                                p.append(data_mean)
                                print('Now is:',b)
                            
                        except:
                            pass
           
            
            else:
                for i in range(0,60):
                    if i < 10:
                        try:
                            a = str(j) + ':' + str(k) + ':0' + str(i)
                            #print(a)
                            u = data[data.loc[:,1] == a].index.tolist()
                        
                        
                            if len(u) == 0:
                                print('无数据',a)
                            else:
                                l.append(u)
                                data_mean = np.sum(data.loc[u[0]:u[-1],3])/float(len(u))
                                p.append(data_mean)
                                print('Now is:',a)
                            
                        except:
                            pass
                
                    else:
                        try:
                            b = str(j) + ':' + str(k) + ':' + str(i)
                            #print(b)
                            u = data[data.loc[:,1] == b].index.tolist()
                        
                        
                            if len(u) == 0:
                                print('无数据',b)
                            else:
                                l.append(u)
                                data_mean = np.sum(data.loc[u[0]:u[-1],3])/float(len(u))
                                p.append(data_mean)
                                print('Now is:',b)
                            
                        except:
                            pass







q = 0   
w = 0                 
for t in l:
    
    if len(t) == 0:
        q = q + 1
    elif len(t) != 0:
        w = w + 1
        
    
print('空列表个数:',q) #l.append(u) 的位置换了之后就可以不统计空列表的个数了
print('有数据个数:',w)
endtime = datetime.datetime.now()
T = endtime - starttime
print('The time you need to run: {0}s'.format(T.seconds)) # 程序运行时间，单位秒
print('The time you need to run:{0}min'.format(T.seconds/60))
result = pd.DataFrame(p)
result.to_csv(r'e:\py_output\v03.csv')

# 运行时间 513s