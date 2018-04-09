# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 11:21:01 2018

@author: DELL
"""
#此修正版的意义在于弄清楚了为什么之前会占用文件夹导致无法删除干净！
#在于os.chdir,改用glob打开文件就可以

#此程序用于将中空-装沙模型的数据进行分类
#分类标准是 HW1-HW2-HW3--不同日期
#对比的标准是不同高度
import os
import shutil
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ipath = r'e:\py_data\thermo'
spath = r'C:\Users\DELL\Desktop\处理数据\picture\thermo\中空-装沙\south model-facing north-汇总' #修改此处路径可换不同模型的朝向
#----------------------------创建文件夹和复制数据---------------------------------#
l = ['HW1','HW2','HW3']
for i in l:
    qExist = os.path.exists(ipath+'\\'+i)
    if not qExist:
        os.mkdir(ipath+'\\'+i)
    else:
        pass
#复制数据
qfile = os.listdir(spath)
for q in qfile:
    wfile = os.listdir(spath+'\\'+q)
    for w in wfile:
        tfile = os.listdir(spath+'\\'+q+'\\'+r'data')
        for t in tfile:
            for j in l:
                if t[-16:-13] == j:
                    try:
                        shutil.copyfile(spath+'\\'+q+'\\'+r'data'+'\\'+t,
                                        ipath+'\\'+j+'\\'+t)
                    except:
                        pass
for k in l:
    ufile = os.listdir(ipath+'\\'+k)
    for u in ufile:
        wExist = os.path.exists(ipath+'\\'+k+'\\'+u[-12:-4])
        if not wExist:
            os.mkdir(ipath+'\\'+k+'\\'+u[-12:-4])
        else:
            pass
b=[]
for i in l:
    gfile = os.listdir(ipath+'\\'+i)
    for g in gfile:
        if g[-3:] != 'csv':
            b.append(g)
bb = np.array(b)
date = np.unique(bb)
#移动数据
for k in l:
    vfile = os.listdir(ipath+'\\'+k)
    for v in vfile:
        if v[-3:] == 'csv':
            for j in date:
                if v[-12:-4] == j:
                    try:
                        shutil.move(ipath+'\\'+k+'\\'+v,ipath+'\\'+k+'\\'+j+'\\'+v)
                    except:
                        pass
#----------------------------画图----------------------------------------------#
for i in l:
    dfile = os.listdir(ipath+'\\'+i)
    for d in dfile:
        sfile = glob.glob(ipath+'\\'+i+'\\'+d+'\\'+'*.csv') #与上个程序不同的是此处
        
        if len(sfile) == 4:
            
            data1 = pd.read_csv(sfile[1]) # 30cm
            data2 = pd.read_csv(sfile[2]) # 60cm
            data3 = pd.read_csv(sfile[3]) # 90cm
            data4 = pd.read_csv(sfile[0]) # 110cm
            
            y1 = data1.loc[:,'Temperature']
            y2 = data2.loc[:,'Temperature']
            y3 = data3.loc[:,'Temperature']
            y4 = data4.loc[:,'Temperature']
            
            x  = np.arange(144)
            
            fig = plt.figure()
            ax  = fig.add_subplot(1,1,1)     
            
            plt.plot(x,y1,marker = 'D',markersize = 0.5,linewidth = 1,label = sfile[1][-21:-4])
            plt.plot(x,y2,marker = 's',markersize = 0.5,linewidth = 1,label = sfile[2][-21:-4])
            plt.plot(x,y3,marker = '^',markersize = 0.5,linewidth = 1,label = sfile[3][-21:-4])
            plt.plot(x,y4,marker = 'v',markersize = 0.5,linewidth = 1,label = sfile[0][-22:-4])

            plt.xlim(0,143)
            plt.ylim(-6,6)
            plt.xlabel('time',fontsize = 12)
            plt.ylabel('T(℃)',rotation = 90,fontsize = 12)
            plt.minorticks_on()
            xticks = ax.set_xticks([0,24,48,72,96,120,143])  #此命令行可以确定x轴标签的位置
            xlabels = ax.set_xticklabels(['0:00','4:00','8:00','12:00','16:00','20:00','24:00'])  #此命令行可以命名x坐标轴的标签内容
            yticks = ax.set_yticks([-6,-4,-2,0,2,4,6])
            ylabels = ax.set_yticklabels(['-6','-4','-2','0','2','4','6'])
            #设置图注
            plt.legend(loc='best',fontsize = 10)
            plt.grid(True,linestyle='--')
            uExsit = os.path.exists(ipath+'\\'+r'total picture')
            if not uExsit:
                os.mkdir(ipath+'\\'+r'total picture')
            else:
                pass
            plt.savefig(ipath+'\\'+r'total picture'+'\\'+str(i)+'-'+str(d)+'.png')
            plt.savefig(ipath+'\\'+i+'\\'+d+'\\'+str(i)+'-'+str(d)+'.png')
            plt.close()
kpath = r'C:\Users\DELL\Desktop\处理数据\picture\thermo\中空-装沙-不同高度'
pExist = os.path.exists(kpath+'\\'+r'data')
if not pExist:
    os.makedirs(kpath+'\\'+r'data')
else:
    pass
zfile = os.listdir(ipath)
for z in zfile[0:3]:
    try:
        shutil.move(ipath+'\\'+z,kpath+'\\'+r'data'+'\\'+z)
    except:
        pass
shutil.move(ipath+'\\'+r'total picture',kpath+'\\'+r'total picture')