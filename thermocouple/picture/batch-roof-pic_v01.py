# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 19:52:37 2018

@author: DELL
"""
#--------------v01---------------------------#
#此程序用于批量处理-- 同一个方位的屋顶温度24小时变化图
import os
import glob
import shutil
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipath = r'e:\py_data\thermo'
spath = r'C:\Users\DELL\Desktop\处理数据\分析数据\thermo\10min_average'
l = ['data','total picture']
for i in l:
    qExist = os.path.exists(ipath+'\\'+i)
    if not qExist:
        os.mkdir(ipath+'\\'+i)
    else:
        pass
qfile = os.listdir(spath)
for q in qfile[8:12]:
    try:
        shutil.copytree(spath+'\\'+q,ipath+'\\'+r'data'+'\\'+q)
    except:
        pass
for qq in qfile[16:20]:
    try:
        shutil.copytree(spath+'\\'+qq,ipath+'\\'+r'data'+'\\'+qq)
    except:
        pass
   
wfile = os.listdir(ipath+'\\'+r'data')
for w in wfile:
    tfile = os.listdir(ipath+'\\'+r'data'+'\\'+w)
    for t in tfile:
        ufile = glob.glob(ipath+'\\'+r'data'+'\\'+w+'\\'+t+'\\'+'*.csv')
        if len(ufile) == 6:
            data1 = pd.read_csv(ufile[4]) #sand model 1:1
            data2 = pd.read_csv(ufile[0]) #sand model 2:1
            data3 = pd.read_csv(ufile[3]) #sand model 3:1
            data4 = pd.read_csv(ufile[1]) #empty model 1:1
            data5 = pd.read_csv(ufile[5]) #empty model 2:1
            data6 = pd.read_csv(ufile[2]) #empty model 3:1
            
            y1 = data1.loc[:,'Temperature']
            y2 = data2.loc[:,'Temperature']
            y3 = data3.loc[:,'Temperature']
            y4 = data4.loc[:,'Temperature']
            y5 = data5.loc[:,'Temperature']
            y6 = data6.loc[:,'Temperature']
            
            x = np.arange(144)
            
            fig = plt.figure(figsize=(12,9))
            ax  = fig.add_subplot(1,1,1)     
            
            plt.plot(x,y1,marker='D',markersize = 0.5,linewidth = 1,label = ufile[4][-51:-4])
            plt.plot(x,y2,marker='^',markersize = 0.5,linewidth = 1,label = ufile[0][-51:-4])
            plt.plot(x,y3,marker='s',markersize = 0.5,linewidth = 1,label = ufile[3][-51:-4])
            plt.plot(x,y4,marker='v',markersize = 0.5,linewidth = 1,label = ufile[1][-52:-4])
            plt.plot(x,y5,marker='s',markersize = 0.5,linewidth = 1,label = ufile[5][-52:-4])
            plt.plot(x,y6,marker='v',markersize = 0.5,linewidth = 1,label = ufile[2][-52:-4])
            
            plt.xlim(0,143)
            plt.ylim(22,54)
            plt.xlabel('time',fontsize = 12)
            plt.ylabel('Temperature(℃)',rotation = 90,fontsize = 12)
            plt.minorticks_on()
            xticks = ax.set_xticks([0,24,48,72,96,120,143])  #此命令行可以确定x轴标签的位置
            xlabels = ax.set_xticklabels(['0:00','4:00','8:00','12:00','16:00','20:00','24:00'])  #此命令行可以命名x坐标轴的标签内容
            yticks = ax.set_yticks([22,26,30,34,38,42,46,50,54])
            ylabels = ax.set_yticklabels(['22','26','30','34','38','42','46','50','54'])
            #设置图注
            plt.legend(loc='best',fontsize = 10,markerscale = 10) #这里可以修改legend中marker的大小
            plt.grid(True,linestyle='--')
            plt.savefig(ipath+'\\'+r'data'+'\\'+w+'\\'+t+'\\'+ufile[0][-51:-30]+'-'+ufile[0][-12:-4]+'.png')
            plt.savefig(ipath+'\\'+r'total picture'+'\\'+ufile[0][-51:-30]+'-'+ufile[0][-12:-4]+'.png')
            plt.close()

kpath = r'C:\Users\DELL\Desktop\处理数据\picture\thermo\屋顶温度'
gExist = os.path.exists(kpath)
if not gExist:
    os.mkdir(kpath)
else:
    pass

gfile = os.listdir(ipath)
for g in gfile:
    shutil.move(ipath+'\\'+g,kpath+'\\'+g)







