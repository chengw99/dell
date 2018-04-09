# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 18:38:56 2018

@author: DELL
"""

#综合处理不同朝向的模型的数据
##此程序用于中空-装沙模型的数据进行分类
#分类文件夹的标准是 30cm-60cm-90cm-110cm--不同日期
#对比的标准是不同高宽比
import os
import glob
import shutil
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ipath = r'e:\py_data\thermo'
spath = r'C:\Users\DELL\Desktop\处理数据\picture\thermo\中空-装沙' 
h = ['north model-facing north-汇总','north model-facing south-汇总','south model-facing north-汇总']
l = ['30cm','60cm','90cm','110cm']
n = ['data','total picture']

for i in h:
    for c in n:
        qExist = os.path.exists(ipath+'\\'+i+'\\'+c)
        if not qExist:
            os.makedirs(ipath+'\\'+i+'\\'+c)
        else:
            pass
    for j in l:
        wExist = os.path.exists(ipath+'\\'+i+'\\'+r'data'+'\\'+j)
        if not wExist:
            os.mkdir(ipath+'\\'+i+'\\'+r'data'+'\\'+j)
        else:
            pass
#复制数据
for i in h:
    qfile = os.listdir(spath+'\\'+i)
    for q in qfile:
        wfile = os.listdir(spath+'\\'+i+'\\'+q)
        for w in wfile:
            tfile = os.listdir(spath+'\\'+i+'\\'+q+'\\'+r'data')
            for t in tfile:
                for j in l[0:3]:
                    if t[0:4] == j:
                        try:
                            shutil.copyfile(spath+'\\'+i+'\\'+q+'\\'+r'data'+'\\'+t,
                                            ipath+'\\'+i+'\\'+r'data'+'\\'+j+'\\'+t)
                        except:
                            pass
                if t[0:5] == '110cm':
                    try:
                        shutil.copyfile(spath+'\\'+i+'\\'+q+'\\'+r'data'+'\\'+t,
                                        ipath+'\\'+i+'\\'+r'data'+'\\'+r'110cm'+'\\'+t)
                    except:
                        pass
for i in h:      
    for j in l:
        ufile = os.listdir(ipath+'\\'+i+'\\'+r'data'+'\\'+j)
        for u in ufile:
            wExist = os.path.exists(ipath+'\\'+i+'\\'+r'data'+'\\'+j+'\\'+u[-12:-4])
            if not wExist:
                os.mkdir(ipath+'\\'+i+'\\'+r'data'+'\\'+j+'\\'+u[-12:-4])
            else:
                pass
b=[]
for i in h:
    for j in l:
        gfile = os.listdir(ipath+'\\'+i+'\\'+r'data'+'\\'+j)
        for g in gfile:
            if g[-3:] != 'csv':
                b.append(g)
bb = np.array(b)
date = np.unique(bb)
for i in h:
    for j in l:
        vfile = os.listdir(ipath+'\\'+i+'\\'+r'data'+'\\'+j)
        for v in vfile:
            if v[-3:] == 'csv':
                for k in date:
                    if v[-12:-4] == k:
                        try:
                            shutil.move(ipath+'\\'+i+'\\'+r'data'+'\\'+j+'\\'+v,
                                        ipath+'\\'+i+'\\'+r'data'+'\\'+j+'\\'+k+'\\'+v)
                        except:
                            pass
                        
#---------------------------画图-----------------------------------------------#
for i in h:
    for j in l:
        dfile = os.listdir(ipath+'\\'+i+'\\'+r'data'+'\\'+j)
        for d in dfile:
            sfile = glob.glob(ipath+'\\'+i+'\\'+r'data'+'\\'+j+'\\'+d+'\\'+'*.csv')
            if len(sfile) == 3:
                data1 = pd.read_csv(sfile[0],engine = 'python')
                data2 = pd.read_csv(sfile[1],engine = 'python')
                data3 = pd.read_csv(sfile[2],engine = 'python')
                
                y1 = data1.loc[:,'Temperature']
                y2 = data2.loc[:,'Temperature']
                y3 = data3.loc[:,'Temperature']
                
                x = np.arange(144)
                
                
                fig = plt.figure()
                ax  = fig.add_subplot(1,1,1)     
            
                plt.plot(x,y1,marker = 'D',markersize = 0.5,linewidth = 1,label = sfile[0][-21:-4])
                plt.plot(x,y2,marker = 's',markersize = 0.5,linewidth = 1,label = sfile[1][-21:-4])
                plt.plot(x,y3,marker = '^',markersize = 0.5,linewidth = 1,label = sfile[2][-21:-4])
                
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
                plt.savefig(ipath+'\\'+i+'\\'+r'total picture'+'\\'+str(i)+'-'+str(j)+'-'+str(d)+'.png')
                plt.savefig(ipath+'\\'+i+'\\'+r'data'+'\\'+j+'\\'+d+'\\'+str(i)+'-'+str(j)+'-'+str(d)+'.png')
                plt.close()

bpath = r'C:\Users\DELL\Desktop\处理数据\picture\thermo\中空-装沙-不同高宽比'
bExist = os.path.exists(bpath)
if not bExist:
    os.mkdir(bpath)
else:
    pass

mfile = os.listdir(ipath)
for m in mfile:
    try:
        shutil.move(ipath+'\\'+m,
                    bpath+'\\'+m)
    except:
        pass