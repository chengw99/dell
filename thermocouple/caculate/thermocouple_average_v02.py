# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 21:54:16 2017

@author: DELL
"""

import glob
import pandas as pd

def p(name,height):
    name = str(name)
    height = str(height)
    a =  name + '_Temperature' + height + 'cm' 
    return a

#列举目录下所有的csv文件
csv_filenames = glob.glob('e:\\py\\*.csv')
#所有csv文件处理得到的每小时温度平均
l_tem1=[]  #目标文件夹下所有csv的通道213数据
l_tem2=[]  #目标文件夹下所有csv的通道214数据
l_tem3=[]  #目标文件夹下所有csv的通道215数据
l_tem4=[]  #目标文件夹下所有csv的通道216数据
#所有csv文件对应得到的时间序列
l_time=[]
#遍历要处理的csv文件

for filename in csv_filenames:
    #读取csv文件并赋予列的名字
    f = pd.read_csv(filename)
    #需要手动做的一件事情是把每个热电偶的数据文件变成同一大小 ----->下一步就是把这一步实现自动，搜索关键字，界定需要的数据范围，自动提取需要的数据
    data_1 = f.ix[:,34]
    data2 = f.ix[:,35]
    data3 = f.ix[:,36]
    data4 = f.ix[:,37]
    tem1 = []
    for i in range(24):
        data_mean_1 = sum(data_1[60*i:60*i+60])/60.
        tem1.append(data_mean_1)
    l_tem1.append(tem1)
    tem2 = []
    for i in range(24):
        data_mean2 = sum(data2[60*i:60*i+60])/60.
        tem2.append(data_mean2)
    l_tem2.append(tem2)
    tem3 = []
    for i in range(24):
        data_mean3 = sum(data3[60*i:60*i+60])/60.
        tem3.append(data_mean3)
    l_tem3.append(tem3)
    tem4 = []
    for i in range(24):
        data_mean4 = sum(data4[60*i:60*i+60])/60.
        tem4.append(data_mean4)
    l_tem4.append(tem4)
    time=[]
    for i in range(24):
        t=str(i)+':00'
        time.append(t)
    l_time.append(time)
#比较直接的一种方式把得到的结果输出到csv文件中
#比之前的节省了命名列的时间
result = pd.DataFrame({'time':time,p(1,30):l_tem1[0],p(2,30):l_tem1[1],
                       p(1,60):l_tem2[0],p(2,60):l_tem2[1],
                       p(1,90):l_tem3[0],p(2,90):l_tem3[1],
                       p(1,110):l_tem4[0],p(2,110):l_tem4[1]})
result.to_csv('e:\data\9.csv')   
    
'''result = pd.DataFrame({'time':time,'A_Temperature30cm':l_tem1[0],'B_Temperature30cm':l_tem1[1],
                       'A_Temperature60cm':l_tem2[0],'B_Temperature60cm':l_tem2[1],
                       'A_Temperature90cm':l_tem3[0],'B_Temperature90cm':l_tem3[1],
                       'A_Temperature110cm':l_tem4[0],'B_Temperature110cm':l_tem4[1]})'''
#这种方法行不通，dataFrame冒号后面的内容不是字符串   
'''result = pd.DataFrame({'time':time,p(1,30):q(1,0),p(2,30):q(1,1),
                       p(1,60):q(2,0),p(2,60):q(2,1),
                       p(1,90):q(3,0),p(2,90):q(3,1),
                       p(1,110):q(4,0),p(2,110):q(4,1)})
def q(num,order):
    num = str(num)
    order = str(num)
    b = 'l_tem' + num +'[' + order + ']'
    return b'''