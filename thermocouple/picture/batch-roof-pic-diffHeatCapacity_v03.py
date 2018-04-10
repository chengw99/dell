# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 18:25:36 2018

@author: DELL
"""
#--------v03----------------#
#此程序用于对比不同建筑热容
#--------v02----------------#
#此程序用于对比不同高宽比屋顶的温度
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
k = ['HW1','HW2','HW3']

#--------------------------复制数据到工作目录------------------------------------#
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
#-------------------------------将数据分类--------------------------------------#
dfile = os.listdir(ipath+'\\'+r'data')
for d in dfile:
    ffile = os.listdir(ipath+'\\'+r'data'+'\\'+d)
    for f in ffile:
        for j in k:
            wExist = os.path.exists(ipath+'\\'+r'data'+'\\'+d+'\\'+f+'\\'+j)
            if not wExist:
                os.mkdir(ipath+'\\'+r'data'+'\\'+d+'\\'+f+'\\'+j)
            else:
                pass
        gfile = os.listdir(ipath+'\\'+r'data'+'\\'+d+'\\'+f)
        for g in gfile:
            if g[-3:] == 'csv':
                if g[33:37] == 'west' or 'east':
                    for n in k:
                        if g[40:43] == n:
                            try:
                                shutil.move(ipath+'\\'+r'data'+'\\'+d+'\\'+f+'\\'+g,
                                            ipath+'\\'+r'data'+'\\'+d+'\\'+f+'\\'+n+'\\'+g)
                            except:
                                pass
                if g[33:38] == 'north' or 'south': #这里之前用了elif发现不行，这是因为当一个块里的if或者任何一个elif判断为真时，后面的elif都不会执行了
                    for nn in k:
                        if g[41:44] == nn:
                            try:
                                shutil.move(ipath+'\\'+r'data'+'\\'+d+'\\'+f+'\\'+g,
                                            ipath+'\\'+r'data'+'\\'+d+'\\'+f+'\\'+nn+'\\'+g)
                            except:
                                pass
#----------------------画图----------------------------------------------------#
wfile = os.listdir(ipath+'\\'+r'data')
for w in wfile:
    tfile = os.listdir(ipath+'\\'+r'data'+'\\'+w)
    for t in tfile:
        for j in k:
            ufile = glob.glob(ipath+'\\'+r'data'+'\\'+w+'\\'+t+'\\'+j+'\\'+'*.csv')
            if len(ufile) == 2:
                data1 = pd.read_csv(ufile[0])
                data2 = pd.read_csv(ufile[1])
                
                y1 = data1.loc[:,'Temperature']
                y2 = data2.loc[:,'Temperature']
                
                x = np.arange(144)
                
                fig = plt.figure()
                ax  = fig.add_subplot(1,1,1)     
                
                plt.plot(x,y1,marker='D',markersize = 0.5,linewidth = 1,label = ufile[0][-24:-19])
                plt.plot(x,y2,marker='^',markersize = 0.5,linewidth = 1,label = ufile[1][-23:-19])
                
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
                
                plt.savefig(ipath+'\\'+r'data'+'\\'+w+'\\'+t+'\\'+j+'\\'+ufile[0][-51:-30]+'-'+ufile[0][-12:-4]+'.png')
                plt.savefig(ipath+'\\'+r'total picture'+'\\'+ufile[0][-51:-30]+'-'+ufile[0][-12:-4]+'.png')
                plt.close()
#--------------------------移动结果到最终文件夹-----------------------------------#                
kpath = r'C:\Users\DELL\Desktop\处理数据\picture\thermo\屋顶温度-不同建筑热容'
gExist = os.path.exists(kpath)
if not gExist:
    os.mkdir(kpath)
else:
    pass

gfile = os.listdir(ipath)
for g in gfile:
    shutil.move(ipath+'\\'+g,kpath+'\\'+g)

                







               