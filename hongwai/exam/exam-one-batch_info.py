# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 10:39:02 2018

@author: DELL
"""

# 此程序用于获取红外温度数据中每个工作簿中的工作表信息
# 适用检查高宽比1:1的Excel

import os
import glob
from xlrd import open_workbook

input_directory = r'E:\py_data\hongwai' # 需要检查的目录
k = ['one-facing north','one-facing south']
workbook_counter = 0 # 计算总共有多少个工作簿
error = [] # 收集长度不统一的工作簿
for i in k:
    for input_file in glob.glob(os.path.join(input_directory+'\\'+i,'*.xls*')):
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