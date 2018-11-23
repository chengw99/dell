# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 14:34:03 2018

@author: DELL
"""

# 此程序根据 thermo+hongwai_v01_pic_coord.py 选出的数据范围 对红外数据进行面平均
# 因为每个时间红外数据选择的范围都不同，所以不能做批量处理

import numpy as np
import pandas as pd

ipath = r'E:\py_data\hongwai'
opath = r'E:\py_output'

data = pd.read_csv(ipath+'\\'+'one-facing south-23.csv',names=np.arange(480)) # 调整输入文件

result = data.ix[1555:1595,220:260] # 选取位置的范围 坐标+—20 取面平均

a = np.array(result)
q = a.sum()/((a.shape[0])*(a.shape[1]))
print(q)
#result.to_csv(opath+'\\'+'30cm-00.csv')