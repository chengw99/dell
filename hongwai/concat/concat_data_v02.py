# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 13:38:53 2018

@author: DELL
"""

# 此程序用于拼接红外温度数据
# 适用于高宽比为1:1朝南面
import glob
import numpy as np
import pandas as pd


ipath = r'F:\外场实验\0626IRdata_empty_module\1时\高宽比1：1朝南'
fname = glob.glob(ipath+'\\'+'*.xls*')
result = []
for f in fname:
    data = pd.read_excel(f,skiprows=8,index_col=0) # 跳过8行来读取数据，以第一列为index（行的名字）
    result.append(data.T)

result.reverse()
final = pd.concat(result)
final.to_csv('E:\py_data\picture'+'\\'+'test.csv',index=False,header=None)