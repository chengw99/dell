# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 14:25:44 2018

@author: DELL
"""

# 此程序用于批量获取红外温度数据中每个工作簿中的工作表信息
# 检测是否符合格式xlsx 以及 工作表长度
# 使用xlrd读取速度较慢

import os
import glob
from xlrd import open_workbook

workbook_counter = 0 # 计算总共有多少个工作簿
error = [] # 收集长度不统一的工作簿

date = ['201706'+str(i) for i in range(25,26)] # 批量处理的日期范围 
for d in date:
    
    k = ['one-facing north','two-facing north','three-facing north',
         'one-facing south','two-facing south','three-facing south']
    for j in k:
        input_directory = r'E:\py_data\hongwai'+'\\'+d+'\\'+j   # 需要检查的目录

        for input_file in glob.glob(os.path.join(input_directory,'*.xls*')):
            workbook = open_workbook(input_file)
            print('Workbook:%s' % os.path.basename(input_file)) # 工作簿文件名
            print('Number of worksheet:%d' % workbook.nsheets) # 工作表数量
    
            for worksheet in workbook.sheets(): # 返回工作表的名字，行数以及列数
                print('Worksheet name:',worksheet.name,'\tRows:',\
                          worksheet.nrows,'\tColumns:',worksheet.ncols)
        
            # 查看是否有行数或列数不统一的工作簿
                if worksheet.nrows != 489 or worksheet.ncols != 641: # 数字代表的是统一的长度
                    error.append(os.path.basename(input_file))
                    workbook_counter += 1

print('Number of Excel workbooks: %d' % (workbook_counter))
print(r'长度不统一的工作簿:',error)