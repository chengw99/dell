# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 16:00:01 2018

@author: DELL
"""

#此程序用于对比热电偶和ibutton在同一高度的空气温度数据
#两个仪器时间不太统一，只分析20170511的温度数据好了
#先获取热电偶数据
import os
import shutil
import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

spath = r'C:\Users\DELL\Desktop\处理数据\picture'
opath = r'e:\py_output'
l = ['1','2','3','5']
k = ['data','total picture']

for j in k:
    qExist = os.path.exists(opath+'\\'+j)
    if not qExist:
        os.mkdir(opath+'\\'+j)
    else:
        pass
#-----------------------------准备数据-----------------------------------------#
#热电偶数据
try:
    shutil.copytree(spath+'\\'+r'thermo\空气-对比不同高度\data\20170511',opath+'\\'+r'data'+'\\'+r'20170511')
except:
    pass
#备注是热电偶的数据
ufile = os.listdir(opath+'\\'+r'data'+'\\'+r'20170511')
for u in ufile:
    vfile = os.listdir(opath+'\\'+r'data'+'\\'+r'20170511'+'\\'+u)
    for v in vfile:
        if v[-3:] == 'csv':
            try:
                shutil.move(opath+'\\'+r'data'+'\\'+r'20170511'+'\\'+u+'\\'+v,
                            opath+'\\'+r'data'+'\\'+r'20170511'+'\\'+u+'\\'+'thermoc-'+v)
            except:
                pass
        else:
            os.unlink(opath+'\\'+r'data'+'\\'+r'20170511'+'\\'+u+'\\'+v)
#ibutton数据
qfile = os.listdir(spath+'\\'+r'ibutton\10min平均\5月份\对比不同高度\data\20170511')
for q in qfile:
    wfile = os.listdir(spath+'\\'+r'ibutton\10min平均\5月份\对比不同高度\data\20170511'+'\\'+q)
    nfile = os.listdir(opath+'\\'+r'data'+'\\'+r'20170511')
    for w in wfile:
        for n in nfile:
            if w[-3:] == 'csv':
                for i in l:
                    if w[1] == i:
                        if n[0] == w[0]:
                            try:
                                shutil.copyfile(spath+'\\'+r'ibutton\10min平均\5月份\对比不同高度\data\20170511'+'\\'+q+'\\'+w,
                                                opath+'\\'+r'data'+'\\'+r'20170511'+'\\'+n+'\\'+'ibutton-'+w)
                            except:
                                pass
#分类创建文件夹，分类数据

cfile = os.listdir(opath+'\\'+r'data\20170511')
for c in cfile:
    for i in l:
        tExist = os.path.exists(opath+'\\'+r'data\20170511'+'\\'+c+'\\'+i)
        if not tExist:
            os.mkdir(opath+'\\'+r'data\20170511'+'\\'+c+'\\'+i)
        else:
            pass
    bfile = os.listdir(opath+'\\'+r'data\20170511'+'\\'+c)
    for b in bfile:
        if b[-3:] == 'csv':
            for a in l[0:3]:
                if b[9] == a:
                    try:
                        shutil.move(opath+'\\'+r'data\20170511'+'\\'+c+'\\'+b,
                                    opath+'\\'+r'data\20170511'+'\\'+c+'\\'+a+'\\'+b)
                    except:
                        pass
            if b[9] == '4' or '5':
                try:
                    shutil.move(opath+'\\'+r'data\20170511'+'\\'+c+'\\'+b,
                                opath+'\\'+r'data\20170511'+'\\'+c+'\\'+'5'+'\\'+b)
                except:
                    pass
#---------------------------------画图-----------------------------------------#
q_file = os.listdir(opath+'\\'+r'data\20170511')
for qq in q_file:
    rfile = os.listdir(opath+'\\'+r'data\20170511'+'\\'+qq)
    for r in rfile:
        g = glob.glob(opath+'\\'+r'data\20170511'+'\\'+qq+'\\'+r+'\\'+'*.csv')
        
        if len(g) == 2:
            data1 = pd.read_csv(g[0]) # ibutton 
            data2 = pd.read_csv(g[1]) # thermo
            
            x = np.arange(144)
            y1 = data1.ix[:,3]
            y2 = data2.ix[:,'Temperature']
            
            fig = plt.figure(figsize=(12,9),dpi=160)
            ax = fig.add_subplot(1,1,1)
                    
            plt.plot(x,y1,linestyle='-',marker='D',markersize=7,markerfacecolor='none',markevery=6,linewidth=1,label='ibutton-'+r+'-20170511')
            plt.plot(x,y2,linestyle='-',marker='o',markersize=7,markerfacecolor='none',markevery=6,linewidth=1,label='thermo-'+r+'-20170511')
            
            plt.xlim(0,144)
            plt.ylim(22,42)
            plt.xlabel('time',fontsize = 12)
            plt.ylabel('Temperature(℃)',rotation = 90,fontsize = 12)
            plt.minorticks_on()
            xticks = ax.set_xticks([0,24,48,72,96,120,144])  #此命令行可以确定x轴标签的位置
            xlabels = ax.set_xticklabels(['0:00','4:00','8:00','12:00','16:00','20:00','24:00'])  #此命令行可以命名x坐标轴的标签内容
            yticks = ax.set_yticks([22,26,30,34,38,42])
            ylabels = ax.set_yticklabels(['22','26','30','34','38','42'])
            plt.legend(loc='best',fontsize = 16,markerscale = 1) #这里可以修改legend中marker的大小
            plt.title('The temperature difference between ibutton and thermo',fontsize=16)
            plt.grid(True,linestyle='--')
    
            plt.savefig(opath+'\\'+r'total picture'+'\\'+qq+'-'+r+'-20170511'+'.png')
            plt.savefig(opath+'\\'+r'data\20170511'+'\\'+qq+'\\'+r+'\\'+qq+'-'+r+'-20170511'+'.png')
            plt.close()            









