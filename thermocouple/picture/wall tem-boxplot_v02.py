# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 11:17:25 2019

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

import os
import glob
import pandas as pd
import matplotlib.pyplot as plt

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
            plt.figure(num=1,figsize=(12,9),dpi=160)
            plt.style.use('ggplot')
            l = [day.iloc[:,g] for g in range(1,9)]
            plt.boxplot(l,flierprops = dict(markerfacecolor='g', marker='D'))
            plt.xlabel('Location',fontsize=12)
            plt.ylabel('Temperature(℃)',rotation=90,fontsize=12)
            plt.xticks(list(range(1,9)),
                       ('N-110cm','N-90cm','N-60cm','N-30cm','S-30cm','S-60cm','S-90cm','S-110cm')) # 也可以这样定义x轴刻度标签
            plt.ylim(15,55)
            plt.title(os.path.basename(q)[:-4],fontsize=12)
            
            #保存图片
            tfile = opath+'\\'+r'day_picture'+'\\'+f
            tExist = os.path.exists(tfile)
            if not tExist:
                os.makedirs(tfile)
                plt.savefig(tfile+'\\'+os.path.basename(q)[:-4]+'.png')
            else:
                plt.savefig(tfile+'\\'+os.path.basename(q)[:-4]+'.png')
            plt.close()
            #------------保存数据------------#
            rfile = opath+'\\'+r'day_data'+'\\'+f
            rExist = os.path.exists(rfile)
            if not rExist:
                os.makedirs(rfile)
                day.to_csv(rfile+'\\'+'wall tem-'+os.path.basename(q),header=columns)
            else:
                day.to_csv(rfile+'\\'+'wall tem-'+os.path.basename(q),header=columns)
               
                
            # -------------------晚上 22:00-07:00-------------------#
            night = pd.read_csv(q,usecols=n,skiprows=list(range(k[0],k[1]+1))) # 跳过白天对应的数据
            #----画图-----#
            plt.figure(num=2,figsize=(12,9),dpi=160)
            plt.style.use('ggplot')
            ll = [night.iloc[:,gg] for gg in range(1,9)]
            plt.boxplot(ll,flierprops = dict(markerfacecolor='g', marker='D'))
            plt.xlabel('Location',fontsize=12)
            plt.ylabel('Temperature(℃)',rotation=90,fontsize=12)
            plt.xticks(list(range(1,9)),
                       ('N-110cm','N-90cm','N-60cm','N-30cm','S-30cm','S-60cm','S-90cm','S-110cm'))
            plt.ylim(15,55)
            plt.title(os.path.basename(q)[:-4],fontsize=12)            
            
            #保存图片
            ttfile = opath+'\\'+r'night_picture'+'\\'+f
            ttExist = os.path.exists(ttfile)
            if not ttExist:
                os.makedirs(ttfile)
                plt.savefig(ttfile+'\\'+os.path.basename(q)[:-4]+'.png')
            else:
                plt.savefig(ttfile+'\\'+os.path.basename(q)[:-4]+'.png')
            plt.close()
            #------------保存数据------------#
            rrfile = opath+'\\'+r'night_data'+'\\'+f
            rrExist = os.path.exists(rrfile)
            if not rrExist:
                os.makedirs(rrfile)
                night.to_csv(rrfile+'\\'+'wall tem-'+os.path.basename(q),header=columns)
            else:
                night.to_csv(rrfile+'\\'+'wall tem-'+os.path.basename(q),header=columns)            
            
            
            
            
            
            
