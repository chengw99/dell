# -*- coding: utf-8 -*-
"""
Created on Fri May  4 10:37:01 2018

@author: DELL
"""

#此程序用于 批量处理气象站连续三天的温度 -- 作为背景温度日循环画图数据
#5月份
import os
import glob
import shutil
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

l = ['north station','south station']
h = ['Initial data','gather data','picture']
k = ['data','picture']

fpath = r'C:\Users\DELL\Desktop\处理数据\按日期排序\station'
ipath = r'e:\py_data\station'

#--------------------------对数据进行分类---------------------------------------#
for i in l:
    qfile = os.listdir(fpath+'\\'+i+'\\'+r'201705')
    m = []
    for mm in range(19): # 20170510没有足够24小时的数据，以20170511为起点，三天为一个周期，至20170529，可循环29-11+1=19次
        m.append(int(mm))
    b = [] # 里面是分类好的需要数据的日期
    for j in m:
        q = []
        for g in qfile[j+1:j+4]: # j+1代表当j=0时，以20170511为起点，j+1:j+4代表三天为一个周期
            q.append(g)
        b.append(q)
    #-----------------------------创建文件夹------------------------------------#
    for v in k:
        uExist = os.path.exists(ipath+'\\'+r'total'+'\\'+i+'\\'+v)
        if not uExist:
            os.makedirs(ipath+'\\'+r'total'+'\\'+i+'\\'+v)
        else:
            pass
    for file in b:
        #创建时间范围的文件夹
        qExist = os.path.exists(ipath+'\\'+i+'\\'+file[0][:-4]+'-'+file[2][:-4])
        if not qExist:
            os.makedirs(ipath+'\\'+i+'\\'+file[0][:-4]+'-'+file[2][:-4])
        else:
            pass
        #分三类文件夹：初始数据，整合数据，图片
        for f in h:
            tExist = os.path.exists(ipath+'\\'+i+'\\'+file[0][:-4]+'-'+file[2][:-4]+'\\'+f)
            if not tExist:
                os.mkdir(ipath+'\\'+i+'\\'+file[0][:-4]+'-'+file[2][:-4]+'\\'+f)
            else:
                pass
        #---------------------------将数据文件放入对应文件夹--------------------------#
        qname = os.listdir(ipath+'\\'+i) # 获取文件夹名
        for q in qname:
            for d in file: # 获取连续三个的数据文件名
                if q[0:8] == file[0][:-4]: # 判断筛选：文件夹名里起始日期 = 连续三个数据文件名里的第一个
                    try:
                        shutil.copyfile(fpath+'\\'+i+'\\'+r'201705'+'\\'+d, # 若上面的等式成立，则将这三个文件都复制到指定文件夹
                                        ipath+'\\'+i+'\\'+q+'\\'+r'Initial data'+'\\'+d)
                    except:
                        pass
#----------------------------批量画图-------------------------------------------#
    total = os.listdir(ipath+'\\'+i)
    for t in total:
        c = glob.glob(ipath+'\\'+i+'\\'+t+'\\'+h[0]+'\\'+'*.csv')
        
        data1 = pd.read_csv(c[0])
        data2 = pd.read_csv(c[1])
        data3 = pd.read_csv(c[2])
        
        y1 = data1.loc[:,'T_AIR']
        y2 = data2.loc[:,'T_AIR']
        y3 = data3.loc[:,'T_AIR'] 
        
        y = pd.concat([y1,y2,y3])
        x = np.arange(432)
            
        fig = plt.figure(figsize=(10,8))
        ax = fig.add_subplot(1,1,1)
            
        plt.plot(x,y,'rD-',markersize = 0.5,linewidth = 1,label = 'Diurnal Cycle Temperature-'+i+'-'+t)
            
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
        
        plt.savefig(ipath+'\\'+i+'\\'+t+'\\'+h[2]+'\\'+t+'.png')
        plt.savefig(ipath+'\\'+r'total'+'\\'+i+'\\'+r'picture'+'\\'+i+'-'+t+'.png')
        plt.close()

        time = []
        for a in range(72):
            for b in np.linspace(0,60,num = 6,endpoint = False):
                if b == 0:
                    time.append(str(int(a))+':0'+str(int(b)))
                else:
                    time.append(str(int(a))+':'+str(int(b)))
        
        result = pd.DataFrame({'Temperature':y,'time':time})
        columns = ['time','Temperature']
        result.to_csv(ipath+'\\'+i+'\\'+t+'\\'+h[1]+'\\'+t+'.csv',columns=columns)
        result.to_csv(ipath+'\\'+r'total'+'\\'+i+'\\'+r'data'+'\\'+i+'-'+t+'.csv',columns=columns)
#------------------------------移动最终文件夹到指定目录---------------------------#
mExist = os.path.exists(r'C:\Users\DELL\Desktop\处理数据\picture\station\日循环-5月份')
if not mExist:
    os.mkdir(r'C:\Users\DELL\Desktop\处理数据\picture\station\日循环-5月份')
else:
    pass

jfile = os.listdir(ipath)
for j in jfile:
    shutil.move(ipath+'\\'+j,r'C:\Users\DELL\Desktop\处理数据\picture\station\日循环-5月份'+'\\'+j)
                        