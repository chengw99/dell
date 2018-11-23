# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 09:38:09 2018

@author: DELL
"""
# 先运行程序 batch-thermo-rename.py 将文件夹改名--可以清楚知道是哪个街谷的数据，同时将数据复制到 py_data
# 实现目标：此程序用于批量处理 将同一街谷不同朝向不同高度热电偶壁面温度数据进行平均 -- 进而对比不同高宽比和不同建筑热容的影响 -- 比单个固定点温度对比更具说服力
#--------------------------------------v01---------------------------------------#
# 获取各街谷热电偶数据，取10min平均，文件夹分类（不同街谷-不同日期-同一街谷不同高度测点的温度数据.csv）

import os
import glob
import numpy as np
import pandas as pd

ipath = r'E:\py_data\thermo'
opath = r'E:\py_output'

f_file = os.listdir(ipath)
for f in f_file:
    c_file = glob.glob(ipath+'\\'+f+'\\'+'*.csv')
    
    for c in c_file:
        if os.path.basename(c)[-3:] == 'csv':
            #------------------------选择进行分析的通道-------------------------------#
            num = np.arange(35,39) # 通道数对应测点位置
            dict =  {'35':'facing north-30cm','36':'facing north-60cm','37':'facing north-90cm','38':'facing north-110cm'}
            
            for n in num:
                if n != 32:
                
                    try:
                        
                        a = pd.read_csv(c)
                        data = a.ix[:,n]
                        
                        tem = []
                        for k in range(144):
                            data_mean = np.sum(data[10*k:10*k+10].values)/10.
                            tem.append(data_mean)
                        
                        time = []
                        for i in range(24):
                            for j in np.linspace(0,60,num=6,endpoint = False):
                                if j == 0:
                                    time.append(str(int(i))+':0'+str(int(j)))
                                else:
                                    time.append(str(int(i))+':'+str(int(j)))
                        
                        result = pd.DataFrame({'time':time,'Temperature':tem})
                        columns = ['time','Temperature']
                        
                        r_file = opath+'\\'+f+'\\'+os.path.basename(c)[-12:-4]
                        qExist = os.path.exists(r_file)
                        if not qExist:
                            os.makedirs(r_file)
                            result.to_csv(r_file+'\\'+'Tem-10min-'+dict[str(n)]+'.csv',columns = columns)
                        else:
                            result.to_csv(r_file+'\\'+'Tem-10min-'+dict[str(n)]+'.csv',columns = columns)
                    except:
                        print('Error read')   
                else: # 32对应通道数据有问题，故加判断，除掉这个测点
                    pass 
                        