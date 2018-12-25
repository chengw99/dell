# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 20:53:55 2018

@author: DELL
"""
# 此程序用于求解各街谷壁面平均温度的日循环特征-平均温度，DTR，最高温出现时间 温度数据的时间分辨率是1min
#-------------------------------准备数据---------------------------------------#
# 先运行程序 batch-thermo-rename.py 将文件夹改名--可以清楚知道是哪个街谷的数据，同时将数据复制到 py_data
# 运行程序 average-Temperature-canyon-1min.py 获取壁面测点的温度，将数据文件分类放好
# 运行程序 average-Temperature-canyon-10min_v02.py 将同一街谷不同高度不同朝向的热电偶温度进行平均，获取各街谷平均温度

import os
import glob
import pandas as pd

#----------------------------------处理数据-------------------------------------#

ipath = r'E:\py_output\T_average_whole canyon'
opath = r'E:\py_output'


c_file = os.listdir(ipath)
for c in c_file:
    # 平均温度
    m1=[]
    # DTR
    m2=[]
    # 最大值对应的时间
    m3=[]
    n=[] #街谷类型
    file = glob.glob(ipath+'\\'+c+'\\'+'*.csv')
    for f in file:
        data = pd.read_csv(f)
        tem = data.iloc[:,2]
        
        tem_mean = tem.mean() #平均值
        tem_DTR = tem.max() - tem.min() # 最大值-最小值
        time_max = data.iloc[:,1][tem.argmax()] # 最大值对应的时间
        
        m1.append(tem_mean)
        m2.append(tem_DTR)
        m3.append(time_max)
        n.append(os.path.basename(f)[2:11])
        
    result1 = pd.DataFrame({'tem_mean':m1,'street':n})
    result2 = pd.DataFrame({'tem_DTR':m2,'street':n})
    result3 = pd.DataFrame({'time_max':m3,'street':n})
    columns1 = ['street','tem_mean']
    columns2 = ['street','tem_DTR']
    columns3 = ['street','time_max']
        #result = pd.DataFrame({'tem_mean':[tem_mean],'tem_DTR':[tem_DTR],'time_max':[time_max]})
        #columns = ['tem_mean','tem_DTR','time_max']
        
    r_file = opath+'\\'+'origin-Daily cycle temperature characteristic'+'\\'+c
    qExist = os.path.exists(r_file)
    if not qExist:
        os.makedirs(r_file)
        result1.to_csv(r_file+'\\'+'tem_mean-'+os.path.basename(f)[-12:],columns=columns1)
        result2.to_csv(r_file+'\\'+'tem_DTR-'+os.path.basename(f)[-12:],columns=columns2)
        result3.to_csv(r_file+'\\'+'time_max-'+os.path.basename(f)[-12:],columns=columns3)

    else:
        result1.to_csv(r_file+'\\'+'tem_mean-'+os.path.basename(f)[-12:],columns=columns1)
        result2.to_csv(r_file+'\\'+'tem_DTR-'+os.path.basename(f)[-12:],columns=columns2)
        result3.to_csv(r_file+'\\'+'time_max-'+os.path.basename(f)[-12:],columns=columns3)


        
        






