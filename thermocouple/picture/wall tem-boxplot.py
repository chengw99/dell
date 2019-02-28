# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 14:02:38 2019

@author: DELL
"""

# 此程序用于分析街谷两侧壁面温度的箱型图
# 运行程序batch-thermo-rename.py获取各街谷数据
#------------------再运行此程序-------------------#
# pandas只读取需要的数据，而不是将整个文件都读取
# 根据读取的数据直接画图以及保存这份数据

import os
import glob
import pandas as pd
import matplotlib.pyplot as plt

ipath = r'E:\py_data\thermo'
opath = r'E:\py_output'

file = os.listdir(ipath)
for f in file:
    qfile = glob.glob(ipath+'\\'+f+'\\'+'*.csv')
    for q in qfile:
        if os.path.basename(q)[-3:] == 'csv':
            # 获取需要进行分析的通道
            #n = [i for i in range(31,39)] # 使用列表推导式获取需要的通道号
            n = list(range(31,39)) # 或者使用list函数生成列表
            data = pd.read_csv(q,usecols=n) # 参数usecols可以选定读取哪几列的数据，而不需要读取完整个文件然后再进行筛选
            
            # 画箱型图
            fig = plt.figure(figsize=(12,9),dpi=160)
            ax = fig.add_subplot(1,1,1)
            plt.style.use('ggplot') # 设置图形的显示风格为ggplot
            
            #data.boxplot() # 快速制作箱型图
            
            #--------------使用plt.boxplot定制箱型图----------------------------#
            l = [data.iloc[:,i] for i in range(8)]
            plt.boxplot(l,flierprops = dict(markerfacecolor='g', marker='D'))
            #----------------------------------------------------------------#
            
            plt.xlabel('Location',fontsize=12)
            plt.ylabel('Temperature(℃)',rotation=90,fontsize=12)
            xlabels = ax.set_xticklabels(['N-110cm','N-90cm','N-60cm','N-30cm','S-30cm','S-60cm','S-90cm','S-110cm'])
            plt.ylim(15,55)
            plt.title(os.path.basename(q)[:-4],fontsize=12)
            
            # 保存图片
            tfile = opath +'\\'+r'picture'+'\\'+f
            tExist = os.path.exists(tfile)
            if not tExist:
                os.makedirs(tfile)
                plt.savefig(tfile+'\\'+os.path.basename(q)[:-4]+'.png')
            else:
                plt.savefig(tfile+'\\'+os.path.basename(q)[:-4]+'.png')
            plt.close()
            
            
            # 保存数据
            rfile = opath +'\\'+r'data'+'\\'+f
            rExist = os.path.exists(rfile)
            if not rExist:
                os.makedirs(rfile)
                data.to_csv(rfile+'\\'+'wall tem-'+os.path.basename(q))
            else:
                data.to_csv(rfile+'\\'+'wall tem-'+os.path.basename(q))
                
                
