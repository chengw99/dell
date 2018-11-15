# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 22:05:41 2018

@author: DELL
"""

import os
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ipath = 'E:\py_data\station'
opath = 'E:\py_output'

nfile = glob.glob(ipath+'\\'+'north'+'\\'+'*.csv')
sfile = glob.glob(ipath+'\\'+'south'+'\\'+'*.csv')

for n in nfile:
    for s in sfile:
        if os.path.basename(n) == os.path.basename(s):
            
            data1 = pd.read_csv(n)
            data2 = pd.read_csv(s)
        
            y1 = data1.loc[:,'WSPD'][:144]
            y2 = data2.loc[:,'WSPD'][:144]
            x = np.arange(144)
            
            # 画图
            if len(y1) and len(y2) == 144:
                fig = plt.figure(figsize=(12,9))
                ax = fig.add_subplot(1,1,1)
            
                plt.plot(x,y1,linestyle='-',marker='D',markersize=7,markerfacecolor='none',markevery=6,linewidth=1,label='wind-north-'+'-'+os.path.basename(n)[:-4])
                plt.plot(x,y2,linestyle='-',marker='o',markersize=7,markerfacecolor='none',markevery=6,linewidth=1,label='wind-south-'+'-'+os.path.basename(s)[:-4])
                plt.xlim(0,143)
                plt.ylim(0,3)
                plt.xlabel('Time',fontsize=12,fontname='Times New Roman')
                plt.ylabel('Wind speed(m/s)',rotation = 90,fontsize = 12,fontname = 'Times New Roman')
                xticks = ax.set_xticks([0,24,48,72,96,120,143])
                xlabels = ax.set_xticklabels(['0:00','4:00','8:00','12:00','16:00','20:00','24:00'])
                yticks = ax.set_yticks([0,1,2,3])
                ylabels = ax.set_yticklabels(['0','1','2','3'])
                plt.legend(loc='best',fontsize=18)
                plt.savefig(opath+'\\'+'wind-compare-north&south station'+'-'+os.path.basename(n)[:-4]+'.png')    
                plt.close()

