# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 08:40:39 2018

@author: DELL
"""

# 数据要求是导出的Excel内含多个工作表
# 此程序用于拼接红外温度数据，2017.08，中空模型，不同日期

import os
import glob
import pandas as pd

ipath = r'E:\py_data\hongwai' # 输入数据文件位置
opath = r'E:\py_output' # 输出数据
date = ['201708'+str(i) for i in range(15,19)] #分析日期
k = ['east','north','south','west']

for d in date:
    for i in k:
        fname = glob.glob(ipath+'\\'+d+'\\'+i+'\\'+'*.xls*')
        
        for f in fname:
            all_worksheets = pd.read_excel(f,sheetname=None,skiprows=8,index_col=0)
            
            result = []
            for worksheet_name,data in all_worksheets.items():
                result.append((data.T)[::-1])
            final = pd.concat(result)
            
            qExist = os.path.exists(opath+'\\'+d+'\\'+'data'+'\\'+i)
            if not qExist:
                os.makedirs(opath+'\\'+d+'\\'+'data'+'\\'+i)
                final.to_csv(opath+'\\'+d+'\\'+'data'+'\\'+i+'\\'+os.path.basename(f)[:-5]+'.csv',index=False,header=None)
            else:
                final.to_csv(opath+'\\'+d+'\\'+'data'+'\\'+i+'\\'+os.path.basename(f)[:-5]+'.csv',index=False,header=None)
                
                