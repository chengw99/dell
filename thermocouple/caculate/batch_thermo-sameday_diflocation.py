# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 14:06:31 2018

@author: DELL
"""

import os
import pandas as pd

import glob

#此程序用于批量处理同一天数不同摆放位置ABCDEF的热电偶温度数据,只处理了一个通道
os.chdir('e:\py_output')
csv_filenames = glob.glob('e:\\py_data\\*.csv') #得到要处理的文件路径，此路径可修改

for filename in csv_filenames:  #循环处理列举的文件
    a = pd.read_csv(filename)

    data = a.ix[:,35]

    tem = []
    for i in range(24):
        data_mean = sum(data[60*i:60*i+60])/60.
        tem.append(data_mean)
    
    time = []
    for j in range(24):
        t = str(j) + ':00'
        time.append(t)
    
    result = pd.DataFrame({'time':time,'Temperature':tem})
    columns = ['time','Temperature']
    result.to_csv('e:\\py_output\\T_average_perhour_'+filename[11]+'.csv',columns = columns)  #得到对应日期的每小时平均的文件

