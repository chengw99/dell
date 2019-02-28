# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 21:08:14 2019

@author: DELL
"""

#--------------------------------v1-------------------------------------------#
# 此程序用于分析街谷两侧壁面温度24小时的箱型图
# 运行程序batch-thermo-rename.py获取各街谷数据
#再运行此程序#
# pandas只读取需要的数据，而不是将整个文件都读取
# 根据读取的数据直接画图以及保存这份数据
#--------------------------------v2-------------------------------------------#
# 筛选两侧壁面的温度时间，做了区分，白天和晚上
# 还是画箱型图及保存数据
#--------------------------------v3-------------------------------------------#
# 白天和晚上含重复代码，改为函数封装
# 画箱型图函数和保存数据函数

import os
import glob
import pandas as pd
import matplotlib.pyplot as plt

#----------画箱型图------------#
def plot_box(number,dfile,s):
    # number；激活图片的代号   dfile:需要画图的变量  s：图片保存的文件夹
    # 白天和晚上箱型图设置基本一样，将共同部分用函数表达，但尽量减少参数，用函数可以精简代码
    plt.figure(number,figsize=(12,9),dpi=160)
    plt.style.use('ggplot')
    plt.boxplot(dfile,flierprops = dict(markerfacecolor='g', marker='D'))
    plt.xlabel('Location',fontsize=12)
    plt.ylabel('Temperature(℃)',rotation=90,fontsize=12)
    plt.xticks(list(range(1,9)),
               ('N-110cm','N-90cm','N-60cm','N-30cm','S-30cm','S-60cm','S-90cm','S-110cm')) # 也可以这样定义x轴刻度标签
    plt.ylim(15,55)
    plt.title(os.path.basename(q)[:-4],fontsize=12)
    
    #保存图片
    tfile = opath+'\\'+s+'\\'+f
    tExist = os.path.exists(tfile)
    if not tExist:
        os.makedirs(tfile)
        plt.savefig(tfile+'\\'+os.path.basename(q)[:-4]+'.png')
    else:
        plt.savefig(tfile+'\\'+os.path.basename(q)[:-4]+'.png')
    plt.close()    
#----------保存数据-----------#
def save_data(routh,result):
    # routh 文件保存文件夹    result ： 需要保存的变量
    rfile = opath+'\\'+routh+'\\'+f
    rExist = os.path.exists(rfile)
    if not rExist:
        os.makedirs(rfile)
        result.to_csv(rfile+'\\'+'wall tem-'+os.path.basename(q),header=columns)
    else:
        result.to_csv(rfile+'\\'+'wall tem-'+os.path.basename(q),header=columns) 
        
# 文件夹位置
ipath = r'E:\py_data\thermo'
opath = r'E:\py_output'
# 筛选后的数据列名称
columns = ['Time','N-110cm','N-90cm','N-60cm','N-30cm',
           'S-30cm','S-60cm','S-90cm','S-110cm']
# 数据需要的时间段 白天 07:00-22:00   晚上 22:00-07:00
start = '07:00'
end = '22:00'

file = os.listdir(ipath)
for f in file:
    qfile = glob.glob(ipath+'\\'+f+'\\'+'*.csv')
    for q in qfile:
        if os.path.basename(q)[-3:] == 'csv':
            # -----------------------选择需要分析的数据---------------------------#
            # ------------规定需要读取的列数---内容包括： Time时间列 + 数据列
            #n = [i for i in range(31,39)] # 使用列表推导式获取需要的通道号
            n = list(range(31,39)) # 或者使用list函数生成列表
            n.append(2) # 2是时间列对应的位置
            # ------------规定需要读取的行数
            # 需要将24小时数据分段，白天 07:00-21:00，晚上 22:00-06:00
            # 可使用参数skiprows  输入不需要的行数
            
            #-----------------------筛选符合要求的数据---------------------------#
            data1 = pd.read_csv(q,usecols=[2]) # 读取时间列
            k=[] # 储存符合条件的时间对应的位置
            # 07:00对应的位置
            for i in range(1440):
                if data1.iloc[i][0][11:16] == start:
                    k.append(i)
                    break
                else:
                    pass
            # 22:00对应的位置
            for j in range(1440):
                if data1.iloc[j][0][11:16] == end:
                    k.append(j)
                    break
                else:
                    pass

            #------------------白天 07:00-22:00-----------------#        
            data2 = pd.read_csv(q,usecols=n) # 参数usecols可以选定读取哪几列的数据，而不需要读取完整个文件然后再进行筛选
            day = data2.iloc[k[0]:k[1]] # 选择白天数据的范围,当然也可以在上面的表达式里使用skiprows
            # -------------画图-----------#
            l = [day.iloc[:,g] for g in range(1,9)] #选取两侧壁面的温度数据
            plot_box(1,l,s='day_picture')
            #------------保存数据------------#
            save_data(routh='day_data',result=day)
                
            # -------------------晚上 22:00-07:00-------------------#
            night = pd.read_csv(q,usecols=n,skiprows=list(range(k[0],k[1]+1))) # 跳过白天对应的数据
            #----画图-----#
            ll = [night.iloc[:,gg] for gg in range(1,9)]
            plot_box(2,ll,s='night_picture')
            #------------保存数据------------#
            save_data(routh='night_data',result=night)