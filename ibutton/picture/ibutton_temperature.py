# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import shutil

os.chdir("E:\\py_data\\ibutton")#修改工作路径

#读取所需数据
shutil.copyfile(r'C:\Users\DELL\Desktop\处理数据\按日期排序\ibutton\5月份\A1\A1-20170506.csv','e:\\py_data\\ibutton\\A1-20170506.csv')
a=pd.read_csv('A1-20170506.csv',names=['0','1','2'])

data=(a.ix[:,2]).values.astype(float)#除掉字符串，使数据变成浮点数，可进行数学运算
    
#print(data.values)
#print(sum(data.values.astype(float)))
#处理温度数据，得到每小时平均
tem=[]
for j in range(24):
     data_mean=sum(data[j*6:j*6+6])/6.
     tem.append(data_mean)
#另外生成时间序列
time=[]
for i in range(24):
    t=str(i)+':00'
    time.append(t)

text=pd.DataFrame({'time':time,'Temperature':tem})
text.to_csv('35.csv')
#test=pd.DataFrame({'time':time})
#test.to_csv('shabi.csv')
#test=pd.DataFrame({'temperatue':data,'time':time})
#print(test)

x=range(24)
y=tem
figure=plt.plot(x,y,'r-',label='temperature')
#设置坐标轴范围
plt.xlim(0,24)
plt.ylim(26,38)
#设置坐标轴名称
plt.title('Temperature from ibutton per hour')
plt.xlabel('hour')
plt.ylabel('℃',rotation=0)
#设置坐标轴刻度
x_ticks=np.arange(0,24,4)
y_ticks=np.arange(26,38,2)
plt.xticks(x_ticks)
plt.yticks(y_ticks)
#设置标注
plt.legend(loc='best')
#plt.savefig('ibutton.png')


plt.show()