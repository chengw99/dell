# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 15:53:00 2018

@author: DELL
"""

import os
import shutil
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

spath = r'C:\Users\DELL\Desktop\处理数据\分析数据\thermo\10min_average'
ipath = r'e:\py_data\thermo'
kpath = r'C:\Users\DELL\Desktop\处理数据\按日期排序\station\north station\201705'
tpath = r'e:\py_data\station'
opath = r'C:\Users\DELL\Desktop\处理数据\picture\thermo'

qfile = os.listdir(spath)
for q in qfile[12:16]:
    try:
        shutil.copytree(spath+'\\'+q,ipath+'\\'+q)
    except:
        pass
    
vfile = os.listdir(kpath)
for v in vfile:
    try:
        shutil.copyfile(kpath+'\\'+v,tpath+'\\'+v)
    except:
        pass
#直接在中文路径下读取的时候发生了一个OSerror，read_csv添加参数engine = 'python'就可以解决了
#但是还是在这里换成英文路径
wfile = os.listdir(ipath)
for w in wfile:
    tfile = os.listdir(ipath+'\\'+w)
    for t in tfile:
        ufile = os.listdir(ipath+'\\'+w+'\\'+t)
        pfile = os.listdir(tpath)
        for u in ufile: #thermo datafile
            for p in pfile: #radiation datafile
                if p[-12:-4] == t:
                    x = np.arange(144)
                    data = pd.read_csv(tpath+'\\'+p) # data : station solar radiation
                    data2 = pd.read_csv(ipath+'\\'+w+'\\'+t+'\\'+u) # data : thermo
                    
                    y = data.loc[:,'SRAD'] #solar radiation
                    y2 = data2.iloc[:,2] #thermo
                    
                    if len(y) == 144 and len(y2) == 144:
                        fig = plt.figure()
                        ax1  = fig.add_subplot(1,1,1)
                        plt.bar(x,y,label = 'The solar radiation'+'-'+p[-12:-4])
                        plt.xlim(0,143) 
                        plt.ylim(0,600)
                        plt.xlabel('time',fontsize = 12)
                        plt.ylabel('solar radiation(Watts/m2)',rotation = 90,fontsize = 12)
                        xticks = ax1.set_xticks([0,24,48,72,96,120,143])  #此命令行可以确定x轴标签的位置
                        xlabels = ax1.set_xticklabels(['0:00','4:00','8:00','12:00','16:00','20:00','24:00'])  #此命令行可以命名x坐标轴的标签内容
                        yticks = ax1.set_yticks([0,100,200,300,400,500,600])
                        ylabels = ax1.set_yticklabels(['0','100','200','300','400','500','600'])
                        plt.legend(loc='upper right',bbox_to_anchor=(1,1),fontsize = 12)
                        plt.grid(True,linestyle='--')
                        plt.minorticks_on()
                        
                        ax2 = ax1.twinx() #用于添加y轴
                        plt.plot(x,y2,color = 'darkorange',marker = 'D',markersize = 0.5,linestyle = '-',linewidth = 1.5,label = 'The temperature'+'-'+u[-12:-4])
                        
                        plt.xlim(0,143)
                        plt.ylim(22,46)
                        plt.xlabel('time',fontsize = 12)
                        plt.ylabel('Temperature(℃)',rotation = 90,fontsize = 12)
                        plt.minorticks_on()
                        xticks = ax2.set_xticks([0,24,48,72,96,120,143])  #此命令行可以确定x轴标签的位置
                        xlabels = ax2.set_xticklabels(['0:00','4:00','8:00','12:00','16:00','20:00','24:00'])  #此命令行可以命名x坐标轴的标签内容
                        yticks = ax2.set_yticks([22,26,30,34,38,42,46])
                        ylabels = ax2.set_yticklabels(['22','26','30','34','38','42','46'])
                        #设置图注
                        plt.legend(loc='upper right',bbox_to_anchor=(0.98,0.93),fontsize = 12,markerscale = 10) #这里可以修改legend中marker的大小
                        plt.grid(True,linestyle='--')
                        plt.minorticks_on()
    
                        mExist = os.path.exists(opath+'\\'+r'辐射量+壁面温度'+'\\'+qfile[12][:24]+'\\'+u[-12:-4])
                        if not mExist:
                            os.makedirs(opath+'\\'+r'辐射量+壁面温度'+'\\'+qfile[12][:24]+'\\'+u[-12:-4])
                        else:
                            pass
                        plt.savefig(opath+'\\'+r'辐射量+壁面温度'+'\\'+qfile[12][:24]+'\\'+u[-12:-4]
                                    +'\\'+'Solar-'+u[:-4]+'.png')
                        plt.close()

lfile = os.listdir(ipath)
for l in lfile:
    try:
        shutil.rmtree(ipath+'\\'+l)
    except:
        pass
kfile = os.listdir(tpath)
for k in kfile:
    try:
        os.unlink(tpath+'\\'+k)
    except:
        pass








            
