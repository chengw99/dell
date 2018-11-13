# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 09:11:24 2018

@author: DELL
"""


# 此程序用于批量画图
# 适用所有类型的高宽比侧壁
# 数据存放对应的是拼接数据程序的存放方式

import os
import glob
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#date = ['20170624','20170625','20170626','20170627']
date = ['201706'+str(i) for i in range(26,27)]

for d in date: 
    ipath = r'e:\py_output'+'\\'+d+'\\'+'data'
    opath = r'e:\py_output'

    fname = os.listdir(ipath)
    for f in fname:
        #csvfile = glob.glob(ipath+'\\'+f+'\\'+'*.csv')
        csvfile = glob.glob(os.path.join(ipath+'\\'+f,'*.csv'))
        for q in csvfile:    
            data = pd.read_csv(q,names=np.arange(480)) # 480是根据数据的维度得出的
            a = np.array(data)
            
            dy = 1500 / (data.shape[0] -1) 
            dx = dy

            x = np.arange(0,dx*(data.shape[1]),dx)
            y = np.linspace(0,1500,data.shape[0])
            X,Y = np.meshgrid(x,y)
            
            fig = plt.figure(figsize=(10,8))
            ax = fig.add_subplot(1,1,1)
            
            plt.pcolormesh(X,Y,a,cmap='jet',vmin=20,vmax=44)
            plt.gca().set_aspect('equal')
            #plt.ylabel('height (mm)',fontsize=16,fontname='Times New Roman')
            plt.xticks([])
            ytciks = ax.set_yticks(np.arange(0,1800,300))
            ylabels = ax.set_yticklabels([str(i) for i in np.arange(0,1800,300)])
            plt.yticks([])
            #plt.title(os.path.basename(q),fontsize=12)
            #plt.colorbar(ticks=[20,24,28,32,36,40,44])
        
            qExist = os.path.exists(opath+'\\'+d+'\\'+'picture'+'\\'+f)
            if not qExist:
                os.makedirs(opath+'\\'+d+'\\'+'picture'+'\\'+f)
                plt.savefig(opath+'\\'+d+'\\'+'picture'+'\\'+f+'\\'+os.path.basename(q)[:-4]+'.png')
            else:
                plt.savefig(opath+'\\'+d+'\\'+'picture'+'\\'+f+'\\'+os.path.basename(q)[:-4]+'.png')
        
            tExist = os.path.exists(opath+'\\'+'gather-picture'+'\\'+d)
            if not tExist:
                os.makedirs(opath+'\\'+'gather-picture'+'\\'+d)
                plt.savefig(opath+'\\'+'gather-picture'+'\\'+d+'\\'+os.path.basename(q)[:-4]+'.png')
            else:
                plt.savefig(opath+'\\'+'gather-picture'+'\\'+d+'\\'+os.path.basename(q)[:-4]+'.png')
             
            plt.close()
