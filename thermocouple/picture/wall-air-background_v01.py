# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 09:35:45 2018

@author: DELL
"""
#----------v01-----------------------#
#此程序用于批量分类和画图 -- 壁面+空气+背景场
#此程序只处理了一天的- 20170511
import os
import glob
import shutil
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ipath = r'e:\py_data\thermo'
bpath = r'e:\py_data\ibutton'
spath = r'C:\Users\DELL\Desktop\处理数据\分析数据\thermo\10min_average'
dpath = r'C:\Users\DELL\Desktop\处理数据\按日期排序\ibutton\5月份'
l = ['30cm','60cm']
k=['A-HW2-sand','B-HW1-empty','C-HW3-empty','D-HW3-sand','E-HW1-sand','F-HW2-empty']
#复制所需thermo数据
qfile = os.listdir(spath)
for q in qfile[13:15]:
    try:
        shutil.copytree(spath+'\\'+q+'\\'+r'20170511',ipath+'\\'+q+'\\'+r'20170511')
    except:
        pass
for i in l:    
    qExist = os.path.exists(bpath+'\\'+i)
    if not qExist:
        os.mkdir(bpath+'\\'+i)
    else:
        pass
#复制所需ibutton数据    
wfile = os.listdir(dpath)
for w in wfile:
    tfile = os.listdir(dpath+'\\'+w)
    for t in tfile:
        if w[1] == '2':
            if t[-12:-4] == '20170511':
                try:
                    shutil.copyfile(dpath+'\\'+w+'\\'+t,bpath+'\\'+r'30cm'+'\\'+t)
                except:
                    pass
        if w[1] == '3':
            if t[-12:-4] == '20170511':
                try:
                    shutil.copyfile(dpath+'\\'+w+'\\'+t,bpath+'\\'+r'60cm'+'\\'+t)
                except:
                    pass
#----------------将ibutton对应数据放入thermo-----------------------#
#先分类好thermo的数据
ufile = os.listdir(ipath)
for u in ufile:
    for j in k:
        tExist = os.path.exists(ipath+'\\'+u+'\\'+r'20170511'+'\\'+j)
        if not tExist:
            os.mkdir(ipath+'\\'+u+'\\'+r'20170511'+'\\'+j)
        else:
            pass
    afile = os.listdir(ipath+'\\'+u+'\\'+r'20170511')
    for a in afile:
        if a[-3:] == 'csv':
            for j in k:
                if a[48] == j[0]:
                    try:
                        shutil.move(ipath+'\\'+u+'\\'+r'20170511'+'\\'+a,
                                    ipath+'\\'+u+'\\'+r'20170511'+'\\'+j+'\\'+a)
                    except:
                        pass
#移动ibutton数据到thermo
    sfile = os.listdir(bpath)
    for s in sfile:
        ffile = os.listdir(bpath+'\\'+s)
        for f in ffile:
            for j in k:
                if s == u[27:31]:
                    if f[0] == j[0]:
                        try:
                            shutil.move(bpath+'\\'+s+'\\'+f,ipath+'\\'+u+'\\'+r'20170511'+'\\'+j+'\\'+f)
                        except:
                            pass
#------------------------移动自动站数据到指定文件夹--------------------------------#
    nfile = os.listdir(ipath+'\\'+u+'\\'+r'20170511')
    for n in nfile:        
        mpath = r'C:\Users\DELL\Desktop\处理数据\picture\station\north station\temperature\data'
        m = r'north station-20170511-Temperature.csv'
        try:
            shutil.copyfile(mpath+'\\'+m,ipath+'\\'+u+'\\'+r'20170511'+'\\'+n+'\\'+m)
        except:
            pass
#------------------------画图--------------------------------------------------#
    gfile = os.listdir(ipath+'\\'+u+'\\'+r'20170511')
    for g in gfile:
        hfile = glob.glob(ipath+'\\'+u+'\\'+r'20170511'+'\\'+g+'\\'+'*.csv')
        if len(hfile) == 3:
            data1 = pd.read_csv(hfile[0])
            data2 = pd.read_csv(hfile[1])
            data3 = pd.read_csv(hfile[2])
            
            x = np.arange(144)
            y1 = data1.loc[:,'2'] # ibutton
            y2 = data2.loc[:,'Temperature'] # station
            y3 = data3.loc[:,'Temperature'] # thermo
            
            fig = plt.figure(figsize=(12,9))
            ax  = fig.add_subplot(1,1,1)     
            
            plt.plot(x,y1,marker='D',markersize = 0.5,linewidth = 1,label = 'The air temperature')
            plt.plot(x,y2,marker='^',markersize = 0.5,linewidth = 1,label = 'The background temperature')
            plt.plot(x,y3,marker='s',markersize = 0.5,linewidth = 1,label = 'The wall temperature')
                 
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
            
            nExist = os.path.exists(ipath+'\\'+'total picture')
            if not nExist:
                os.mkdir(ipath+'\\'+'total picture')
            else:
                pass
            plt.savefig(ipath+'\\'+'total picture'+'\\'+u+'-'+g+'.png')
            plt.savefig(ipath+'\\'+u+'\\'+r'20170511'+'\\'+g+'\\'+u+'-'+g+'.png')
            plt.close()
kpath = r'C:\Users\DELL\Desktop\处理数据\picture\thermo\壁面-空气-背景场温度对比'
gExist = os.path.exists(kpath)
if not gExist:
    os.mkdir(kpath)
else:
    pass

lfile = os.listdir(ipath)
for mm in lfile:
    shutil.move(ipath+'\\'+mm,kpath+'\\'+mm)

vfile = os.listdir(bpath)
for c in vfile:
    os.rmdir(bpath+'\\'+c)




    