# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 11:40:43 2018

@author: DELL
"""

import os
import shutil

#---------------------------复制、重命名源文件------------------------------------#
#重命名需要跟处理数据分隔开，不然没运行一次，文件就会被重命名一次
#不更改源文件
folder = os.listdir(r'C:\Users\DELL\Desktop\处理数据\按日期排序\thermo')
for file in folder:
    try:
        shutil.copytree(r'C:\Users\DELL\Desktop\处理数据\按日期排序\thermo\\'+file,r'e:\py_data\thermo\\'+file) #复制整个目录
    except:
        pass
#对csv文件进行重命名
u_file = os.listdir(r'E:\py_data\thermo')
for u in u_file:
    w_file = os.listdir(r'E:\py_data\thermo'+'\\'+u)
    for w in w_file:
        if w[-3:] == 'csv':
            cExist = os.path.exists(r'E:\py_data\thermo'+'\\'+u+'\\'+u+'-'+w)
            if not cExist:
                shutil.move(r'E:\py_data\thermo'+'\\'+u+'\\'+w,r'E:\py_data\thermo'+'\\'+u+'\\'+u+'-'+w)
            else:
                pass