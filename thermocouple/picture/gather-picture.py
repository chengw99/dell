# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 11:33:56 2018

@author: DELL
"""

#此程序用于获取所有的图片到一个汇总文件夹中
import os 
import shutil

qfile = os.listdir(r'C:\Users\DELL\Desktop\处理数据\picture\thermo')
for q in qfile:
    qExist = os.path.exists(r'C:\Users\DELL\Desktop\处理数据\picture\thermo\\'+q+'\\'+r'汇总')
    if not qExist:
        os.mkdir(r'C:\Users\DELL\Desktop\处理数据\picture\thermo\\'+q+'\\'+r'汇总')
    else:
        pass
wfile = os.listdir(r'C:\Users\DELL\Desktop\处理数据\picture\thermo')
for w in wfile:
    tfile = os.listdir(r'C:\Users\DELL\Desktop\处理数据\picture\thermo'+'\\'+w)
    for t in tfile[0:3]:
        ufile = os.listdir(r'C:\Users\DELL\Desktop\处理数据\picture\thermo'+'\\'+w+'\\'+t+'\\'+r'汇总')
        for u in ufile:
            kfile = os.listdir(r'C:\Users\DELL\Desktop\处理数据\picture\thermo'+'\\'+w+'\\'+t+'\\'+r'汇总'+'\\'+u)
            for k in kfile:
                if k[-3:] == 'png':
                    shutil.copyfile(r'C:\Users\DELL\Desktop\处理数据\picture\thermo'+'\\'+w+'\\'+t+'\\'+r'汇总'+'\\'+u+'\\'+k,r'C:\Users\DELL\Desktop\处理数据\picture\thermo\\'+w+'\\'+r'汇总'+'\\'+k)