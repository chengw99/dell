# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 15:26:53 2018

@author: DELL
"""

#此程序用于筛选不同日期-不同街谷-不同高度的ibutton数据--6月份
#分离成不同的日期

import os
import glob
import shutil
import numpy as np
import pandas as pd

ipath = r'C:\Users\DELL\Desktop\处理数据\源数据\ibutton数据\20170608-20170622'
opath = r'e:\py_output'

qfile = glob.glob(ipath+'\\'+'*.csv')
for q in qfile:
    data = pd.read_csv(q,names=['0','1','2'],engine='python')
    sample = data.ix[22,'0'][-4:]
    
    if q[-6:-4] != 'B5':
        
        for i in range(9,22):
            po = str(i)
            start = '17-'+'6'+'-'+po+' 0:0' + sample   #这样可以得到所需的时段
            end = '17-'+'6'+'-'+po+' 23:5' + sample    #只需要修改月份的数字
            a = data[(data.ix[:,0] == start)].index.tolist()  
            b = data[(data.ix[:,0] == end)].index.tolist()
            f = data.ix[a[0]:b[0],:]
        
            if i < 10:
                f.to_csv('e:\\py_output\\'+q[-6:-4]+'-2017060'+str(i)+'.csv')
            elif i >= 10:
                f.to_csv('e:\\py_output\\'+q[-6:-4]+'-201706'+str(i)+'.csv')

    # 出现一个error,报错超出list范围，经过排查是因为B5缺测，与其他数据文件的时间范围不一致
    if q[-6:-4] == 'B5':

        for i in range(12,22):
            po = str(i)
            start = '17-'+'6'+'-'+po+' 0:0' + sample   #这样可以得到所需的时段
            end = '17-'+'6'+'-'+po+' 23:5' + sample    #只需要修改月份的数字
            a = data[(data.ix[:,0] == start)].index.tolist()  
            b = data[(data.ix[:,0] == end)].index.tolist()
            f = data.ix[a[0]:b[0],:]
        
            if i < 10:
                f.to_csv('e:\\py_output\\'+q[-6:-4]+'-2017060'+str(i)+'.csv')
            elif i >= 10:
                f.to_csv('e:\\py_output\\'+q[-6:-4]+'-201706'+str(i)+'.csv')        

#生成序号文件夹
wfile = os.listdir(opath)
m=[]
for w in wfile:
    qExist = os.path.exists(opath+'\\'+w[:2])
    if not qExist:
        os.mkdir(opath+'\\'+w[:2])
    else:
        pass
    m.append(w[:2])
#删除重复值
mm = np.array(m)
cc = np.unique(mm)    
#移动文件到指定文件夹
ufile = os.listdir(opath)
for u in ufile:
    if u[-3:] == 'csv':
        for c in cc:
            if u[:2] == c:
                try:
                    shutil.move(opath+'\\'+u,opath+'\\'+c+'\\'+u)
                except:
                    pass
                
afile = os.listdir(opath)
for a in afile:
    shutil.move(opath+'\\'+a,
                r'C:\Users\DELL\Desktop\处理数据\按日期排序\ibutton\6月份'+'\\'+a)
    
    
    
    
    
    
    