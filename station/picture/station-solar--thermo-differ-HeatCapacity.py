# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 10:10:44 2018

@author: DELL
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

station = pd.read_csv(r'C:\Users\DELL\Desktop\处理数据\按日期排序\station\north station\201706\20170609.csv',engine = 'python')
#---------------------rain---------------------------------------------------#
#==============================================================================
# rain = station.loc[:,'RAINF']
# solar = station.loc[:,'SRAD']
# x = np.arange(144)
# fig = plt.figure(dpi=160)
# ax  = fig.add_subplot(1,1,1)
# 
# plt.bar(x,rain,label = 'rainfall-20170609')
# 
# plt.xlim(0,143)
# plt.ylim(0,10)
# plt.xlabel('time',fontsize = 12)
# plt.ylabel('Precipitation(inches)',rotation = 90,fontsize = 12)
# plt.minorticks_on()
# xticks = ax.set_xticks([0,24,48,72,96,120,143])  #此命令行可以确定x轴标签的位置
# xlabels = ax.set_xticklabels(['0:00','4:00','8:00','12:00','16:00','20:00','24:00'])  #此命令行可以命名x坐标轴的标签内容
# yticks = ax.set_yticks([0,2,4,6,8,10])
# ylabels = ax.set_yticklabels(['0','2','4','6','8','10'])
# #设置图注
# plt.legend(loc='best',fontsize = 14)
# plt.grid(True,linestyle='--')
# plt.savefig(r'C:\Users\DELL\Desktop\画图数据\不同天气-装沙+中空\20170609\precipatation-20170609.png')
# 
# time = []
# for a in range(24):
#     for b in np.linspace(0,60,num=6,endpoint=False):
#         if b == 0:
#             time.append(str(int(a))+':0'+str(int(b)))
#         else:
#             time.append(str(int(a))+':'+str(int(b)))
# result = pd.DataFrame({'rainfall':rain,'time':time})
# columns = ['time','rainfall']
# result.to_csv(r'C:\Users\DELL\Desktop\画图数据\不同天气-装沙+中空\20170609\rain-20170609.csv',columns = columns)
#==============================================================================
#-----------------------------------solar--------------------------------------#
solar = station.loc[:,'SRAD']
x = np.arange(144)

fig = plt.figure(dpi=160)
ax = fig.add_subplot(1,1,1)
            
plt.bar(x,solar,label = 'The solar radiation-20170609')
plt.xlim(0,143) 
plt.ylim(0,600)
plt.xlabel('time',fontsize = 12)
plt.ylabel('solar radiation(Watts/m2)',rotation = 90,fontsize = 12)
xticks = ax.set_xticks([0,24,48,72,96,120,143])  #此命令行可以确定x轴标签的位置
xlabels = ax.set_xticklabels(['0:00','4:00','8:00','12:00','16:00','20:00','24:00'])  #此命令行可以命名x坐标轴的标签内容
yticks = ax.set_yticks([0,100,200,300,400,500,600])
ylabels = ax.set_yticklabels(['0','100','200','300','400','500','600'])
#设置图注
plt.legend(loc='best',fontsize = 8)
plt.grid(True,linestyle='--')
plt.savefig(r'C:\Users\DELL\Desktop\画图数据\不同天气-装沙+中空\20170609\solaradiation-20170609.png')

time = []
for i in range(24):
    for j in np.linspace(0,60,num = 6,endpoint = False):
        if j == 0:
            time.append(str(int(i))+':0'+str(int(j)))
        else:
            time.append(str(int(i))+':'+str(int(j)))
        
result = pd.DataFrame({'solar radiation':solar,'time':time})
columns = ['time','solar radiation']
result.to_csv(r'C:\Users\DELL\Desktop\画图数据\不同天气-装沙+中空\20170609\solaradiation-20170609.csv')
        