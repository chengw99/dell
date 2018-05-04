# -*- coding: utf-8 -*-
"""
Created on Fri May  4 14:26:16 2018

@author: DELL
"""

# 此程序用于壁面温度三天日循环+气象站背景温度三天日循环 -- 画图
import os
import glob
import shutil
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fpath = r'C:\Users\DELL\Desktop\处理数据\picture\thermo\日循环（时间范围0-72小时）方便origin画图'
tpath = r'C:\Users\DELL\Desktop\处理数据\picture\station\日循环-5月份\total'
ipath = r'e:\py_data\thermo'
l = ['north station','south station']
#------------------------------获取数据-----------------------------------------#
qfile = os.listdir(fpath)
for q in qfile:
    try:
        shutil.copytree(fpath+'\\'+q+'\\'+r'gather data',
                        ipath+'\\'+q+'\\'+r'thermo-gather data')
    except:
        pass
#---------------------将自动站数据放入对应的文件夹----------------------------------#
    qExist = os.path.exists(ipath+'\\'+q+'\\'+r'station-gather data')
    if not qExist:
        os.mkdir(ipath+'\\'+q+'\\'+r'station-gather data')
    else:
        pass
for i in l:
    tfile = os.listdir(tpath+'\\'+i+'\\'+r'data')
    ufile = os.listdir(ipath)
    for t in tfile:
        for u in ufile:
            if t[-21:-4] == u:
                try:
                    shutil.copyfile(tpath+'\\'+i+'\\'+r'data'+'\\'+t,
                                    ipath+'\\'+u+'\\'+r'station-gather data'+'\\'+t)
                except:
                    pass
#---------------------------批量画图--------------------------------------------#
sfile = os.listdir(ipath)
for s in sfile:
    c = glob.glob(ipath+'\\'+s+'\\'+r'station-gather data'+'\\'+'*.csv')
    v = glob.glob(ipath+'\\'+s+'\\'+r'thermo-gather data'+'\\'+'*.csv')
    
    north = pd.read_csv(c[0]) # north-station
    south = pd.read_csv(c[1]) # south-station
    
    for n in v:
        data = pd.read_csv(n)
        
        x = np.arange(432)
        y1 = north.loc[:,'Temperature']
        y2 = south.loc[:,'Temperature']
        y3 = data.loc[:,'Temperature']
        
        fig = plt.figure(figsize=(10,8))
        ax = fig.add_subplot(1,1,1)
            
        plt.plot(x,y1,'D-',markersize = 3,markerfacecolor='none',markevery=6,linewidth = 1,label = c[0][-35:-4])
        plt.plot(x,y2,'s-',markersize = 3,markerfacecolor='none',markevery=6,linewidth = 1,label = c[1][-35:-4])
        if n[-9:-4] == '110cm':
            plt.plot(x,y3,'v-',markersize = 3,markerfacecolor='none',markevery=6,linewidth = 1,label = r'thermo-'+n[-11:-4]+'-'+s)
        else:
            plt.plot(x,y3,'v-',markersize = 3,markerfacecolor='none',markevery=6,linewidth = 1,label = r'thermo-'+n[-10:-4]+'-'+s)
            
        plt.xlim(0,432)
        plt.ylim(22,46)
        plt.xlabel('time',fontsize = 12)
        plt.ylabel('T(℃)',rotation = 90,fontsize = 12)
        plt.minorticks_on()
        xticks = ax.set_xticks([0,48,96,144,
                                192,240,288,
                                336,384,431])
        xlabels = ax.set_xticklabels(['0:00','8:00','16:00',
                                      '0:00','8:00','16:00',
                                      '0:00','8:00','16:00','24:00'])
        yticks = ax.set_yticks([22,26,30,34,38,42,46])
        ylabels = ax.set_yticklabels(['22','26','30','34','38','42','46'])
        plt.legend(loc='best',fontsize=12)
        plt.grid(True,linestyle='--')
        
        if n[-9:-4] == '110cm':
            plt.savefig(ipath+'\\'+s+'\\'+n[-11:-4]+'-'+s+'.png')
        else:
            plt.savefig(ipath+'\\'+s+'\\'+n[-10:-4]+'-'+s+'.png')
        
        plt.close()    
#------------------------------移动最终文件夹到指定目录---------------------------#
mExist = os.path.exists(r'C:\Users\DELL\Desktop\处理数据\picture\thermo\日循环-壁面+自动站-5月份')
if not mExist:
    os.mkdir(r'C:\Users\DELL\Desktop\处理数据\picture\thermo\日循环-壁面+自动站-5月份')
else:
    pass

jfile = os.listdir(ipath)
for j in jfile:
    shutil.move(ipath+'\\'+j,r'C:\Users\DELL\Desktop\处理数据\picture\thermo\日循环-壁面+自动站-5月份'+'\\'+j)
                        
    
        