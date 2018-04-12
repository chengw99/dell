# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 13:29:55 2018

@author: DELL
"""

#此程序用于批量分类数据和画图--不同建筑热容+朝南朝北侧壁
import os
import glob
import shutil
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ipath = r'e:\py_data\thermo'
spath = r'C:\Users\DELL\Desktop\处理数据\picture\thermo\对比不同建筑热容'
l = ['30cm','60cm','90cm','110cm']
k = ['HW1','HW2','HW3']
#复制数据到工作目录
qfile = os.listdir(spath)
for q in qfile[1:2]:
    try:
        shutil.copytree(spath+'\\'+q+'\\'+r'20170511',ipath+'\\'+q+'\\'+r'20170511')
    except:
        pass
#创建文件夹
qExist = os.path.exists(ipath+'\\'+r'south model-facing north')
if not qExist:
    os.mkdir(ipath+'\\'+r'south model-facing north')
else:
    pass
#把其中一个文件夹里面的csv文件遍历出来
for q in qfile[2:3]:
    wfile = os.listdir(spath+'\\'+q+'\\'+r'20170511')
    for w in wfile:
        tfile = os.listdir(spath+'\\'+q+'\\'+r'20170511'+'\\'+w)
        for t in tfile:
            ufile = os.listdir(spath+'\\'+q+'\\'+r'20170511'+'\\'+w+'\\'+t)
            for u in ufile:
                if u[-3:] == 'csv':
                    try:
                        shutil.copyfile(spath+'\\'+q+'\\'+r'20170511'+'\\'+w+'\\'+t+'\\'+u,
                                        ipath+'\\'+r'south model-facing north'+'\\'+u)
                    except:
                        pass
#将不同朝向不同建筑热容放进同一个文件夹
pfile = os.listdir(ipath+'\\'+r'south model-facing north')
for p in pfile:
    if p[43:48] == '110cm':
            try:
                shutil.move(ipath+'\\'+r'south model-facing north'+'\\'+p,
                            ipath+'\\'+r'north model-facing south'+'\\'+r'20170511'+'\\'+r'110cm'+'\\'+p)
            except:
                pass
    for i in l[0:3]:
        if p[43:47] == i:
            try:
                shutil.move(ipath+'\\'+r'south model-facing north'+'\\'+p,
                            ipath+'\\'+r'north model-facing south'+'\\'+r'20170511'+'\\'+i+'\\'+p)
            except:
                pass
afile = os.listdir(ipath+'\\'+r'north model-facing south'+'\\'+r'20170511')
for a in afile:
    if a == '30cm' or '60cm' or '90cm':
        sfile = os.listdir(ipath+'\\'+r'north model-facing south'+'\\'+r'20170511'+'\\'+a)
        for s in sfile:
            if s[-3:] == 'csv':
                for j in k:
                    if s[50:53] == j:
                        try:
                            shutil.move(ipath+'\\'+r'north model-facing south'+'\\'+r'20170511'+'\\'+a+'\\'+s,
                                        ipath+'\\'+r'north model-facing south'+'\\'+r'20170511'+'\\'+a+'\\'+j+'\\'+s)
                        except:
                            pass
    if a == '110cm':
        sfile = os.listdir(ipath+'\\'+r'north model-facing south'+'\\'+r'20170511'+'\\'+a)
        for s in sfile:
            if s[-3:] == 'csv':
                for j in k:
                    if s[51:54] == j:
                        try:
                            shutil.move(ipath+'\\'+r'north model-facing south'+'\\'+r'20170511'+'\\'+a+'\\'+s,
                                        ipath+'\\'+r'north model-facing south'+'\\'+r'20170511'+'\\'+a+'\\'+j+'\\'+s)
                        except:
                            pass
try:
    shutil.rmtree(ipath+'\\'+r'south model-facing north')
    shutil.move(ipath+'\\'+r'north model-facing south',ipath+'\\'+r'data')                
except:
    pass
#----------------------------画图---------------------------------------------#
gfile = os.listdir(ipath+'\\'+r'data'+'\\'+r'20170511')
for g in gfile:
    hfile = os.listdir(ipath+'\\'+r'data'+'\\'+r'20170511'+'\\'+g)
    for h in hfile:
        zfile = os.listdir(ipath+'\\'+r'data'+'\\'+r'20170511'+'\\'+g+'\\'+h)
        for z in zfile:
            if z[-3:] == 'png':
                try:
                    os.unlink(ipath+'\\'+r'data'+'\\'+r'20170511'+'\\'+g+'\\'+h+'\\'+z)
                except:
                    pass
        cfile = glob.glob(ipath+'\\'+r'data'+'\\'+r'20170511'+'\\'+g+'\\'+h+'\\'+'*.csv')
        if len(cfile) == 4:
            if h == 'HW1' or 'HW3':
                data1 = pd.read_csv(cfile[0]) # north south empty
                data2 = pd.read_csv(cfile[1]) # north south sand
                data3 = pd.read_csv(cfile[2]) # south north empty
                data4 = pd.read_csv(cfile[3]) # south north sand
            if h == 'HW2':
                data1 = pd.read_csv(cfile[1]) # north south sand
                data2 = pd.read_csv(cfile[0]) # north south empty
                data3 = pd.read_csv(cfile[3]) # south north sand
                data4 = pd.read_csv(cfile[2]) # south north empty
            
            x = np.arange(144)
            y1 = data1.loc[:,'Temperature']
            y2 = data2.loc[:,'Temperature']
            y3 = data3.loc[:,'Temperature']
            y4 = data4.loc[:,'Temperature']
            
            fig = plt.figure()
            ax  = fig.add_subplot(1,1,1)     

            plt.plot(x,y1,marker='D',markersize = 0.5,linewidth = 1,label = 'north model-facing south-empty')
            plt.plot(x,y2,marker='^',markersize = 0.5,linewidth = 1,label = 'north model-facing south-sand')
            plt.plot(x,y3,marker='s',markersize = 0.5,linewidth = 1,label = 'south model-facing north-empty')
            plt.plot(x,y4,marker='v',markersize = 0.5,linewidth = 1,label = 'south model-facing north-sand')
                             
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
            
            rExist = os.path.exists(ipath+'\\'+r'total picture')
            if not rExist:
                os.mkdir(ipath+'\\'+r'total picture')
            else:
                pass
            plt.savefig(ipath+'\\'+r'total picture'+'\\'+g+'-'+h+'.png')
            plt.savefig(ipath+'\\'+r'data'+'\\'+r'20170511'+'\\'+g+'\\'+h+'\\'+g+'-'+h+'.png')
            plt.close()
kpath = r'C:\Users\DELL\Desktop\处理数据\picture\thermo\不同建筑热容+侧壁不同朝向'
gExist = os.path.exists(kpath)
if not gExist:
    os.mkdir(kpath)
else:
    pass

gfile = os.listdir(ipath)
for g in gfile:
    shutil.move(ipath+'\\'+g,kpath+'\\'+g)

