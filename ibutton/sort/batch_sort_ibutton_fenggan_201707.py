# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 20:11:32 2018

@author: DELL
"""

#此程序用于分离 风杆 不同高度不同日期的空气温度数据  -7月份
import os
import glob
import shutil
import pandas as pd

#感觉直接复制比较方便，复制的数据也不多
ipath = r'e:\py_data\ibutton' 
opath = r'e:\py_output'

qfile = glob.glob(ipath+'\\'+'*.csv')
for q in qfile:
    data = pd.read_csv(q,names=['0','1','2'],engine='python')
    sample = data.ix[22,'0'][-4:]
    for i in range(1,9):
        
        po = str(i)
        start = '17-'+'7'+'-'+po+' 0:0' + sample   #这样可以得到所需的时段
        end = '17-'+'7'+'-'+po+' 23:5' + sample    #只需要修改月份的数字
        a = data[(data.ix[:,0] == start)].index.tolist()  
        b = data[(data.ix[:,0] == end)].index.tolist()
        f = data.ix[a[0]:b[0],:]
         
        if i < 10:
            qExsit = os.path.exists(opath+'\\'+'2017070'+str(i))
            if not qExsit:
                os.mkdir(opath+'\\'+'2017070'+str(i))
            else:
                pass
            if q[-7] == '1':
                f.to_csv('e:\\py_output\\'+'2017070'+str(i)+'\\'+q[-7:-4]+'-2017070'+str(i)+'.csv')
            else:
                f.to_csv(r'e:\\py_output\\'+'2017070'+str(i)+'\\'+q[-6:-4]+'-2017070'+str(i)+'.csv')
        elif i >= 10:
 
            tExsit = os.path.exists(opath+'\\'+'201707'+str(i))
            if not tExsit:
                os.mkdir(opath+'\\'+'201707'+str(i))
            else:
                pass            
            if q[-7] == '1':
                                     
                f.to_csv('e:\\py_output\\'+'201707'+str(i)+'\\'+q[-7:-4]+'-201707'+str(i)+'.csv')    
            else:
                f.to_csv(r'e:\\py_output\\'+'201707'+str(i)+'\\'+q[-6:-4]+'-201707'+str(i)+'.csv')
                #建议还是按照这种方式生成文件夹，比较方便，不需要另外再去匹配数据
spath = r'C:\Users\DELL\Desktop\处理数据\按日期排序\ibutton\风杆'
uExist = os.path.exists(spath)
if not uExist:
    os.mkdir(spath)
else:
     pass
 
wfile = os.listdir(opath)
for w in wfile:
    shutil.move(opath+'\\'+w,spath+'\\'+w)