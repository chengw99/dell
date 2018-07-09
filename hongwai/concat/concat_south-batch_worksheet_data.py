# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 13:30:03 2018

@author: DELL
"""

# 数据要求是导出的Excel内含多个工作表
# 此程序用于批量拼接红外温度数据,中空模型
# 对应高宽比为1:1，2:1,3:1朝南侧壁

import os
import glob
import pandas as pd

date = ['201706'+str(i) for i in range(24,28)]
for d in date:
    
    ipath = r'E:\py_data\hongwai'+'\\'+d
    opath = r'e:\py_output'
    k = ['one-facing south','two-facing south','three-facing south']

    for i in k:
        fname = glob.glob(ipath+'\\'+i+'\\'+'*.xls*')
    
        for f in fname:
            all_worksheets = pd.read_excel(f,sheetname=None,skiprows=8,index_col=0) # 跳过8行来读取数据，以第一列为index（行的名字）

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
            
