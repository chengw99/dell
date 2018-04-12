# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 20:45:47 2018

@author: DELL
"""

import os
import shutil
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ipath = r'e:\py_data\thermo'
spath = r'C:\Users\DELL\Desktop\处理数据\picture\thermo\对比不同高度\south model-facing north\20170511'
bpath = r'C:\Users\DELL\Desktop\处理数据\picture\thermo\屋顶温度\data'
l = ['A','B','C','D','E','F']
qfile = os.listdir(spath)
for q in qfile:
    try:
        shutil.copytree(spath+'\\'+q,ipath+'\\'+q)
    except:
        pass
wfile = os.listdir(bpath)
for w in wfile[4:8]:
    tfile = os.listdir(bpath+'\\'+w+'\\'+r'20170511')
    for t in tfile:
        if t[-3:] == 'csv':
            if w[17:21] == 'west' or 'east':
                for i in l:
                    if t[38] == i:
                        try:
                            shutil.copyfile(bpath+'\\'+w+'\\'+r'20170511'+'\\'+t,
                                            ipath+'\\'+i+'\\'+t)
                        except:
                            pass
            if w[17:22] == 'north' or 'south':
                for j in l:
                    if t[39] == j:
                        try:
                            shutil.copyfile(bpath+'\\'+w+'\\'+r'20170511'+'\\'+t,
                                            ipath+'\\'+j+'\\'+t)
                        except:
                            pass
            else:
                pass
ufile = os.listdir(ipath)
for u in ufile:
    ofile = os.listdir(ipath+'\\'+u)
    for o in ofile:
        if o[-3:] == 'png':
            try:
                os.unlink(ipath+'\\'+u+'\\'+o)
            except:
                pass
#---画图------#
pfile = os.listdir(ipath)
for p in pfile:
    afile = glob.glob(ipath+'\\'+p+'\\'+'*.csv')
    if len(afile) == 8:
        data1 = pd.read_csv(afile[1]) # 30cm
        data2 = pd.read_csv(afile[2]) # 60cm
        data3 = pd.read_csv(afile[3]) # 90cm
        data4 = pd.read_csv(afile[0]) # 110cm
        data5 = pd.read_csv(afile[4]) # east
        data6 = pd.read_csv(afile[5]) # north
        data7 = pd.read_csv(afile[6]) # south
        data8 = pd.read_csv(afile[7]) # west
        
        x = np.arange(144)
        y1 = data1.loc[:,'Temperature']
        y2 = data2.loc[:,'Temperature']
        y3 = data3.loc[:,'Temperature']
        y4 = data4.loc[:,'Temperature']
        y5 = data5.loc[:,'Temperature']
        y6 = data6.loc[:,'Temperature']
        y7 = data7.loc[:,'Temperature']
        y8 = data8.loc[:,'Temperature']
        
        fig = plt.figure(figsize=(12,9),dpi=160)
        ax  = fig.add_subplot(1,1,1)     

        plt.plot(x,y1,marker='D',markersize = 0.5,linewidth = 1,label = 'wall temperature-h=30cm')
        plt.plot(x,y2,marker='^',markersize = 0.5,linewidth = 1,label = 'wall temperature-h=60cm')
        plt.plot(x,y3,marker='s',markersize = 0.5,linewidth = 1,label = 'wall temperature-h=90cm')
        plt.plot(x,y4,marker='v',markersize = 0.5,linewidth = 1,label = 'wall temperature-h=110cm')
        plt.plot(x,y5,marker='D',markersize = 0.5,linewidth = 1,label = 'roof temperature-east')
        plt.plot(x,y6,marker='^',markersize = 0.5,linewidth = 1,label = 'roof temperature-north')
        plt.plot(x,y7,marker='s',markersize = 0.5,linewidth = 1,label = 'roof temperature-south')
        plt.plot(x,y8,marker='v',markersize = 0.5,linewidth = 1,label = 'roof temperature-west')
                             
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
        
        tExist = os.path.exists(ipath+'\\'+r'total picture')
        if not tExist:
            os.mkdir(ipath+'\\'+r'total picture')
        else:
            pass
        
        plt.savefig(ipath+'\\'+r'total picture'+'\\'+'wall-roof'+'-'+p+'.png')
        plt.savefig(ipath+'\\'+p+'\\'+'wall-roof'+'-'+p+'.png')
        plt.close()
kpath = r'C:\Users\DELL\Desktop\处理数据\picture\thermo\屋顶-壁面不同高度-温度对比'
gExist = os.path.exists(kpath)
if not gExist:
    os.mkdir(kpath)
else:
    pass

gfile = os.listdir(ipath)
for g in gfile:
    shutil.move(ipath+'\\'+g,kpath+'\\'+g)
