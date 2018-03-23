# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 08:37:08 2018

@author: DELL
"""

import os 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

os.chdir('e:\py_output')

#画图-不同建筑热容
#读取数据
#------------高宽比1：1---------------------------------------------------------
'''data1 = pd.read_csv('e:\\py_data\\pic\\T_average_perhour_B.csv') #B中空模型1:1
data2 = pd.read_csv('e:\\py_data\\pic\\T_average_perhour_E.csv') #E装沙模型1:1'''
#------------高宽比2:1----------------------------------------------------------
'''data1 = pd.read_csv('e:\\py_data\\pic\\T_average_perhour_F.csv') #F中空模型2:1
data2 = pd.read_csv('e:\\py_data\\pic\\T_average_perhour_A.csv') #A装沙模型2:1'''
#------------高宽比3:1----------------------------------------------------------
data1 = pd.read_csv('e:\\py_data\\pic\\T_average_perhour_C.csv') #C中空模型3:1
data2 = pd.read_csv('e:\\py_data\\pic\\T_average_perhour_D.csv') #D装沙模型3:1'''


x = np.arange(24)
y1 = data1.ix[:,2]
y2 = data2.ix[:,2]

fig = plt.figure()
ax = fig.add_subplot(1,1,1) 
plt.plot(x,y1,'r^-',linewidth = 1,label = 'empty south model facing north(H/W=3,h=1.1m)')
plt.plot(x,y2,'ks-',linewidth = 1,label = 'sand south model facing north(H/W=3,h=1.1m)')
#plt.plot(x,y1,'r^-',linewidth = 1,label = 'empty model air temperature-S(H/W=3,h=1.44m)')
#plt.plot(x,y2,'ks-',linewidth = 1,label = 'sand model air temperature-S(H/W=3,h=1.44m)')

plt.xlim(0,24) #表示x轴的范围设置为0到24
plt.ylim(22,45)
plt.xlabel('time')
plt.ylabel('T(℃)',rotation = 90)
xticks = ax.set_xticks([0,4,8,12,16,20,24])  #此命令行可以确定x轴标签的位置
xlabels = ax.set_xticklabels(['0:00','4:00','8:00','12:00','16:00','20:00','24:00'])  #此命令行可以命名x坐标轴的标签内容
plt.legend(loc='best')

plt.savefig('e:\\py_output\\Temperature22-45-southmodel-facing north-h=1.1m-HW=3-different-HC.png')
#plt.show()