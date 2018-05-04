# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 09:49:51 2018

@author: DELL
"""

#此程序用于画图-壁面温度和自动站的24小时温度变化图-样板图
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'e:\py_data\station\20170511.csv')
data2 = pd.read_csv(r'e:\py_data\station\T_average_10min-north model-facing north-h=90cm-B-HW1-empty model-20170511.csv')
x = np.arange(144)
y = data.loc[:,'SRAD']
y2 = data2.iloc[:,2]

fig = plt.figure()
ax1  = fig.add_subplot(1,1,1)
    plt.bar(x,y,label = 'The solar radiation')
plt.xlim(0,143) 
plt.ylim(0,600)
plt.xlabel('time',fontsize = 12)
plt.ylabel('solar radiation(Watts/m2)',rotation = 90,fontsize = 12)
xticks = ax1.set_xticks([0,24,48,72,96,120,143])  #此命令行可以确定x轴标签的位置
xlabels = ax1.set_xticklabels(['0:00','4:00','8:00','12:00','16:00','20:00','24:00'])  #此命令行可以命名x坐标轴的标签内容
yticks = ax1.set_yticks([0,100,200,300,400,500,600])
ylabels = ax1.set_yticklabels(['0','100','200','300','400','500','600'])
plt.legend(loc='upper right',bbox_to_anchor=(1,1),fontsize = 12)
plt.grid(True,linestyle='--')
plt.minorticks_on()

ax2 = ax1.twinx() #用于添加y轴
plt.plot(x,y2,color = 'darkorange',marker = 'D',markersize = 0.5,linestyle = '-',linewidth = 1.5,label = 'The temperature')
         
plt.xlim(0,143)
plt.ylim(22,46)
plt.xlabel('time',fontsize = 12)
plt.ylabel('Temperature(℃)',rotation = 90,fontsize = 12)
plt.minorticks_on()
xticks = ax2.set_xticks([0,24,48,72,96,120,143])  #此命令行可以确定x轴标签的位置
xlabels = ax2.set_xticklabels(['0:00','4:00','8:00','12:00','16:00','20:00','24:00'])  #此命令行可以命名x坐标轴的标签内容
yticks = ax2.set_yticks([22,26,30,34,38,42,46])
ylabels = ax2.set_yticklabels(['22','26','30','34','38','42','46'])
#设置图注
plt.legend(loc='upper right',bbox_to_anchor=(0.98,0.93),fontsize = 12,markerscale = 10) #这里可以修改legend中marker的大小
plt.grid(True,linestyle='--')
plt.minorticks_on()


plt.show()