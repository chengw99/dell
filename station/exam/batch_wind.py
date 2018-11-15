# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 20:57:48 2018

@author: DELL
"""

# 此程序用于批量生成自动站风速数据
# 易于以同样的处理方法处理其它物理量，但这程序缺乏输入数据，仍需要手动输入数据，还比较粗糙，也可后面再添加输入数据的功能，易实现

import os
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ipath = r'e:\py_data\station'
opath = r'e:\py_output'
u = ['north','south']

for i in u:
    file = glob.glob(ipath+'\\'+i+'\\'+'*.csv')
    for f in file:
        data = pd.read_csv(f)
        
        y = data.loc[:,'WSPD'][:144]
        x = np.arange(144)
        
        # 数据文件
        time = data.loc[:,'TIME'][:144]
        columns = ['Time','Wind']
        result = pd.DataFrame({'Wind':y,'Time':time})
        
        # 画图
        if len(y) == 144:
            fig = plt.figure(figsize=(12,9))
            ax = fig.add_subplot(1,1,1)
            
            plt.plot(x,y,linestyle='-',marker='D',markersize=7,markerfacecolor='none',markevery=6,linewidth=1,label='wind-'+i+'-'+os.path.basename(f)[:-4])
            plt.xlim(0,143)
            plt.ylim(0,3)
            plt.xlabel('Time',fontsize=12,fontname='Times New Roman')
            plt.ylabel('Wind speed(m/s)',rotation = 90,fontsize = 12,fontname = 'Times New Roman')
            xticks = ax.set_xticks([0,24,48,72,96,120,143])
            xlabels = ax.set_xticklabels(['0:00','4:00','8:00','12:00','16:00','20:00','24:00'])
            yticks = ax.set_yticks([0,1,2,3])
            ylabels = ax.set_yticklabels(['0','1','2','3'])
            plt.legend(loc='best',fontsize=18)
            
            qExist = os.path.exists(opath+'\\'+'picture'+'\\'+i)
            if not qExist:
                os.makedirs(opath+'\\'+'picture'+'\\'+i)
                plt.savefig(opath+'\\'+'picture'+'\\'+i+'\\'+'wind-'+i+'-'+os.path.basename(f)[:-4]+'.png')
            else:
                plt.savefig(opath+'\\'+'picture'+'\\'+i+'\\'+'wind-'+i+'-'+os.path.basename(f)[:-4]+'.png')
            plt.close()
            
            wExist = os.path.exists(opath+'\\'+'data'+'\\'+i)
            if not wExist:
                os.makedirs(opath+'\\'+'data'+'\\'+i)
                result.to_csv(opath+'\\'+'data'+'\\'+i+'\\'+'wind-'+i+'-'+os.path.basename(f)[:-4]+'.csv',columns=columns)
            else:
                result.to_csv(opath+'\\'+'data'+'\\'+i+'\\'+'wind-'+i+'-'+os.path.basename(f)[:-4]+'.csv',columns=columns)
                