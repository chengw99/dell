# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 20:06:31 2018

@author: DELL
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


os.chdir('e:\py_output')

#画图-不同高宽比
#提取数据
#---------------------------------------------------------------------------
'''data1 = pd.read_csv('e:\\py_data\\pic\\T_average_perhour_B.csv') #B中空模型1:1
data2 = pd.read_csv('e:\\py_data\\pic\\T_average_perhour_F.csv') #F中空模型2:1
data3 = pd.read_csv('e:\\py_data\\pic\\T_average_perhour_C.csv') #C中空模型3:1'''
#---------------------------------------------------------------------------
data1 = pd.read_csv('e:\\py_data\\pic\\T_average_perhour_E.csv') #E装沙模型1:1
data2 = pd.read_csv('e:\\py_data\\pic\\T_average_perhour_A.csv') #A装沙模型2:1
data3 = pd.read_csv('e:\\py_data\\pic\\T_average_perhour_D.csv') #D装沙模型3:1'''
#---------------------------------------------------------------------------
x = np.arange(24)
y1 = data1.ix[:,2]
y2 = data2.ix[:,2]
y3 = data3.ix[:,2]

    
fig = plt.figure()
ax = fig.add_subplot(1,1,1)  #貌似引入这个才可以调用后面的方法set_xticks
#------------------------------------------------------------------------------------------
plt.plot(x,y1,'rv-',linewidth = 1,label = 'sand south model facing north(H/W=1,h=0.9m)')
plt.plot(x,y2,'ks-',linewidth = 1,label = 'sand south model facing north(H/W=2,h=0.9m)')
plt.plot(x,y3,'b^-',linewidth = 1,label = 'sand south model facing north(H/W=3,h=0.9m)')#'''
#------------------------------------------------------------------------------------------
'''plt.plot(x,y1,'rv-',linewidth = 1,label = 'sand model-air temperature-south(H/W=1,h=1.14m)')
plt.plot(x,y2,'ks-',linewidth = 1,label = 'sand model-air temperature-south(H/W=2,h=0.9m)')
plt.plot(x,y3,'b^-',linewidth = 1,label = 'sand model-air temperature-south(H/W=3,h=0.9m)')#'''


plt.xlim(0,24) #表示x轴的范围设置为0到24
plt.ylim(22,45)
plt.xlabel('time')
plt.ylabel('T(℃)',rotation = 90)
#plt.xticks(np.arange(0,26,2))
#plt.yticks(np.arange(25,40,2))
xticks = ax.set_xticks([0,4,8,12,16,20,24])  #此命令行可以确定x轴标签的位置
#yticks = ax.set_xticks([25,27,29,31,33,35,37,39,41])
xlabels = ax.set_xticklabels(['0:00','4:00','8:00','12:00','16:00','20:00','24:00'])  #此命令行可以命名x坐标轴的标签内容
#ylabels = ax.set_yticklabels(['25','27','29','31','33','35','37','39','41'])
    #plt.title('Tem-perhour',fontsize = 18)
plt.legend(loc='best')
#plt.savefig('e:\\py_output\\air temperature-sandmodel-h=1.14m-south-different-HW.png')
plt.savefig('e:\\py_output\\Temperature22-45-southsandmodel-facing north-h=0.9m-different-HW.png') 
#plt.show()