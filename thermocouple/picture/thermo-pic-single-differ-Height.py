# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 09:29:44 2018

@author: DELL
"""

#此程序用于画单张图-热电偶-对比不同高度
import os
import glob
import shutil
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fname = os.listdir(r'C:\Users\DELL\Desktop\处理数据\分析数据\thermo\10min_average')
for f in fname[0:4]:
    gname = os.listdir(r'C:\Users\DELL\Desktop\处理数据\分析数据\thermo\10min_average'+'\\'+f)
    for g in gname:
        if g == '20170511':
            hname = os.listdir(r'C:\Users\DELL\Desktop\处理数据\分析数据\thermo\10min_average'+'\\'+f+'\\'+g)
            for h in hname:
                if h[-3:] == 'csv':
                    shutil.copyfile(r'C:\Users\DELL\Desktop\处理数据\分析数据\thermo\10min_average'+'\\'+f+'\\'+g+'\\'+h,r'E:\py_data\thermo\\'+h)

l = ['A','B','C','D','E','F']
for i in l:
    qExist = os.path.exists(r'e:\py_data\thermo\\'+i)
    if not qExist:
        os.mkdir(r'e:\py_data\thermo\\'+i)
    else:
        pass
q_file = os.listdir(r'e:\py_data\thermo')
for q in q_file:
    if q[-3:] == 'csv':
        for j in l:
            if q[-29] == j:
                shutil.move(r'e:\py_data\thermo\\'+q,r'e:\py_data\thermo\\'+j+'\\'+q)
            elif q[-30] == j:
                shutil.move(r'e:\py_data\thermo\\'+q,r'e:\py_data\thermo\\'+j+'\\'+q)

#--------------------------------画图------------------------------------------#
w_file = os.listdir(r'e:\py_data\thermo')
for w in w_file:

    e_file = glob.glob(r'e:\py_data\thermo\\'+w+'\\*.csv')
        
    data1 = pd.read_csv(e_file[1])
    data2 = pd.read_csv(e_file[2]) 
    data3 = pd.read_csv(e_file[3])
    data4 = pd.read_csv(e_file[0])

    x = np.arange(144)
    y1 = data1.ix[:,2]
    y2 = data2.ix[:,2]
    y3 = data3.ix[:,2]
    y4 = data4.ix[:,2]
    
    b = np.array([0,12,24,36,48,60,72,84,96,108,120,132,143])
    l1=[]
    for i in b:
        result1 = data1.ix[i,2]
        l1.append(result1)
    p1 = np.array(l1)

    l2=[]
    for i in b:
        result2 = data2.ix[i,2]
        l2.append(result2)
    p2 = np.array(l2)

    l3=[]
    for i in b:
        result3 = data3.ix[i,2]
        l3.append(result3)
    p3 = np.array(l3)

    l4=[]
    for i in b:
        result4 = data4.ix[i,2]
        l4.append(result4)
    p4 = np.array(l4)    

    fig = plt.figure(figsize = (10,8),dpi = 1000)
    ax = fig.add_subplot(1,1,1)
    
    if e_file[0][-24:-19] == 'empty':
        plt.plot(x,y1,'x-',markersize = 0.5,linewidth = 1.,label = e_file[1][37:95])
        plt.plot(x,y2,'D-',markersize = 0.5,linewidth = 1.,label = e_file[2][37:95])
        plt.plot(x,y3,'<-',markersize = 0.5,linewidth = 1.,label = e_file[3][37:95])
        plt.plot(x,y4,'s-',markersize = 0.5,linewidth = 1.,label = e_file[0][37:96])
 
    else:
        plt.plot(x,y1,'x-',markersize = 0.5,linewidth = 1.,label = e_file[1][37:94])
        plt.plot(x,y2,'D-',markersize = 0.5,linewidth = 1.,label = e_file[2][37:94])
        plt.plot(x,y3,'<-',markersize = 0.5,linewidth = 1.,label = e_file[3][37:94])
        plt.plot(x,y4,'s-',markersize = 0.5,linewidth = 1.,label = e_file[0][37:95])
 
    plt.scatter(b,p1,marker = 'x',s = 22)
    plt.scatter(b,p2,marker = 'D',s = 22)
    plt.scatter(b,p3,marker = '<',s = 22)
    plt.scatter(b,p4,marker = 's',s = 22)
   
    #设置坐标刻度和名称
    plt.xlim(0,144) #表示x轴的范围设置为0到24
    plt.ylim(22,46)
    plt.xlabel('time',fontsize = 12)
    plt.ylabel('T(℃)',rotation = 90,fontsize = 12)
    plt.minorticks_on()
    xticks = ax.set_xticks([0,24,48,72,96,120,143])  #此命令行可以确定x轴标签的位置
    xlabels = ax.set_xticklabels(['0:00','4:00','8:00','12:00','16:00','20:00','24:00'])  #此命令行可以命名x坐标轴的标签内容
    yticks = ax.set_yticks([22,26,30,34,38,42,46])
    ylabels = ax.set_yticklabels(['22','26','30','34','38','42','46'])
    #设置图注
    plt.legend(loc='best',fontsize = 10)
    plt.grid(True,linestyle='--')
    #plt.show()
    
    #保存图片，如果需要命名高宽比，可以在这里加条件判断语句
    if e_file[0][-24:-19] == 'empty':    
        plt.savefig('e:\py_output\\'+e_file[0][21:62]+e_file[0][-30:-4]+'.png')
    else:
        plt.savefig('e:\py_output\\'+e_file[0][21:62]+e_file[0][-29:-4]+'.png')
    plt.close()
    
