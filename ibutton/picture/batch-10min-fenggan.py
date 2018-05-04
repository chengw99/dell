# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 20:21:48 2018

@author: DELL
"""

#此程序用于批量画图-风杆-6月份和7月份
import os
import glob
import shutil
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ipath = r'e:\py_data\ibutton'
spath = r'C:\Users\DELL\Desktop\处理数据\按日期排序\ibutton\风杆'
l = ['data','total picture']
for ll in l:
    pExist = os.path.exists(ipath+'\\'+ll)
    if not pExist:
        os.mkdir(ipath+'\\'+ll)
    else:
        pass
#将数据复制到工作目录
qfile = os.listdir(spath)
for q in qfile:
    try:
        shutil.copytree(spath+'\\'+q,ipath+'\\'+r'data'+'\\'+q)
    except:
        pass
#画图
wfile = os.listdir(ipath+'\\'+r'data')
for w in wfile:
    tfile = glob.glob(ipath+'\\'+r'data'+'\\'+w+'\\'+'*.csv')
    if len(tfile) == 4:
        data1 = pd.read_csv(tfile[1]) # 2m
        data2 = pd.read_csv(tfile[2]) # 4m
        data3 = pd.read_csv(tfile[3]) # 6m
        data4 = pd.read_csv(tfile[0]) # 10m
        
        x = np.arange(144)
        y1 = data1.iloc[:,3] 
        y2 = data2.iloc[:,3]
        y3 = data3.iloc[:,3]
        y4 = data4.iloc[:,3]
                
        fig = plt.figure(figsize=(12,9),dpi=160)
        ax = fig.add_subplot(1,1,1)
                
        plt.plot(x,y1,linestyle='-',marker='D',markersize=5,markerfacecolor='none',markevery=6,linewidth=0.8,label='2m'+'-'+w)
        plt.plot(x,y2,linestyle='-',marker='o',markersize=5,markerfacecolor='none',markevery=6,linewidth=0.8,label='4m'+'-'+w)
        plt.plot(x,y3,linestyle='-',marker='s',markersize=5,markerfacecolor='none',markevery=6,linewidth=0.8,label='6m'+'-'+w)
        plt.plot(x,y4,linestyle='-',marker='d',markersize=5,markerfacecolor='none',markevery=6,linewidth=0.8,label='10m'+'-'+w)

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
        
        plt.savefig(ipath+'\\'+r'total picture'+'\\'+'fenggan different height-'+w+'.png')
        plt.savefig(ipath+'\\'+r'data'+'\\'+w+'\\'+'fenggan different height-'+w+'.png')
        plt.close()
#--------------------------移动结果到最终文件夹-----------------------------------#                
kpath = r'C:\Users\DELL\Desktop\处理数据\picture\ibutton\10min平均\风杆不同高度'
gExist = os.path.exists(kpath)
if not gExist:
    os.makedirs(kpath)
else:
    pass

mfile = os.listdir(ipath)
for m in mfile:
    shutil.move(ipath+'\\'+m,kpath+'\\'+m)  