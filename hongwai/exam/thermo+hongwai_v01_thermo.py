# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 13:52:12 2018

@author: DELL
"""

# 此程序用于获取热电偶温度数据，再与红外数据进行对比

#--------------------------热电偶----------------------------------------------#
# 此程序用于批量获取热电偶每小时温度平均的数据
# 数据来源是热电偶10min平均的温度数据 - 10min平均数据已整理好，故使用它

import os
import glob
import pandas as pd

ipath = r'E:\py_data\thermo'
opath = r'E:\py_output'

file = glob.glob(ipath+'\\'+'*.csv')
for f in file:
    a = pd.read_csv(f)
    data = a.ix[:,2]
    
    tem = []
    for i in range(24):
        data_mean = sum(data[6*i:6*i+6])/6.
        tem.append(data_mean)
        
    time = []
    for j in range(24):
        t = str(j) + ':00'
        time.append(t)
        
    result = pd.DataFrame({'Time':time,'Temperature':tem})
    columns = ['Time','Temperature']
    
    if os.path.basename(f)[-36:-31] == '110cm':
        result.to_csv(r'e:\py_output'+'\\'+'T_average_1h-'+os.path.basename(f)[-36:-31]+'.csv',columns=columns)
    else:
        result.to_csv(r'e:\py_output'+'\\'+'T_average_1h-'+os.path.basename(f)[-35:-31]+'.csv',columns=columns)
