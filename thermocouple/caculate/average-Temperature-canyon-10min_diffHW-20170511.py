# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 10:03:39 2018

@author: DELL
"""

# 此程序用于处理某一天热电偶缺失温度数据，但若出问题的总是某一通道数据，可直接在生成数据的时候去掉问题通道，再进行批量处理，不必单个处理
# 在avverage-Temperature-canyon-10min_v01.py程序运行后的基础上，获取各街谷平均温度
# 但发现中空模型有个通道崩了
# 此程序用于获取20170514各街谷平均温度--中空模型2:1街谷90cm测点有问题，需去掉此点，重新平均画图

import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#----------------------------------获取数据-------------------------------------#
k_file = ['B-HW1-empty model','F-HW2-empty model','C-HW3-empty model']
for k in k_file:
    ipath = r'E:\py_output'+'\\'+k+'\\'+'20170514'
    q_file = glob.glob(ipath+'\\'+'*.csv')
    
    l = []
    for i in range(7):
        a = pd.read_csv(q_file[i])
        l.append(a)
                
    tem_mean = (l[0].iloc[:,2] + l[1].iloc[:,2] + l[2].iloc[:,2] + l[3].iloc[:,2] +\
                    l[4].iloc[:,2] + l[5].iloc[:,2] + l[6].iloc[:,2])/len(q_file) 
    time = l[0].iloc[:,1]
                
    result = pd.DataFrame({'time':time,'Temperature':tem_mean})
    columns = ['time','Temperature']
    
    result.to_csv(r'e:\\py_output'+'\\'+k+'.csv',columns = columns)
    
#-------------------------------画图-------------------------------------------#
q_file = glob.glob(r'e:\\py_output'+'\\'+'*.csv')

data1 = pd.read_csv(q_file[0]) # H/W=1
data2 = pd.read_csv(q_file[2]) # H/W=2
data3 = pd.read_csv(q_file[1]) # H/W=3

x = np.arange(144)
y1 = data1.loc[:,'Temperature'] # H/W=1
y2 = data2.loc[:,'Temperature'] # H/W=2
y3 = data3.loc[:,'Temperature'] # H/W=3

fig = plt.figure(figsize=(12,9),dpi=160)
ax = fig.add_subplot(1,1,1)

plt.plot(x,y1,linestyle='-',marker='D',markersize=5,markerfacecolor='none',markevery=6,linewidth=0.8,label='HW1'+'-'+'20170514')
plt.plot(x,y2,linestyle='-',marker='o',markersize=5,markerfacecolor='none',markevery=6,linewidth=0.8,label='HW2'+'-'+'20170514')
plt.plot(x,y3,linestyle='-',marker='s',markersize=5,markerfacecolor='none',markevery=6,linewidth=0.8,label='HW3'+'-'+'20170514')

plt.xlim(0,144)
plt.ylim(22,42)
plt.xlabel('time',fontsize=12)
plt.ylabel('Temperature(℃)',rotation=90,fontsize=12)
plt.minorticks_on()
xticks = ax.set_xticks([0,24,48,72,96,120,144])
xlabels = ax.set_xticklabels(['0:00','4:00','8:00','12:00','16:00','20:00','24:00'])
yticks = ax.set_yticks([22,26,30,34,38,42])
ylabels = ax.set_yticklabels(['22','26','30','34','38','42'])
plt.legend(loc='best',fontsize=14,markerscale=1)
plt.title('The average canyon temperature-20170514',fontsize=12)
plt.grid(True,linestyle='--')
plt.savefig(r'e:\py_output'+'\\'+'The average canyon temperature-20170514.png')
plt.close()