# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 11:36:13 2018

@author: DELL
"""

#此程序用于分析不同高宽比的街谷空气温度 -5月份
import os
import glob
import shutil
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ipath = r'e:\py_data\ibutton'
spath = r'C:\Users\DELL\Desktop\处理数据\按日期排序\ibutton\5月份'
k = ['empty','sand']
l = ['data','total picture']
qfile = os.listdir(spath)
for q in qfile:
    wfile = os.listdir(spath+'\\'+q)
    for w in wfile:
        #--------------------------创建文件夹-----------------------------------#
        #创建数据和图片文件夹
        for j in l:
            qExist = os.path.exists(ipath+'\\'+j)
            if not qExist:
                os.mkdir(ipath+'\\'+j)
            else:
                pass
        #创建日期文件夹
        for i in k:
            for h in range(1,7):
                wExist = os.path.exists(ipath+'\\'+r'data'+'\\'+w[-12:-4]+'\\'+i+'\\'+str(h))
                if not wExist:
                    os.makedirs(ipath+'\\'+r'data'+'\\'+w[-12:-4]+'\\'+i+'\\'+str(h))
                else:
                    pass
#---------------------------------移动数据到指定文件夹----------------------------#
#先聚集相同日期的文件
ufile = os.listdir(spath)
for u in ufile:
    pfile = os.listdir(spath+'\\'+u)
    sfile = os.listdir(ipath+'\\'+r'data')
    for p in pfile:
        for s in sfile:
            if p[-12:-4] == s:
                try:
                    shutil.copyfile(spath+'\\'+u+'\\'+p,ipath+'\\'+r'data'+'\\'+s+'\\'+p)
                except:
                    pass
#先聚集中空或装沙模型
dfile = os.listdir(ipath+'\\'+r'data')
for d in dfile:
    ffile = os.listdir(ipath+'\\'+r'data'+'\\'+d)
    for f in ffile:
        if f[-3:] == 'csv':
            for em in ['B','C','F']:
                if f[0] == em:
                    try:
                        shutil.move(ipath+'\\'+r'data'+'\\'+d+'\\'+f,
                                    ipath+'\\'+r'data'+'\\'+d+'\\'+r'empty'+'\\'+f)
                    except:
                        pass
            for sa in ['A','D','E']:
                if f[0] == sa:
                    try:
                        shutil.move(ipath+'\\'+r'data'+'\\'+d+'\\'+f,
                                    ipath+'\\'+r'data'+'\\'+d+'\\'+r'sand'+'\\'+f)
                    except:
                        pass
#再聚集不同高度
gfile = os.listdir(ipath+'\\'+r'data')
for g in gfile:
    hfile = os.listdir(ipath+'\\'+r'data'+'\\'+g)
    for hf in hfile:
        zfile = os.listdir(ipath+'\\'+r'data'+'\\'+g+'\\'+hf)
        for z in zfile:
            if z[-3:] == 'csv':
                for h in range(1,7):
                    if z[1] == str(h):
                        try:
                            shutil.move(ipath+'\\'+r'data'+'\\'+g+'\\'+hf+'\\'+z,
                                        ipath+'\\'+r'data'+'\\'+g+'\\'+hf+'\\'+str(h)+'\\'+z)
                        except:
                            pass
#---------------------------------画图-----------------------------------------#
vfile = os.listdir(ipath+'\\'+r'data')
for v in vfile:
    bfile = os.listdir(ipath+'\\'+r'data'+'\\'+v)
    for b in bfile:
        bbfile = os.listdir(ipath+'\\'+r'data'+'\\'+v+'\\'+b)
        for bb in bbfile:
            cc = glob.glob(ipath+'\\'+r'data'+'\\'+v+'\\'+b+'\\'+bb+'\\'+'*.csv')
            dict = {'1':'10cm','2':'30cm','3':'60cm','4':'144cm','5':'144cm-north','6':'144cm-south'}
            if len(cc) == 3:
                if b == 'empty':
                    data1 = pd.read_csv(cc[0]) # B-HW1
                    data2 = pd.read_csv(cc[2]) # F-HW2
                    data3 = pd.read_csv(cc[1]) # C-HW3
                    
                else:
                    data1 = pd.read_csv(cc[2]) # E-HW1
                    data2 = pd.read_csv(cc[0]) # A-HW2
                    data3 = pd.read_csv(cc[1]) # D-HW3
                    
                x = np.arange(144)
                y1 = data1.iloc[:,3] 
                y2 = data2.iloc[:,3]
                y3 = data3.iloc[:,3]

                fig = plt.figure(figsize=(12,9))
                ax = fig.add_subplot(1,1,1)
                
                plt.plot(x,y1,linestyle='-',marker='D',markersize=5,markerfacecolor='none',markevery=6,linewidth=0.8,label=b+'-HW1-'+dict[bb]+'-'+v)
                plt.plot(x,y2,linestyle='-',marker='o',markersize=5,markerfacecolor='none',markevery=6,linewidth=0.8,label=b+'-HW2-'+dict[bb]+'-'+v)
                plt.plot(x,y3,linestyle='-',marker='s',markersize=5,markerfacecolor='none',markevery=6,linewidth=0.8,label=b+'-HW3-'+dict[bb]+'-'+v)
    
                plt.xlim(0,144)
                plt.ylim(22,42)
                plt.xlabel('time',fontsize = 12)
                plt.ylabel('Temperature(℃)',rotation = 90,fontsize = 12)
                plt.minorticks_on()
                xticks = ax.set_xticks([0,24,48,72,96,120,144])  #此命令行可以确定x轴标签的位置
                xlabels = ax.set_xticklabels(['0:00','4:00','8:00','12:00','16:00','20:00','24:00'])  #此命令行可以命名x坐标轴的标签内容
                yticks = ax.set_yticks([22,26,30,34,38,42])
                ylabels = ax.set_yticklabels(['22','26','30','34','38','42'])
                plt.legend(loc='best',fontsize = 14,markerscale = 1) #这里可以修改legend中marker的大小
                plt.title('The air temperature',fontsize=12)
                plt.grid(True,linestyle='--')
                
                plt.savefig(ipath+'\\'+r'total picture'+'\\'+b+'-'+dict[bb]+'-'+r'different HW-'+v+'.png')
                plt.savefig(ipath+'\\'+r'data'+'\\'+v+'\\'+b+'\\'+bb+'\\'+b+'-'+dict[bb]+'-'+r'different HW-'+v+'.png')                                
                plt.close()
#--------------------------移动结果到最终文件夹-----------------------------------#                
kpath = r'C:\Users\DELL\Desktop\处理数据\picture\ibutton\10min平均\5月份\对比不同高宽比'
gExist = os.path.exists(kpath)
if not gExist:
    os.makedirs(kpath)
else:
    pass

mfile = os.listdir(ipath)
for m in mfile:
    shutil.move(ipath+'\\'+m,kpath+'\\'+m)                        