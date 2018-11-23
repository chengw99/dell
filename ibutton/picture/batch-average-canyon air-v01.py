# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 19:10:49 2018

@author: DELL
"""

# 此程序用于分析街谷平均空气温度（考虑不同高度进行平均） --使用ibutton数据

import os
import glob
import shutil
import pandas as pd

ipath = r'F:\result\处理数据_20181122\picture\ibutton\10min平均\5月份\对比不同高度\data'
opath = r'e:\py_data\ibutton'
l = ['1','2','3','5'] # 此处可选择不同的测点位置来进行分析

q_file = os.listdir(ipath)
for q in q_file:
    w_file = os.listdir(ipath+'\\'+q)
    for w in w_file:
        e_file = glob.glob(ipath+'\\'+q+'\\'+w+'\\'+'*.csv')
        for e in e_file:
            qExist = os.path.exists(opath+'\\'+w+'\\'+q)
            if not qExist:
                os.makedirs(opath+'\\'+w+'\\'+q)
            else:
                pass
            f = os.path.basename(e)
            for j in l:
                if f[1] == str(j):
                    try:
                        shutil.copyfile(ipath+'\\'+q+'\\'+w+'\\'+f,opath+'\\'+w+'\\'+q+'\\'+f)
                    except:
                        pass