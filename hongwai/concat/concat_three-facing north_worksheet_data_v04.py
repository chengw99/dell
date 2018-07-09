# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 09:57:04 2018

@author: DELL
"""

# 此程序用于拼接红外温度数据
# 对应高宽比为3:1的朝北侧壁

import glob
import pandas as pd


ipath = r'E:\py_data\hongwai\three-facing north'
#fname = glob.glob(ipath+'\\'+'*.xls*')
fname = glob.glob(ipath+'\\'+'three-facing north-22.xlsx')

result = []
for f in fname:
    all_worksheets = pd.read_excel(f,sheetname=None,skiprows=8,index_col=0) # 跳过8行来读取数据，以第一列为index（行的名字）
    for worksheet_name,data in all_worksheets.items():
        result.append(data.T)

#result.reverse()
final = pd.concat(result)
final.to_csv('E:\py_output'+'\\'+'test.csv',index=False,header=None)