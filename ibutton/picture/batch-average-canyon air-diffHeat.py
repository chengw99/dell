# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 20:34:40 2018

@author: DELL
"""

#-----------------------------------step1-------------------------------------#
# 运行 batch-average-canyon air-v01.py，获取各街谷不同高度数据，为平均做准备

#----------------------------------step2（此程序）------------------------------#
# 比较不同建筑热容 街谷空气平均温度

import os 
import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipath = r'e:\py_data\ibutton'
opath = r'e:\py_output'
c_file = os.listdir(ipath)
p = ['HW1','HW2','HW3']


for c in c_file:
    u_file = os.listdir(ipath+'\\'+c)
    
    for u in u_file:
        
        f_file = glob.glob(ipath+'\\'+c+'\\'+u+'\\'+'*.csv')
        
        if len(f_file) == 4:
            
            l = []
            for i in range(4):
                a = pd.read_csv(f_file[i])
                l.append(a)
            
            tem_mean = (l[0].iloc[:,3] + l[1].iloc[:,3] + l[2].iloc[:,3] + l[3].iloc[:,3])/len(f_file)
            
            time = l[0].iloc[:,1]
            
            result = pd.DataFrame({'time':time,'Temperature':tem_mean})
            columns = ['time','Temperature']
            
            for t in p:
                q_file = opath+'\\'+r'data'+'\\'+t+'\\'+u
                qExist = os.path.exists(q_file)
                if not qExist:
                    os.makedirs(q_file)
                else:
                    pass
            if c[2:5] == p[0]:
                result.to_csv(opath+'\\'+r'data'+'\\'+p[0]+'\\'+u+'\\'+c[-5:]+'.csv',columns=columns)
            if c[2:5] == p[1]:
                result.to_csv(opath+'\\'+r'data'+'\\'+p[1]+'\\'+u+'\\'+c[-5:]+'.csv',columns=columns)
            if c[2:5] == p[2]:  
                result.to_csv(opath+'\\'+r'data'+'\\'+p[2]+'\\'+u+'\\'+c[-5:]+'.csv',columns=columns)

        else:
            print('Error in:',c+'-'+u)
            
#----------------------------------画图----------------------------------------#

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
            plt.title('The average canyon air temperature-'+w+'-'+e,fontsize=12)
            plt.grid(True,linestyle='--')
            
            plt.savefig(opath+'\\'+'data'+'\\'+w+'\\'+e+'\\'+'The average canyon air temperature-diffHeat'+w+'-'+e+'.png')
            tExist = os.path.exists(opath+'\\'+'total picture')
            if not tExist:
                os.mkdir(opath+'\\'+'total picture')
                plt.savefig(opath+'\\'+'total picture'+'\\'+'The average canyon air temperature-diffHeat'+w+'-'+e+'.png')
            else:
                plt.savefig(opath+'\\'+'total picture'+'\\'+'The average canyon air temperature-diffHeat'+w+'-'+e+'.png')
                
            plt.close()