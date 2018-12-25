# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 12:23:24 2018

@author: DELL
"""

import os
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#----------------------------------处理数据-------------------------------------#

ipath = r'E:\py_output\T_average_whole canyon'
opath = r'E:\py_output'
p=['empty','sandy']

c_file = os.listdir(ipath)
for c in c_file:

    file = glob.glob(ipath+'\\'+c+'\\'+'*.csv')
    for f in file:
        data = pd.read_csv(f)
        tem = data.iloc[:,2]
        
        tem_mean = tem.mean() #平均值
        tem_DTR = tem.max() - tem.min() # 最大值-最小值
        time_max = data.iloc[:,1][tem.argmax()] # 最大值对应的时间

        result = pd.DataFrame({'tem_mean':[tem_mean],'tem_DTR':[tem_DTR],'time_max':[time_max]})
        columns = ['tem_mean','tem_DTR','time_max']
        
        for t in p:
            q_file = opath+'\\'+'Daily cycle temperature characteristic'+'\\'+'data'+'\\'+c+'\\'+t
            qExist = os.path.exists(q_file)
            if not qExist:
                os.makedirs(q_file)
            else:
                pass
        wfile = opath+'\\'+'Daily cycle temperature characteristic'+'\\'+'data'+'\\'+c
        if os.path.basename(f)[6:11] == p[0]:
            result.to_csv(wfile+'\\'+p[0]+'\\'+os.path.basename(f)[2:],columns=columns)
        else:
            result.to_csv(wfile+'\\'+p[1]+'\\'+os.path.basename(f)[2:],columns=columns)



#-----------------------------画图---------------------------------------------#

rpath = r'E:\py_output\Daily cycle temperature characteristic\data'
upath = r'E:\py_output\Daily cycle temperature characteristic\total picture'
t_file = os.listdir(rpath)
for t in t_file:
    u_file = os.listdir(rpath+'\\'+t)
    for u in u_file:
        mfile = glob.glob(rpath+'\\'+t+'\\'+u+'\\'+'*.csv')
        if len(mfile) == 3:
            data1 = pd.read_csv(mfile[0]) #HW1
            data2 = pd.read_csv(mfile[1]) #HW2
            data3 = pd.read_csv(mfile[2]) #HW3
            
            '''
            #平均温度
            x1 = np.arange(3)
            tem_mean1 = data1.loc[:,'tem_mean'] 
            tem_mean2 = data2.loc[:,'tem_mean']
            tem_mean3 = data3.loc[:,'tem_mean']
            k=[]
            k.append(tem_mean1)
            k.append(tem_mean2)
            k.append(tem_mean3)
            
            fig1 = plt.figure(figsize=(10,8),dpi=160)
            ax1 = fig1.add_subplot(1,1,1)
            
            plt.plot(x1,np.array(k),linestyle='-',marker='D',markersize=5,markerfacecolor='none',linewidth=1.5,label=u+'-'+t)
            plt.xlabel('H/W',fontsize=12)
            xticks = ax1.set_xticks([0,1,2])
            xlabels = ax1.set_xticklabels(['1','2','3'])
            plt.ylabel('Average temperature(℃)',rotation=90,fontsize=12)
            plt.legend(loc='best',fontsize=14)
            tExist = os.path.exists(upath+'\\'+'Average temperature')
            if not tExist:
                os.makedirs(upath+'\\'+'Average temperature')
                plt.savefig(upath+'\\'+'Average temperature'+'\\'+'tem_mean-'+u+'-'+t+'.png')
            else:
                plt.savefig(upath+'\\'+'Average temperature'+'\\'+'tem_mean-'+u+'-'+t+'.png')
            
            
            '''
            '''
            #DTR
            x2 = np.arange(3)
            tem_DTR1 = data1.loc[:,'tem_DTR'] 
            tem_DTR2 = data2.loc[:,'tem_DTR']
            tem_DTR3 = data3.loc[:,'tem_DTR']
            kk=[]
            kk.append(tem_DTR1)
            kk.append(tem_DTR2)
            kk.append(tem_DTR3)
            
            fig2 = plt.figure(figsize=(10,8),dpi=160)
            ax2 = fig2.add_subplot(1,1,1)
            
            plt.plot(x2,np.array(kk),linestyle='-',marker='o',markersize=5,markerfacecolor='none',linewidth=1.5,label=u+'-'+t)
            plt.xlabel('H/W',fontsize=12)
            xticks = ax2.set_xticks([0,1,2])
            xlabels = ax2.set_xticklabels(['1','2','3'])
            plt.ylabel('Temperature amplitude(℃)',rotation=90,fontsize=12)
            plt.legend(loc='best',fontsize=14)
            tExist = os.path.exists(upath+'\\'+'Temperature range')
            if not tExist:
                os.makedirs(upath+'\\'+'Temperature range')
                plt.savefig(upath+'\\'+'Temperature range'+'\\'+'tem_DTR-'+u+'-'+t+'.png')
            else:
                plt.savefig(upath+'\\'+'Temperature range'+'\\'+'tem_DTR-'+u+'-'+t+'.png')
            '''
            
            
            #time_max
            x3 = np.arange(3)
            time_max1 = data1.loc[:,'time_max'] 
            time_max2 = data2.loc[:,'time_max']
            time_max3 = data3.loc[:,'time_max']
            kkk=[]
            kkk.append(time_max1[0][:2]+time_max1[0][3:])
            kkk.append(time_max2[0][:2]+time_max2[0][3:])
            kkk.append(time_max3[0][:2]+time_max3[0][3:])
            
            fig3 = plt.figure(figsize=(10,8),dpi=160)
            ax3 = fig3.add_subplot(1,1,1)
            
            plt.plot(x3,kkk,linestyle='-',marker='o',markersize=5,markerfacecolor='none',linewidth=1.5,label=u+'-'+t)
            plt.xlabel('H/W',fontsize=12)
            xticks = ax3.set_xticks([0,1,2])
            xlabels = ax3.set_xticklabels(['1','2','3'])
            plt.ylabel('Time(h)',rotation=90,fontsize=12)
            plt.legend(loc='best',fontsize=14)
            tExist = os.path.exists(upath+'\\'+'Time max')
            if not tExist:
                os.makedirs(upath+'\\'+'Time max')
                plt.savefig(upath+'\\'+'Time max'+'\\'+'time_max-'+u+'-'+t+'.png')
            else:
                plt.savefig(upath+'\\'+'Time max'+'\\'+'time_max-'+u+'-'+t+'.png')
             
              
            plt.close()
  