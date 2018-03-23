# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 21:39:01 2017

@author: DELL
"""

import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

os.chdir('e:\py_data\wind')

data = pd.read_csv('try.csv',names = range(11))

#a = data.ix[2:21,4]

x = np.arange(160)

l=[]
p=[]
for j in range(20,21):
    for k in range(27,28):
        if k < 10:
            for i in range(0,20):
                if i < 10:
                    try:
                        a = str(j) + ':0' + str(k) + ':0' + str(i)
                        print(a)
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
                        print(b)
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
            for i in range(0,22):
                if i < 10:
                    try:
                        a = str(j) + ':' + str(k) + ':0' + str(i)
                        print(a)
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
                        print(b)
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
                        
'''                       
for i in range(20):
    if i < 10:
        a = '20:27:0'+str(i)
        print(a)
        u = data[data.ix[:,1] == a].index.tolist()
        print(i)
        l.append(u)
        
    else:
        b = '20:27:'+str(i)
        print(b)
        u = data[data.ix[:,1] == b].index.tolist()
        print(i)
        l.append(u)
'''



'''
z = 0.0

fig = plt.figure()
ax = fig.add_subplot(1,1,1)


plt.xlim(0,160)
plt.ylim(-0.6,0.6)
plt.xlabel('time(s)',fontsize = 12)
plt.ylabel('wind speed (m/s)',rotation = 90,fontsize = 12)
xticks = ax.set_xticks([0,20,40,60,80,100,120,140,160])  #此命令行可以确定x轴标签的位置
xlabels = ax.set_xticklabels(['0','1','2','3','4','5','6','7','8']) 
plt.minorticks_on()

plt.plot(x,-u,'gD-',markersize = 2.5,markerfacecolor = 'none',linewidth = 1,label = 'vertical speed')
#plt.plot(x,x*z,'r--',linewidth = 2)

#街谷内垂直向上的风速
#plt.plot(x,-u,linewidth =1,label = 'vertical speed')
#街谷内沿着
#plt.plot(x,w,linewidth = 1,label = 'speed of w')
plt.plot(x,x*z,'r--',linewidth = 2)



plt.grid(True,linestyle='--')
plt.legend(loc = 'best',fontsize = 12) # frameon = False 可去掉图例边框

plt.show()
'''