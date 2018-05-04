# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 15:16:16 2018

@author: DELL
"""
import os
import glob
import shutil
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#-----------------------------工作路径-----------------------------------------#
ipath = r'e:\py_data\station'
gpath = r'C:\Users\DELL\Desktop\处理数据\按日期排序\station'
spath = r'C:\Users\DELL\Desktop\处理数据\picture\station'
l = ['north station','south station']

for name in l:
    #--------------------------------创建文件夹---------------------------------#
    qExist = os.path.exists(ipath+'\\'+name)
    if not qExist:
        os.mkdir(ipath+'\\'+name)
    else:
        pass
    
    wExist = os.path.exists(ipath+'\\'+name+'\\'+r'total data')
    if not wExist:
        os.mkdir(ipath+'\\'+name+'\\'+r'total data')
    else:
        pass
    k = ['data','picture']
    for i in k:
        tExist = os.path.exists(ipath+'\\'+name+'\\'+r'solar radiation'+'\\'+i)
        if not tExist:
            os.makedirs(ipath+'\\'+name+'\\'+r'solar radiation'+'\\'+i) #创建多级目录 
        else:
            pass
    #---------------------------------获取数据----------------------------------#
    file = os.listdir(gpath+'\\'+name+'\\'+r'201706')
    for f in file:
        shutil.copyfile(gpath+'\\'+name+'\\'+r'201706'+'\\'+f,
                        ipath+'\\'+name+'\\'+r'total data'+'\\'+f)

    #---------------------------------画图-------------------------------------#
    qfile = glob.glob(ipath+'\\'+name+'\\'+r'total data'+'\\'+'*.csv')
    for q in qfile:
        data = pd.read_csv(q)
    
        y = data.loc[:,'SRAD'] #选取辐射数据
        x = np.arange(144)
        
        if len(y) == 144:
            fig = plt.figure(figsize=(12,9))
            ax  = fig.add_subplot(1,1,1)
            
            plt.bar(x,y,label = 'The solar radiation'+'-'+name+'-'+q[-12:-4])
            plt.xlim(0,143) 
            plt.ylim(0,600)
            plt.xlabel('time',fontsize = 12)
            plt.ylabel('solar radiation(Watts/m2)',rotation = 90,fontsize = 12)
            xticks = ax.set_xticks([0,24,48,72,96,120,143])  #此命令行可以确定x轴标签的位置
            xlabels = ax.set_xticklabels(['0:00','4:00','8:00','12:00','16:00','20:00','24:00'])  #此命令行可以命名x坐标轴的标签内容
            yticks = ax.set_yticks([0,100,200,300,400,500,600])
            ylabels = ax.set_yticklabels(['0','100','200','300','400','500','600'])
            #设置图注
            plt.legend(loc='best',fontsize = 16)
            plt.grid(True,linestyle='--')
        
        
            plt.savefig(ipath+'\\'+name+'\\'+r'solar radiation\picture\\'+name+'-'+q[-12:-4]+'-'+'Solaradiation.png')
            plt.close()
            
            #------------------------生成数据文件--------------------------------#
            time = []
            for i in range(24):
                for j in np.linspace(0,60,num = 6,endpoint = False):
                    if j == 0:
                        time.append(str(int(i))+':0'+str(int(j)))
                    else:
                        time.append(str(int(i))+':'+str(int(j)))
        
            result = pd.DataFrame({'solar radiation':y,'time':time})
            columns = ['time','solar radiation']
            result.to_csv(ipath+'\\'+name+'\\'+r'solar radiation\data\\'+name+'-'+q[-12:-4]+'-'+'Solaradiation.csv')
        
        else:
            pass

ufile = os.listdir(ipath)
for u in ufile:
    try:
        shutil.move(ipath+'\\'+u,spath+'\\'+r'6月份'+'\\'+u)
    except:
        pass

