# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 21:17:20 2017

@author: DELL
"""
import glob
import pandas as pd
import numpy as np

#列举目录下所有的csv文件
csv_filenames = glob.glob('e:\\py\\*.csv')
#所有csv文件处理得到的每小时温度平均
l_tem=[]
#所有csv文件对应得到的时间序列
l_time=[]
#遍历要处理的csv文件
for filename in csv_filenames:
    #读取csv文件并赋予列的名字
    f = pd.read_csv(filename,names=['0','1','2'])
    #选取所要处理的数据序列
    data=f.ix[20:451,2].values.astype(np.float)
    #循环得到每小时温度平均
    tem=[]
    for j in range(24):
        data_mean=sum(data[j*6:j*6+6])/6.
        tem.append(data_mean)
    l_tem.append(tem)
    #生成时间序列
    time=[]
    for i in range(24):
        t=str(i)+':00'
        time.append(t)
    l_time.append(time)
#--------#这样其实还是缺少了列的名称，还不如直接指定，也只是加个函数
time = []
for i in range(24):
    t = str(i)+':00'
    time.append(t)
sucess=[]
for g in range(5):
    text=pd.Series(l_tem[g],index = time)  #这样可以得到不是24个数据在一个单元格
    sucess.append(text)
final=pd.DataFrame(sucess)
final.to_csv('e:\\255.csv')

p = pd.read_csv('e:\\255.csv')
pp = p.T  #意外发现，可以直接得到转置
pp.to_csv('e:\\3.csv')
#------------------#