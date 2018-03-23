# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 17:41:22 2017

@author: DELL
"""


import pandas as pd
import os

os.chdir('e:\py_data\ibutton')

data = pd.read_csv('B2.csv',names = ['0','1','2'])

#每个日期时间序列里文本不同的地方，因为ibutton比较难设置整点开始采集数据
sample = data.ix[22,0][-4:]

#获取单个日期24小时ibutton温度数据
#start = '17-'+'6'+'-13 0:0' + sample   #这样可以得到所需的时段
#end = '17-'+'6'+'-13 23:5' + sample 
#a = data[(data.ix[:,0] == start)].index.tolist()  
#b = data[(data.ix[:,0] == end)].index.tolist()  
#f = data.ix[a[0]:b[0],:]
#f.to_csv('e:\\py_output\\'+'201705'+str(i)+'.csv')

#获取同一个csv文件中不同日期，按照日期分割成不同的文件，最终得到不同日期24小时的ibutton温度数据  
for i in range(6,14):  #范围根据日期的时间来修改，左边是起点，右边是终点，但不取右边的终点值
    po = str(i)
    start = '17-'+'5'+'-'+po+' 0:0' + sample   #这样可以得到所需的时段
    end = '17-'+'5'+'-'+po+' 23:5' + sample 
    a = data[(data.ix[:,0] == start)].index.tolist()  
    b = data[(data.ix[:,0] == end)].index.tolist()  
    f = data.ix[a[0]:b[0],:]
    if i < 10:
        f.to_csv('e:\\py_output\\'+'2017050'+str(i)+'.csv')
    elif i >= 10:
        f.to_csv('e:\\py_output\\'+'201705'+str(i)+'.csv')
        
