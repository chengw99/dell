# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 19:54:01 2018

@author: DELL
"""
# 先运行程序 batch-thermo-rename.py 将文件夹改名--可以清楚知道是哪个街谷的数据，同时将数据复制到 py_data
# 实现目标：此程序用于批量处理 将同一街谷不同朝向不同高度热电偶温度数据进行平均 -- 进而对比不同高宽比和不同建筑热容的影响 -- 比单个固定点温度对比更具说服力
#--------------------------------------v01---------------------------------------#
# 获取各街谷热电偶数据，取10min平均，文件夹分类（不同街谷-不同日期-同一街谷不同高度测点的温度数据.csv）
#--------------------------------------v02---------------------------------------#
# 需要先运行avverage-Temperature-canyon-10min_v01.py，生成平均数据到文件夹py_output
# 实现算法：批量处理，将同一街谷不同高度不同朝向的热电偶温度进行平均，获取各街谷平均温度

import os 
import glob
import pandas as pd

ipath = r'E:\py_output'
c_file = os.listdir(ipath)

for c in c_file:
    u_file = os.listdir(ipath+'\\'+c)
    
    for u in u_file:

        f_file = glob.glob(ipath+'\\'+c+'\\'+u+'\\'+'*.csv')
        
        if len(f_file) == 8:
            
            l = []
            for i in range(8):
                a = pd.read_csv(f_file[i])
                l.append(a)
            
            tem_mean = (l[0].iloc[:,2] + l[1].iloc[:,2] + l[2].iloc[:,2] + l[3].iloc[:,2] +\
                        l[4].iloc[:,2] + l[5].iloc[:,2] + l[6].iloc[:,2] + l[7].iloc[:,2])/len(f_file)
            
            time = l[0].iloc[:,1]
            
            result = pd.DataFrame({'time':time,'Temperature':tem_mean})
            columns = ['time','Temperature']
            
            q_file = ipath+'\\'+r'T_average_whole canyon'+'\\'+c
            qExist = os.path.exists(q_file)
            if not qExist:
                os.makedirs(q_file)
                result.to_csv(q_file+'\\'+u+'.csv',columns=columns)
            else:
                result.to_csv(q_file+'\\'+u+'.csv',columns=columns)
        else:
            print('Error in:',c+'-'+u)