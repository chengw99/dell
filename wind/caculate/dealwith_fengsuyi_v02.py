# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 19:23:37 2018

@author: DELL
"""

import os
import pandas as pd
import datetime

starttime = datetime.datetime.now()
#long running
#do something other
os.chdir('e:\py_data\wind')

data = pd.read_csv('20170609.csv',names = range(11))

l=[]
p=[]
for j in range(0,24):
    if j < 10:
        
        for k in range(0,60):
            if k < 10:
                for i in range(0,60):
                    if i < 10:
                        try:
                            a = '0' + str(j) + ':0' + str(k) + ':0' + str(i)
                            #print(a)
                            u = data[data.ix[:,1] == a].index.tolist()
                            #l.append(u) 如果将此命令放在这里，那l里面会增加空列表
                            #加上条件筛选后，可以去掉空列表
                            if len(u) == 0:
                                print('无数据',a)
                            else:
                                l.append(u)
                                data_mean = sum(data.ix[u[0]:u[-1],3])/float(len(u))
                                p.append(data_mean)
                        except:
                            pass
                
                    else:
                        try:
                            b = '0' + str(j) + ':0' + str(k) + ':' + str(i)
                            #print(b)
                            u = data[data.ix[:,1] == b].index.tolist()
                        
                        
                            if len(u) == 0:
                                print('无数据',b)
                            
                            else:
                                l.append(u)
                                data_mean = sum(data.ix[u[0]:u[-1],3])/float(len(u))
                                p.append(data_mean)
                            
                        except:
                            pass
           
            
            else:
                for i in range(0,60):
                    if i < 10:
                        try:
                            a = '0' + str(j) + ':' + str(k) + ':0' + str(i)
                            #print(a)
                            u = data[data.ix[:,1] == a].index.tolist()
                        
                        
                            if len(u) == 0:
                                print('无数据',a)
                            else:
                                l.append(u)
                                data_mean = sum(data.ix[u[0]:u[-1],3])/float(len(u))
                                p.append(data_mean)
                            
                        except:
                            pass
                
                    else:
                        try:
                            b = '0' + str(j) + ':' + str(k) + ':' + str(i)
                            #print(b)
                            u = data[data.ix[:,1] == b].index.tolist()
                        
                        
                            if len(u) == 0:
                                print('无数据',b)
                            else:
                                l.append(u)
                                data_mean = sum(data.ix[u[0]:u[-1],3])/float(len(u))
                                p.append(data_mean)
                            
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
                            u = data[data.ix[:,1] == a].index.tolist()
                            #l.append(u) 如果将此命令放在这里，那l里面会增加空列表
                            #加上条件筛选后，可以去掉空列表
                            if len(u) == 0:
                                print('无数据',a)
                            else:
                                l.append(u)
                                data_mean = sum(data.ix[u[0]:u[-1],3])/float(len(u))
                                p.append(data_mean)
                        except:
                            pass
                
                    else:
                        try:
                            b = str(j) + ':0' + str(k) + ':' + str(i)
                            #print(b)
                            u = data[data.ix[:,1] == b].index.tolist()
                        
                        
                            if len(u) == 0:
                                print('无数据',b)
                            
                            else:
                                l.append(u)
                                data_mean = sum(data.ix[u[0]:u[-1],3])/float(len(u))
                                p.append(data_mean)
                            
                        except:
                            pass
           
            
            else:
                for i in range(0,60):
                    if i < 10:
                        try:
                            a = str(j) + ':' + str(k) + ':0' + str(i)
                            #print(a)
                            u = data[data.ix[:,1] == a].index.tolist()
                        
                        
                            if len(u) == 0:
                                print('无数据',a)
                            else:
                                l.append(u)
                                data_mean = sum(data.ix[u[0]:u[-1],3])/float(len(u))
                                p.append(data_mean)
                            
                        except:
                            pass
                
                    else:
                        try:
                            b = str(j) + ':' + str(k) + ':' + str(i)
                            #print(b)
                            u = data[data.ix[:,1] == b].index.tolist()
                        
                        
                            if len(u) == 0:
                                print('无数据',b)
                            else:
                                l.append(u)
                                data_mean = sum(data.ix[u[0]:u[-1],3])/float(len(u))
                                p.append(data_mean)
                            
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
print((endtime - starttime).seconds)
