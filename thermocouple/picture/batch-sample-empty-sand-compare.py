# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 18:39:15 2018

@author: DELL
"""

#此程序用于调整画图的样式，作为批量画图的模板
#此程序并不是批量处理程序
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

os.chdir(r'C:\Users\DELL\Desktop\处理数据\分析数据\thermo\10min_average\south model-facing north-h=30cm-10min_average\20170511')
file = os.listdir(r'C:\Users\DELL\Desktop\处理数据\分析数据\thermo\10min_average\south model-facing north-h=30cm-10min_average\20170511')
data1 = pd.read_csv(file[0])
data2 = pd.read_csv(file[-1])

y1 = data1.loc[:,'Temperature'] #sand
y2 = data2.loc[:,'Temperature'] #empty 

y = y2 - y1 # empty-sand
x = np.arange(143)
z = x * 0

fig = plt.figure()
ax  = fig.add_subplot(1,1,1)

plt.plot(x,y,'rD-',markersize = 1,linewidth = 1.5,label = 'The difference between empty model and sand model')
plt.plot(x,z,'k--',linewidth = 1.1)
plt.xlim(0,143)
plt.ylim(-6,6)
plt.xlabel('time',fontsize = 12)
plt.ylabel('T(℃)',rotation = 90,fontsize = 12)
plt.minorticks_on()
xticks = ax.set_xticks([0,24,48,72,96,120,143])  #此命令行可以确定x轴标签的位置
xlabels = ax.set_xticklabels(['0:00','4:00','8:00','12:00','16:00','20:00','24:00'])  #此命令行可以命名x坐标轴的标签内容
yticks = ax.set_yticks([-6,-4,-2,0,2,4,6])
ylabels = ax.set_yticklabels(['-6','-4','-2','0','2','4','6'])
#设置图注
plt.legend(loc='best',fontsize = 13)
plt.grid(True,linestyle='--')
plt.show()



  
