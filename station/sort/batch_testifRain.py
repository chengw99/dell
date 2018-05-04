# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 16:55:45 2018

@author: DELL
"""
#此程序用于分析有无下雨的日期
#用于批量画图--降水量
#还是有个问题，删除文件的时候会显示程序正在占用。。
import os
import shutil
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

l = ['north station','south station']
ipath = r'e:\py_data\station'
opath = r'e:\py_output'
spath = r'C:\Users\DELL\Desktop\处理数据\picture\station'
for name in l:
    #--------------------------------创建文件夹---------------------------------#
    k = ['data','picture']
    for i in k:
        wExist = os.path.exists(ipath+'\\'+name+'\\'+r'total data')
        if not wExist:
            os.makedirs(ipath+'\\'+name+'\\'+r'total data')
        else:
            pass
        qExist = os.path.exists(ipath+'\\'+name+'\\'+'rain'+'\\'+i)
        if not qExist:
            os.makedirs(ipath+'\\'+name+'\\'+'rain'+'\\'+i)
        else:
            pass
        #复制数据到工作目录
        qfile = os.listdir(spath+'\\'+name+'\\'+r'total data')
        for q in qfile:
            try:
                shutil.copyfile(spath+'\\'+name+'\\'+r'total data'+'\\'+q,
                                ipath+'\\'+name+'\\'+r'total data'+'\\'+q)
            except:
                pass
    mk  = []        
    wfile = os.listdir(ipath+'\\'+name+'\\'+r'total data')
    for w in wfile:
        os.chdir(ipath+'\\'+name+'\\'+r'total data')
        data = pd.read_csv(w)
        
        y = data.loc[:,'RAINF']
        x = np.arange(144)
        
        if len(y) == 144:
            #------------------------------画图--------------------------------#
            fig = plt.figure()
            ax  = fig.add_subplot(1,1,1)  
            plt.bar(x,y,label = 'Precipatation'+'-'+name+'-'+w[-12:-4])

            plt.xlim(0,143)
            plt.ylim(0,10)
            plt.xlabel('time',fontsize = 12)
            plt.ylabel('Precipitation(mm)',rotation = 90,fontsize = 12)
            plt.minorticks_on()
            xticks = ax.set_xticks([0,24,48,72,96,120,143])  #此命令行可以确定x轴标签的位置
            xlabels = ax.set_xticklabels(['0:00','4:00','8:00','12:00','16:00','20:00','24:00'])  #此命令行可以命名x坐标轴的标签内容
            yticks = ax.set_yticks([0,2,4,6,8,10])
            ylabels = ax.set_yticklabels(['0','2','4','6','8','10'])
            #设置图注
            plt.legend(loc='best',fontsize = 14)
            plt.grid(True,linestyle='--')
            
            plt.savefig(ipath+'\\'+name+'\\'+r'rain\picture'+'\\'+name+'-'+w[-12:-4]+'-'+'Precipitation.png')
            plt.close()
            #---------------------------生成数据文件----------------------------#
            time = []
            for a in range(24):
                for b in np.linspace(0,60,num=6,endpoint=False):
                    if b == 0:
                        time.append(str(int(a))+':0'+str(int(b)))
                    else:
                        time.append(str(int(a))+':'+str(int(b)))
            result = pd.DataFrame({'rain':y,'time':time})
            columns = ['time','Precipitation']
            result.to_csv(ipath+'\\'+name+'\\'+r'rain\data'+'\\'+name+'-'+w[-12:-4]+'-'+'Precipitation.csv')
            #-------------------------判断是否下雨------------------------------#
            
            for g in y:
                if g > 0:
                    rainday = name+'-'+w[-12:-4]
                    mk.append(rainday)
    pp = np.array(mk)
    mfile = np.unique(pp)
    for le in mfile:
        print('有雨的日期',le)
    with open(ipath+'\\'+name+'\\'+r'rain'+'\\'+' raining day.txt','w') as f:
        for oo in mfile:
            f.write(oo)
            f.write('\n')
    #移动文件夹到指定目录
    try:
        shutil.move(ipath+'\\'+name+'\\'+r'rain',
                   spath+'\\'+name+'\\'+r'rain')
    except:
        pass
