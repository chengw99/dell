# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 09:46:02 2018

@author: DELL
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


os.chdir('e:\py_output')
#画图-不同高度
#读取数据
#B中空模型1：1  
#A装沙模型2：1  
#C中空模型3:1  
#D装沙模型3:1  
#E装沙模型1:1  
#F中空模型2:1
data1 = pd.read_csv('e:\\py_data\\pic\\T_average_perhour_C30.csv')
data2 = pd.read_csv('e:\\py_data\\pic\\T_average_perhour_C60.csv') 
data3 = pd.read_csv('e:\\py_data\\pic\\T_average_perhour_C90.csv') 
data4 = pd.read_csv('e:\\py_data\\pic\\T_average_perhour_C110.csv')
#------------------------------------------------------------------------------
x = np.arange(24)
y1 = data1.ix[:,2]
y2 = data2.ix[:,2]
y3 = data3.ix[:,2]
y4 = data4.ix[:,2]
    
fig = plt.figure()
ax = fig.add_subplot(1,1,1)  #貌似引入这个才可以调用后面的方法set_xticks

#plt.plot(x,y1,'ko-',linewidth = 1.5,label = 'sand south model facing north(H/W=1,h=0.3m)')
#plt.plot(x,y2,'rs-',linewidth = 1.5,label = 'sand south model facing north(H/W=1,h=0.6m)')
#plt.plot(x,y3,'b^-',linewidth = 1.5,label = 'sand south model facing north(H/W=1,h=0.9m)')
#plt.plot(x,y4,'mv-',linewidth = 1.5,label = 'sand south model facing north(H/W=1,h=1.1m)')

plt.plot(x,y1,'ko-',linewidth = 1.5,label = 'empty south model facing north(H/W=3,h=0.3m)')
plt.plot(x,y2,'rs-',linewidth = 1.5,label = 'empty south model facing north(H/W=3,h=0.6m)')
plt.plot(x,y3,'b^-',linewidth = 1.5,label = 'empty south model facing north(H/W=3,h=0.9m)')
plt.plot(x,y4,'mv-',linewidth = 1.5,label = 'empty south model facing north(H/W=3,h=1.1m)')

#plt.plot(x,y1,'ko-',linewidth = 1.5,label = 'sand model south model facing north(H/W=2,h=1.44m)') 
#plt.plot(x,y2,'rs-',linewidth = 1.5,label = 'sand model air temperature-N(H/W=3,h=1,44m)')
#plt.plot(x,y3,'b^-',linewidth = 1.5,label = 'sand model air temperature-S(H/W=3,h=1.44m)')
#plt.plot(x,y4,'mv-',linewidth = 1.5,label = 'sand model air temperature(H/W=1,h=1.44m)')

plt.xlim(0,24) #表示x轴的范围设置为0到24
plt.ylim(22,45)
plt.xlabel('time')
plt.ylabel('T(℃)',rotation = 90)
xticks = ax.set_xticks([0,4,8,12,16,20,24])  #此命令行可以确定x轴标签的位置
xlabels = ax.set_xticklabels(['0:00','4:00','8:00','12:00','16:00','20:00','24:00'])  #此命令行可以命名x坐标轴的标签内容
plt.legend(loc='best')

plt.savefig('e:\\py_output\\Temperature22-45-empty-southmodel-facing north-HW=3-different-Height.png')
#plt.show()