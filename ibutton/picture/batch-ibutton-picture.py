# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 14:59:12 2018

@author: DELL
"""

#此程序用于批量作图
#画的是各个位置不同日期ibutton24小时温度图，采用数据是每小时平均的温度数据
#只有一条曲线
import os
import pandas as pd
import shutil
import matplotlib.pyplot as plt
import numpy as np



foldername = os.listdir(r'C:\Users\DELL\Desktop\处理数据\分析数据\ibutton')
for folder in foldername:
    filename = os.listdir(r'C:\Users\DELL\Desktop\处理数据\分析数据\ibutton\\'+folder+'\\'+r'每小时平均')
    os.chdir(r'C:\Users\DELL\Desktop\处理数据\分析数据\ibutton\\'+folder+'\\'+r'每小时平均')
    for file in filename:
        data = pd.read_csv(file)
    
        x = np.arange(24)
        y = data.ix[:,2]
  
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)  #貌似引入这个才可以调用后面的方法set_xticks
        plt.plot(x,y,'rD-',markersize = 6,markerfacecolor = 'none',linewidth = 1.5,label = file[:-4])
        plt.xlim(0,24) #表示x轴的范围设置为0到24
        plt.ylim(22,46)
        plt.xlabel('time',fontsize = 12)
        plt.ylabel('T(℃)',rotation = 90,fontsize = 12)
        plt.minorticks_on()
        xticks = ax.set_xticks([0,4,8,12,16,20,24])  #此命令行可以确定x轴标签的位置
        xlabels = ax.set_xticklabels(['0:00','4:00','8:00','12:00','16:00','20:00','24:00'])  #此命令行可以命名x坐标轴的标签内容
        yticks = ax.set_yticks([22,26,30,34,38,42,46])
        ylabels = ax.set_yticklabels(['22','26','30','34','38','42','46'])
        plt.legend(loc='best',fontsize = 12)
        
        plt.savefig('e:\\py_output\\'+file[:-4]+'.png')
        plt.close()
        
#---------------------按日期生成文件夹，筛选相同日期的所有文件-------------------------
#只需要修改文件名(提供分类标志）以及name[]内数字的范围即可进行任意文件夹分类
folderaddress = 'e:\\py_output'      #目标路径
file_all = os.listdir(folderaddress) #路径下所有文件名
folderlist = []                      #存放文件夹的命名
os.chdir('e:\\py_output')            #修改工作目录

for name in file_all:
    if name[-3:] == 'png':            #此处可设定移动文件的类型 
        folderlist.append(name[-12:-4])  #此处获取所需对应的文件夹名
        isExists = os.path.exists(name[-12:-4]) #判断文件夹是否存在
        if not isExists:                     #加一个判断语句，就不会因为文件已存在而报错
            os.mkdir(folderaddress+'\\'+name[-12:-4])
        else:
            pass

#移动文件    
for i in file_all:                    #遍历所有目标文件
    for j in folderlist:              #遍历文件夹 
        #判断文件是否存在以及文件名与文件夹名是否一致，进行定向筛选
        if os.path.isfile(folderaddress+'\\'+i) == True and i[-12:-4] == j:
            #移动文件到目标文件夹
            shutil.copyfile(folderaddress+'\\'+i,folderaddress+'\\'+j+'\\'+i)
            #删除原来位置的文件
            os.remove(folderaddress+'\\'+i)
#------------------------将整理好的文件夹移动到指定的文件夹--------------------------
filenames = os.listdir('e:\\py_output')
for file in filenames:
    shutil.move('e:\\py_output\\'+file,r'C:\Users\DELL\Desktop\处理数据\ibutton')

