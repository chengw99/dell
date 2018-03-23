# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 10:16:55 2017

@author: DELL
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir('e:\py_output')

a = pd.read_csv('1.csv')
#读取所有的列
#l = data.columns  获取所有的列的名称
#for i in l:
    #a = data[i]
    #print(a)
#还有两个问题：用多次类似的循环那里能不能用函数搞定？列表有很多元素的时候，怎么分割成单一元素然后再写进csv
#读取所需数据    
data_1 = a.ix[787:2226,34]  #突然发现pandas行索引和列索引是有区别的，行索引的时候结束索引是被包含的，而列索引的结束索引是不被包含的
data2 = a.ix[787:2226,35]   #连续读出4列数据的时候，变成列表的时候，4列数据会变成一个元素，打印到csv的时候就会在一个单元格里，所以分开了，这是第一种方法
data3 = a.ix[787:2226,36]
data4 = a.ix[787:2226,37]
#求每小时平均
#求温度平均
tem1 = []
for i in range(24):
    data_mean_1 = sum(data_1[60*i:60*i+60])/60.
    tem1.append(data_mean_1)
tem2 = []
for i in range(24):
    data_mean2 = sum(data2[60*i:60*i+60])/60.
    tem2.append(data_mean2)
tem3 = []
for i in range(24):
    data_mean3 = sum(data3[60*i:60*i+60])/60.
    tem3.append(data_mean3)
tem4 = []
for i in range(24):
    data_mean4 = sum(data4[60*i:60*i+60])/60.
    tem4.append(data_mean4)

#生成时间序列
time = []
for j in range(24):
    t = str(j) + ':00'
    time.append(t)

#将生成的数据写进csv文件中
result = pd.DataFrame({'time':time,'Temperature30cm':tem1,'Temperature60cm':tem2,'Temperature90cm':tem3,'Temperature110cm':tem4})
columns = ['time','Temperature30cm','Temperature60cm','Temperature90cm','Temperature110cm']  #这样可以指定列的顺序
result.to_csv('T_average_perhour.csv',columns = columns)

#画图
x = range(24)
y1 = tem1
y2 = tem2
y3 = tem3
y4 = tem4
plt.figure()
#plt.plot(x,y1,'r-',x,y2,'r--',x,y3,'b-',x,y4,'b--')  把多条曲线放在同一张图上
#第一张子图
plt.subplot(221)
plt.plot(x,y1,'r-',label = 'Temperature30cm')
plt.xlim(0,24)
plt.ylim(26,38)
plt.xlabel('hour')
plt.ylabel('℃',rotation = 0)
x_ticks = np.arange(0,28,4)
y_ticks = np.arange(26,38,2)
plt.xticks(x_ticks)
plt.yticks(y_ticks)
plt.legend(loc='best')
plt.xlim(0,24)
plt.ylim(26,38)
#第二张子图
plt.subplot(222)
plt.plot(x,y2,'r--',label = 'Temperature60cm')
plt.xlabel('hour')
plt.ylabel('℃',rotation = 0)
x_ticks = np.arange(0,28,4)
y_ticks = np.arange(26,38,2)
plt.xticks(x_ticks)
plt.yticks(y_ticks)
plt.legend(loc='best')
#第三张子图
plt.subplot(223)
plt.plot(x,y3,'b-',label = 'Temperature90cm')
plt.xlabel('hour')
plt.ylabel('℃',rotation = 0)
x_ticks = np.arange(0,28,4)
y_ticks = np.arange(26,38,2)
plt.xticks(x_ticks)
plt.yticks(y_ticks)
plt.legend(loc='best')
#第四张子图
plt.subplot(224)
plt.plot(x,y4,'b--',label = 'Temperature110cm')
plt.xlabel('hour')
plt.ylabel('℃',rotation = 0)
x_ticks = np.arange(0,28,4)
y_ticks = np.arange(26,38,2)
plt.xticks(x_ticks)
plt.yticks(y_ticks)
plt.legend(loc='best')
#把所有的设置都显示出来
plt.show()
####--------------------------------------####
#求半小时平均
Tem1 = []
for i in range(48):
    data_mean_one = sum(data_1[30*i:30*i+30])/30.
    Tem1.append(data_mean_one)
    
Tem2 = []
for i in range(48):
    data_mean_two = sum(data2[30*i:30*i+30])/30.
    Tem2.append(data_mean_two)
    
Tem3 = []
for i in range(48):
    data_mean_three = sum(data3[30*i:30*i+30])/30.
    Tem3.append(data_mean_three)

Tem4 = []
for i in range(48):
    data_mean_four = sum(data4[30*i:30*i+30])/30.
    Tem4.append(data_mean_four)
#或者用函数！

    
#生成时间序列
Time = []     #开心！
for i in range(24):
    for j in range(2):
        if j % 2 == 0:
            t = str(i)+':00'
        else:
            t = str(i)+':30'
        Time.append(t)
average_half_hour = pd.DataFrame({'time':Time,'Temperature30cm':Tem1,'Temperature60cm':Tem2,'Temperature90cm':Tem3,'Temperature110cm':Tem4})
columns = ['time','Temperature30cm','Temperature60cm','Temperature90cm','Temperature110cm'] 
average_half_hour.to_csv('T_average_half_hour.csv',columns = columns)