# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 21:42:32 2017

@author: DELL
"""

import pandas as pd
import os

os.chdir('e:\py_data\station')

data = pd.read_csv('5.csv')

#获取单个日期自动站数据
#start = '06/'+'13'+'/17'
#a = data[(data.DATE == start)].index.tolist()  
 
#f = data.ix[a[0]:a[-1],:]

#-------进阶-------#
#获取同一个csv文件中不同日期并且按照不同日期分割成不同的文件
for i in range(10,11):  #范围根据日期的时间来修改，左边是起点，右边是终点，但不取右边的终点值
    po = str(i)
    start = '12/'+ po +'/17'
    a = data[(data.DATE == start)].index.tolist()
    f = data.ix[a[0]:a[-1],:]
    f.to_csv('e:\\py_output\\'+'201712'+str(i)+'.csv')