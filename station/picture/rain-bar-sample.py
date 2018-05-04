# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 10:58:20 2018

@author: DELL
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

os.chdir(r'C:\Users\DELL\Desktop\处理数据\picture\station\north station\total data')
data = pd.read_csv(r'20170515.csv')

r = data.loc[:,'RAINF']
x = np.arange(144)

fig = plt.figure()
ax  = fig.add_subplot(1,1,1)

plt.bar(x,r,label = 'Precipatation')

plt.xlim(0,143)
plt.ylim(0,10)
plt.xlabel('time',fontsize = 12)
plt.ylabel('Precipitation(inches)',rotation = 90,fontsize = 12)
plt.minorticks_on()
xticks = ax.set_xticks([0,24,48,72,96,120,143])  #此命令行可以确定x轴标签的位置
xlabels = ax.set_xticklabels(['0:00','4:00','8:00','12:00','16:00','20:00','24:00'])  #此命令行可以命名x坐标轴的标签内容
yticks = ax.set_yticks([0,2,4,6,8,10])
ylabels = ax.set_yticklabels(['0','2','4','6','8','10'])
#设置图注
plt.legend(loc='best',fontsize = 14)
plt.grid(True,linestyle='--')
plt.savefig()