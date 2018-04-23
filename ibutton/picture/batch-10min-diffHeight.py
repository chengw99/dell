# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 09:34:17 2018

@author: DELL
"""

#此程序用于批量画图-5月份-空气温度-对比不同高度
#非常高兴找到了画间隔标记的方法！
import os
import glob
import shutil
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ipath = r'e:\py_data\ibutton'
spath = r'C:\Users\DELL\Desktop\处理数据\按日期排序\ibutton\5月份'
k = ['A-HW2- sandy','B-HW1-empty','C-HW3-empty','D-HW3- sandy','E-HW1- sandy','F-HW2-empty']
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
        wExist = os.path.exists(ipath+'\\'+r'data'+'\\'+w[-12:-4])
        if not wExist:
            os.mkdir(ipath+'\\'+r'data'+'\\'+w[-12:-4])
        else:
            pass
        for i in k:
            rExist = os.path.exists(ipath+'\\'+r'data'+'\\'+w[-12:-4]+'\\'+i)
            if not rExist:
                os.mkdir(ipath+'\\'+r'data'+'\\'+w[-12:-4]+'\\'+i)
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
#再聚集相同街谷的文件
dfile = os.listdir(ipath+'\\'+r'data')
for d in dfile:
    ffile = os.listdir(ipath+'\\'+r'data'+'\\'+d)
    for f in ffile:
        if f[-3:] == 'csv':
            for i in k:
                if f[0] == i[0]:
                    try:
                        shutil.move(ipath+'\\'+r'data'+'\\'+d+'\\'+f,
                                        ipath+'\\'+r'data'+'\\'+d+'\\'+i+'\\'+f)
                    except:
                        pass
                    
#---------------------------------画图-----------------------------------------#
gfile = os.listdir(ipath+'\\'+r'data')
for g in gfile:
    zfile = os.listdir(ipath+'\\'+r'data'+'\\'+g)
    for z in zfile:
        cfile = glob.glob(ipath+'\\'+r'data'+'\\'+g+'\\'+z+'\\*.csv')
        if len(cfile) == 6:
            #读取数据
            data1 = pd.read_csv(cfile[0]) # 10cm
            data2 = pd.read_csv(cfile[1]) # 30cm
            data3 = pd.read_csv(cfile[2]) # 60cm
            data4 = pd.read_csv(cfile[3]) # 144cm
            data5 = pd.read_csv(cfile[4]) # 144cm-N
            data6 = pd.read_csv(cfile[5]) # 144cm-S
            
            x = np.arange(144)
            y1 = data1.iloc[:,3]
            y2 = data2.iloc[:,3]
            y3 = data3.iloc[:,3]
            y4 = data4.iloc[:,3]
            y5 = data5.iloc[:,3]
            y6 = data6.iloc[:,3]
            
            fig = plt.figure(figsize=(12,9))
            ax = fig.add_subplot(1,1,1)
                        
            plt.plot(x,y1,linestyle='-',marker='D',markersize=5,markerfacecolor='none',markevery=6,linewidth=0.8,label=z+'-'+r'h=0.1m-'+g)
            plt.plot(x,y2,linestyle='-',marker='o',markersize=5,markerfacecolor='none',markevery=6,linewidth=0.8,label=z+'-'+r'h=0.3m-'+g)
            plt.plot(x,y3,linestyle='-',marker='v',markersize=5,markerfacecolor='none',markevery=6,linewidth=0.8,label=z+'-'+r'h=0.6m-'+g)
            plt.plot(x,y4,linestyle='-',marker='s',markersize=5,markerfacecolor='none',markevery=6,linewidth=0.8,label=z+'-'+r'h=1.44m-'+g)
            #plt.plot(x,y5,linestyle='-',marker='x',markersize=5,markerfacecolor='none',markevery=6,linewidth=0.8,label=z+'-'+r'h=1.44m-north-'+g)
            #plt.plot(x,y6,linestyle='-',marker='^',markersize=5,markerfacecolor='none',markevery=6,linewidth=0.8,label=z+'-'+r'h=1.44m-south-'+g)
            
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
            plt.savefig(ipath+'\\'+r'data'+'\\'+g+'\\'+z+'\\'+z+'-differentHeight-'+g+'.png')
            plt.savefig(ipath+'\\'+r'total picture'+'\\'+z+'-differentHeight-'+g+'.png')
            plt.close()
            
        #E模型缺测144cm高度的数据
        if len(cfile) == 5:
            
            #读取数据
            data1 = pd.read_csv(cfile[0]) # 10cm
            data2 = pd.read_csv(cfile[1]) # 30cm
            data3 = pd.read_csv(cfile[2]) # 60cm
            data4 = pd.read_csv(cfile[3]) # 144cm-N
            data5 = pd.read_csv(cfile[4]) # 144cm-S
            
            x = np.arange(144)
            y1 = data1.iloc[:,3]
            y2 = data2.iloc[:,3]
            y3 = data3.iloc[:,3]
            y4 = data4.iloc[:,3]
            y5 = data5.iloc[:,3]
            
            fig = plt.figure(figsize=(12,9))
            ax = fig.add_subplot(1,1,1)
                        
            plt.plot(x,y1,linestyle='-',marker='D',markersize=5,markerfacecolor='none',markevery=6,linewidth=0.8,label=z+'-'+r'h=0.1m-'+g)
            plt.plot(x,y2,linestyle='-',marker='o',markersize=5,markerfacecolor='none',markevery=6,linewidth=0.8,label=z+'-'+r'h=0.3m-'+g)
            plt.plot(x,y3,linestyle='-',marker='v',markersize=5,markerfacecolor='none',markevery=6,linewidth=0.8,label=z+'-'+r'h=0.6m-'+g)
            plt.plot(x,y4,linestyle='-',marker='x',markersize=5,markerfacecolor='none',markevery=6,linewidth=0.8,label=z+'-'+r'h=1.44m-north-'+g)
            #plt.plot(x,y5,linestyle='-',marker='^',markersize=5,markerfacecolor='none',markevery=6,linewidth=0.8,label=z+'-'+r'h=1.44m-south-'+g)
            
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
            plt.savefig(ipath+'\\'+r'data'+'\\'+g+'\\'+z+'\\'+z+'-differentHeight-'+g+'.png')
            plt.savefig(ipath+'\\'+r'total picture'+'\\'+z+'-differentHeight-'+g+'.png')
            plt.close()
  
#--------------------------移动结果到最终文件夹-----------------------------------#                
kpath = r'C:\Users\DELL\Desktop\处理数据\picture\ibutton\10min平均\对比不同高度'
gExist = os.path.exists(kpath)
if not gExist:
    os.mkdir(kpath)
else:
    pass

mfile = os.listdir(ipath)
for m in mfile:
    shutil.move(ipath+'\\'+m,kpath+'\\'+m)           
            
            
            
            
            
            
            
            















        