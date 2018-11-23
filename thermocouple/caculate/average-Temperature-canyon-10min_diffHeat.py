# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 11:37:55 2018

@author: DELL
"""

# 先运行程序 batch-thermo-rename.py 将文件夹改名--可以清楚知道是哪个街谷的数据，同时将数据复制到 py_data
# 实现目标：此程序用于批量处理 将同一街谷不同朝向不同高度热电偶壁面温度数据进行平均 -- 进而对比不同高宽比和不同建筑热容的影响 -- 比单个固定点温度对比更具说服力
#--------------------------------------v01---------------------------------------#
# 获取各街谷热电偶数据，取10min平均，文件夹分类（不同街谷-不同日期-同一街谷不同高度测点的温度数据.csv）
#--------------------------------------v02---------------------------------------#
# 需要先运行avverage-Temperature-canyon-10min_v01.py，生成平均数据到文件夹py_output
# 实现算法：批量处理，将同一街谷不同高度不同朝向的热电偶温度进行平均，获取各街谷平均温度
#---------------------------------------v03--------------------------------------#
# 在avverage-Temperature-canyon-10min_v01.py程序运行后的基础上，获取各街谷平均温度，区别于v02版，此处划分数据文件夹--同一高宽比，按照不同建筑热容
# 画图
# len(f_file) == 7
# 前面的数据分析发现中空模型2:1街谷90cm测点位置有问题，故v01生成数据的时候将此测点除掉

import os 
import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


ipath = r'e:\py_output'
c_file = os.listdir(ipath)
p = ['HW1','HW2','HW3']

for c in c_file:
    u_file = os.listdir(ipath+'\\'+c)
    
    for u in u_file:
        
        f_file = glob.glob(ipath+'\\'+c+'\\'+u+'\\'+'*.csv')
        
        if len(f_file) == 7:
            
            l = []
            for i in range(7):
                a = pd.read_csv(f_file[i])
                l.append(a)
            
            tem_mean = (l[0].iloc[:,2] + l[1].iloc[:,2] + l[2].iloc[:,2] + l[3].iloc[:,2] +\
                        l[4].iloc[:,2] + l[5].iloc[:,2] + l[6].iloc[:,2])/len(f_file)
            
            time = l[0].iloc[:,1]
            
            result = pd.DataFrame({'time':time,'Temperature':tem_mean})
            columns = ['time','Temperature']
            
            for t in p:
                q_file = ipath+'\\'+r'diffHeat_whole canyon'+'\\'+r'data'+'\\'+t+'\\'+u
                qExist = os.path.exists(q_file)
                if not qExist:
                    os.makedirs(q_file)
                else:
                    pass
            if c[2:5] == p[0]:
                result.to_csv(ipath+'\\'+r'diffHeat_whole canyon'+'\\'+r'data'+'\\'+p[0]+'\\'+u+'\\'+c[-11:-6]+'.csv',columns=columns)
            if c[2:5] == p[1]:
                result.to_csv(ipath+'\\'+r'diffHeat_whole canyon'+'\\'+r'data'+'\\'+p[1]+'\\'+u+'\\'+c[-11:-6]+'.csv',columns=columns)
            if c[2:5] == p[2]:  
                result.to_csv(ipath+'\\'+r'diffHeat_whole canyon'+'\\'+r'data'+'\\'+p[2]+'\\'+u+'\\'+c[-11:-6]+'.csv',columns=columns)

        else:
            print('Error in:',c+'-'+u)

#----------------------------------画图----------------------------------------#


opath = ipath+'\\'+'diffHeat_whole canyon'
w_file = os.listdir(opath+'\\'+'data')
for w in w_file:
    e_file = os.listdir(opath+'\\'+'data'+'\\'+w)
    for e in e_file:
        g_file = glob.glob(opath+'\\'+'data'+'\\'+w+'\\'+e+'\\'+'*.csv')
        if len(g_file) == 2:
            data1 = pd.read_csv(g_file[0]) # empty
            data2 = pd.read_csv(g_file[1]) # sand

            x = np.arange(144)
            y1 = data1.loc[:,'Temperature']
            y2 = data2.loc[:,'Temperature'] 
            
            fig = plt.figure(figsize=(12,9),dpi=160)
            ax = fig.add_subplot(1,1,1)
            
            plt.plot(x,y1,linestyle='-',marker='D',markersize=5,markerfacecolor='none',markevery=6,linewidth=1,label='empty'+'-'+w+'-'+e)
            plt.plot(x,y2,linestyle='-',marker='o',markersize=5,markerfacecolor='none',markevery=6,linewidth=1,label='sandy'+'-'+w+'-'+e)
            
            plt.xlim(0,144)
            plt.ylim(22,42)
            plt.xlabel('time',fontsize=12)
            plt.ylabel('Temperature(℃)',rotation=90,fontsize=12)
            plt.minorticks_on()
            xticks = ax.set_xticks([0,24,48,72,96,120,144])
            xlabels = ax.set_xticklabels(['0:00','4:00','8:00','12:00','16:00','20:00','24:00'])
            yticks = ax.set_yticks([22,26,30,34,38,42])
            ylabels = ax.set_yticklabels(['22','26','30','34','38','42'])
            plt.legend(loc='best',fontsize=14,markerscale=1)
            plt.title('The average canyon temperature'+w+'-'+e,fontsize=12)
            plt.grid(True,linestyle='--')
            
            plt.savefig(opath+'\\'+'data'+'\\'+w+'\\'+e+'\\'+'The average canyon temperature-diffHeat'+w+'-'+e+'.png')
            tExist = os.path.exists(opath+'\\'+'total picture')
            if not tExist:
                os.mkdir(opath+'\\'+'total picture')
                plt.savefig(opath+'\\'+'total picture'+'\\'+'The average canyon temperature-diffHeat'+w+'-'+e+'.png')
            else:
                plt.savefig(opath+'\\'+'total picture'+'\\'+'The average canyon temperature-diffHeat'+w+'-'+e+'.png')
                
            plt.close()