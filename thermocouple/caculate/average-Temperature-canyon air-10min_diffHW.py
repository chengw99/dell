# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 15:56:33 2018

@author: DELL
"""

#----------------------------------step1--------------------------------------#
# 先运行程序 batch-thermo-rename.py 将文件夹改名--可以清楚知道是哪个街谷的数据，同时将数据复制到 py_data
# 实现目标：此程序用于批量处理 将同一街谷不同高度热电偶 空气 温度数据进行平均 -- 进而对比不同高宽比和不同建筑热容的影响 -- 比单个固定点温度对比更具说服力
#----------------------------------step2--------------------------------------#
# 运行avverage-Temperature-canyon-10min_v01.py程序
# 获取各街谷热电偶数据，取10min平均，文件夹分类（不同街谷-不同日期-同一街谷不同高度测点的温度数据.csv）
# 此处考虑的高度有10cm, 30cm, 60cm, 144cm（分别对应热电偶通道106,107,108,109）
#----------------------------------step3(此程序)-------------------------------#
# 在avverage-Temperature-canyon-10min_v01.py程序运行后的基础上，获取各街谷空气平均温度，，此处划分数据文件夹--同一建筑热容，按照不同高宽比
# 画图
# len(f_file) == 4

import os 
import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#---------------------------------获取数据--------------------------------------#
ipath = r'E:\py_output'
c_file = os.listdir(ipath)
p=['empty','sandy']


for c in c_file:
    u_file = os.listdir(ipath+'\\'+c)
    
    for u in u_file:

        f_file = glob.glob(ipath+'\\'+c+'\\'+u+'\\'+'*.csv')
        
        if len(f_file) == 4:
            
            try:
                
                l = []
                for i in range(4):
                    a = pd.read_csv(f_file[i])
                    l.append(a)
                
                tem_mean = (l[0].iloc[:,2] + l[1].iloc[:,2] + l[2].iloc[:,2] + l[3].iloc[:,2])/len(f_file)
                
                time = l[0].iloc[:,1]
                
                result = pd.DataFrame({'time':time,'Temperature':tem_mean})
                columns = ['time','Temperature']
                
                for t in p:
                    q_file = ipath+'\\'+r'diffHW_whole canyon air'+'\\'+r'data'+'\\'+t+'\\'+u
                    qExist = os.path.exists(q_file)
                    if not qExist:
                        os.makedirs(q_file)
                    else:
                        pass
                if c[-11:-6] == p[0]:
                    result.to_csv(ipath+'\\'+r'diffHW_whole canyon air'+'\\'+r'data'+'\\'+p[0]+'\\'+u+'\\'+c[2:5]+'.csv',columns=columns)
                else:
                    result.to_csv(ipath+'\\'+r'diffHW_whole canyon air'+'\\'+r'data'+'\\'+p[1]+'\\'+u+'\\'+c[2:5]+'.csv',columns=columns)
            
            except:
                
                pass
            
        else:
            print('Error in:',c+'-'+u)

#----------------------------------画图----------------------------------------#

opath = ipath+'\\'+'diffHW_whole canyon air'
w_file = os.listdir(opath+'\\'+'data')
for w in w_file:
    e_file = os.listdir(opath+'\\'+'data'+'\\'+w)
    for e in e_file:
        g_file = glob.glob(opath+'\\'+'data'+'\\'+w+'\\'+e+'\\'+'*.csv')
        if len(g_file) == 3:
            data1 = pd.read_csv(g_file[0])
            data2 = pd.read_csv(g_file[1])
            data3 = pd.read_csv(g_file[2])

            x = np.arange(144)
            y1 = data1.loc[:,'Temperature'] # H/W=1
            y2 = data2.loc[:,'Temperature'] # H/W=2
            y3 = data3.loc[:,'Temperature'] # H/W=3
            
            fig = plt.figure(figsize=(12,9),dpi=160)
            ax = fig.add_subplot(1,1,1)
            
            plt.plot(x,y1,linestyle='-',marker='D',markersize=5,markerfacecolor='none',markevery=6,linewidth=0.8,label='HW1'+'-'+w+'-'+e)
            plt.plot(x,y2,linestyle='-',marker='o',markersize=5,markerfacecolor='none',markevery=6,linewidth=0.8,label='HW2'+'-'+w+'-'+e)
            plt.plot(x,y3,linestyle='-',marker='s',markersize=5,markerfacecolor='none',markevery=6,linewidth=0.8,label='HW3'+'-'+w+'-'+e)
            
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
            plt.title('The average canyon air temperature'+w+'-'+e,fontsize=12)
            plt.grid(True,linestyle='--')
            
            plt.savefig(opath+'\\'+'data'+'\\'+w+'\\'+e+'\\'+'The average canyon air temperature-'+w+'-'+e+'.png')
            tExist = os.path.exists(opath+'\\'+'total picture')
            if not tExist:
                os.mkdir(opath+'\\'+'total picture')
                plt.savefig(opath+'\\'+'total picture'+'\\'+'The average canyon air temperature-'+w+'-'+e+'.png')
            else:
                plt.savefig(opath+'\\'+'total picture'+'\\'+'The average canyon air temperature-'+w+'-'+e+'.png')
                
            plt.close()