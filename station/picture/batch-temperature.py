# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 09:42:31 2018

@author: DELL
"""

import os
import shutil
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


l = ['north station','south station']
for name in l:
    #--------------------------------创建文件夹---------------------------------#
    qExist = os.path.exists(r'e:\py_data\station'+'\\'+name)
    if not qExist:
        os.mkdir(r'e:\py_data\station'+'\\'+name)
    else:
        pass
    
    wExist = os.path.exists(r'e:\py_data\station'+'\\'+name+'\\'+r'total data')
    if not wExist:
        os.mkdir(r'e:\py_data\station'+'\\'+name+'\\'+r'total data')
    else:
        pass
    k = ['data','picture']
    for i in k:
        tExist = os.path.exists(r'e:\py_data\station'+'\\'+name+'\\'+r'temperature'+'\\'+i)
        if not tExist:
            os.makedirs(r'e:\py_data\station'+'\\'+name+'\\'+r'temperature'+'\\'+i) #创建多级目录 
        else:
            pass
    #---------------------------------获取数据----------------------------------#
    file = os.listdir(r'C:\Users\DELL\Desktop\处理数据\按日期排序\station\\'+name+'\\'+r'201705')
    for f in file:
        shutil.copyfile(r'C:\Users\DELL\Desktop\处理数据\按日期排序\station\\'+name+'\\'+r'201705'+'\\'+f,
                        r'E:\py_data\station\\'+name+'\\'+r'total data'+'\\'+f)

    #---------------------------------画图-------------------------------------#
    qfile = os.listdir(r'e:\py_data\station\\'+name+'\\'+r'total data')
    for q in qfile:
        os.chdir(r'e:\py_data\station\\'+name+'\\'+r'total data')
        data = pd.read_csv(q)
    
        y = data.loc[:,'T_AIR'] #选取温度数据
        x = np.arange(144)
        
        if len(y) == 144:
            fig = plt.figure()
            ax  = fig.add_subplot(1,1,1)
            
            plt.plot(x,y,'rx-',markersize = 1,linewidth = 1.5,label = 'The Background Temperature'+'-'+name+'-'+q[-12:-4])
        
            plt.xlim(0,144)
            plt.ylim(20,40)
            plt.xlabel('time',fontsize = 12)
            plt.ylabel('T(℃)',rotation = 90,fontsize = 12)
            plt.minorticks_on()
            xticks = ax.set_xticks([0,24,48,72,96,120,143])  #此命令行可以确定x轴标签的位置
            xlabels = ax.set_xticklabels(['0:00','4:00','8:00','12:00','16:00','20:00','24:00'])  #此命令行可以命名x坐标轴的标签内容
            yticks = ax.set_yticks([20,24,28,32,36,40])
            ylabels = ax.set_yticklabels(['20','24','28','32','36','40'])
            #设置图注
            plt.legend(loc='best',fontsize = 14)
            plt.grid(True,linestyle='--')
        
        
            plt.savefig(r'e:\py_data\station\\'+name+'\\'+r'temperature\picture\\'+name+'-'+q[-12:-4]+'-'+'Temperature.png')
            plt.close()
            
            #生成数据文件
            time = []
            for i in range(24):
                for j in np.linspace(0,60,num = 6,endpoint = False):
                    if j == 0:
                        time.append(str(int(i))+':0'+str(int(j)))
                    else:
                        time.append(str(int(i))+':'+str(int(j)))
        
            result = pd.DataFrame({'Temperature':y,'time':time})
            columns = ['time','Temperature']
            result.to_csv(r'e:\py_data\station\\'+name+'\\'+r'temperature\data\\'+name+'-'+q[-12:-4]+'-'+'Temperature.csv')
        
        else:
            pass

