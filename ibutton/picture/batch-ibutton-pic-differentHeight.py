# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 15:19:45 2018

@author: DELL
"""

#此程序用于批量作图：不同高度的ibutton温度图
import os
import glob
import shutil
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#复制文件到指定文件夹
folderfile = os.listdir(r'C:\Users\DELL\Desktop\处理数据\分析数据\ibutton')
for folder in folderfile:
    data_file = os.listdir(r'C:\Users\DELL\Desktop\处理数据\分析数据\ibutton\\'+folder+'\\'+r'每小时平均')
    for file in data_file:
        if file[-3:] == 'csv':
            isExists = os.path.exists('e:\py_data\ibutton\\'+folder)
            if not isExists:
                os.mkdir('e:\py_data\ibutton\\'+folder)
            else:
                pass
            shutil.copyfile(r'C:\Users\DELL\Desktop\处理数据\分析数据\ibutton\\'+folder+'\\'+r'每小时平均'+'\\'+file,'e:\\py_data\\ibutton\\'+folder+'\\'+file)


fname = os.listdir('e:\py_data\ibutton') #获取需要遍历的文件夹
for f in fname:
    #处理中空模型的数据
    l = ['B','C','F']
    for i in l:
        #筛选BCF的csv文件
        data_file = glob.glob(r'e:\py_data\ibutton\\'+f+'\\'+r'*['+str(i)+r'][1-4]*.csv')#glob通配符的使用可以更加精确地进行筛选
        #读取数据
        data1 = pd.read_csv(data_file[0])
        data2 = pd.read_csv(data_file[1])
        data3 = pd.read_csv(data_file[2])
        data4 = pd.read_csv(data_file[3])
        #坐标数据
        x = np.arange(24)
        y1 = data1.ix[:,2]
        y2 = data2.ix[:,2]
        y3 = data3.ix[:,2]
        y4 = data4.ix[:,2]

        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        #这里需要分类是因为装沙和中空模型命名的字符长度不一样
        #因此，这里的另一种思路是对原文件进行重命名，通过加点字符串使装沙和中空模型的字符长度一致，在后面的字符切片的范围就会一致，从而可以通过循环进行统一处理
        if i == 'B' or 'C' or 'F':
            #设置曲线性质
            #注意装沙模型与中空模型文件的字符长度不一样
            plt.plot(x,y1,'rD-',markersize = 6,markerfacecolor = 'none',linewidth = 0.8,label = data_file[0][-47:-4])
            plt.plot(x,y2,'ks-',markersize = 6,markerfacecolor = 'none',linewidth = 0.8,label = data_file[1][-47:-4])
            plt.plot(x,y3,'b^-',markersize = 6,markerfacecolor = 'none',linewidth = 0.8,label = data_file[2][-47:-4])
            plt.plot(x,y4,'mo-',markersize = 6,markerfacecolor = 'none',linewidth = 0.8,label = data_file[3][-48:-4])
            #设置坐标刻度和名称
            plt.xlim(0,24) #表示x轴的范围设置为0到24
            plt.ylim(22,46)
            plt.xlabel('time',fontsize = 12)
            plt.ylabel('T(℃)',rotation = 90,fontsize = 12)
            plt.minorticks_on()
            xticks = ax.set_xticks([0,4,8,12,16,20,24])  #此命令行可以确定x轴标签的位置
            xlabels = ax.set_xticklabels(['0:00','4:00','8:00','12:00','16:00','20:00','24:00'])  #此命令行可以命名x坐标轴的标签内容
            yticks = ax.set_yticks([22,26,30,34,38,42,46])
            ylabels = ax.set_yticklabels(['22','26','30','34','38','42','46'])
            #设置图注
            plt.legend(loc='best',fontsize = 10)
            #保存图片，如果需要命名高宽比，可以在这里加条件判断语句
            plt.savefig('e:\py_output\\'+data_file[0][-37]+'-empty model-'+data_file[0][-12:-4]+'.png')
            plt.close()
        else:
            pass
    #处理装沙模型的数据       
    p = ['A','D']
    for j in p:
        
        p_file = glob.glob(r'e:\py_data\ibutton\\'+f+'\\'+r'*['+str(j)+r'][1-4]*.csv')
        data1 = pd.read_csv(p_file[0])
        data2 = pd.read_csv(p_file[1])
        data3 = pd.read_csv(p_file[2])
        data4 = pd.read_csv(p_file[3])

        x = np.arange(24)
        y1 = data1.ix[:,2]
        y2 = data2.ix[:,2]
        y3 = data3.ix[:,2]
        y4 = data4.ix[:,2]

        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        
        if j == 'A' or 'D':

            plt.plot(x,y1,'rD-',markersize = 6,markerfacecolor = 'none',linewidth = 0.8,label = p_file[0][-46:-4])
            plt.plot(x,y2,'ks-',markersize = 6,markerfacecolor = 'none',linewidth = 0.8,label = p_file[1][-46:-4])
            plt.plot(x,y3,'b^-',markersize = 6,markerfacecolor = 'none',linewidth = 0.8,label = p_file[2][-46:-4])
            plt.plot(x,y4,'mo-',markersize = 6,markerfacecolor = 'none',linewidth = 0.8,label = p_file[3][-47:-4])
            
            plt.xlim(0,24) #表示x轴的范围设置为0到24
            plt.ylim(22,46)
            plt.xlabel('time',fontsize = 12)
            plt.ylabel('T(℃)',rotation = 90,fontsize = 12)
            plt.minorticks_on()
            xticks = ax.set_xticks([0,4,8,12,16,20,24])  #此命令行可以确定x轴标签的位置
            xlabels = ax.set_xticklabels(['0:00','4:00','8:00','12:00','16:00','20:00','24:00'])  #此命令行可以命名x坐标轴的标签内容
            yticks = ax.set_yticks([22,26,30,34,38,42,46])
            ylabels = ax.set_yticklabels(['22','26','30','34','38','42','46'])
        
            plt.legend(loc='best',fontsize = 10)
        
            plt.savefig('e:\py_output\\'+p_file[0][-36]+'-sand model-'+p_file[0][-12:-4]+'.png')
            plt.close()
        else:
            pass
        
    #处理装沙模型E位置的温度数据，因为5月份此位置缺测，不然可以将E的数据放在上一段程序当中
    u_file = glob.glob(r'e:\py_data\ibutton\\'+f+'\\'+r'*[E][1-3]*.csv')
    data1 = pd.read_csv(u_file[0])
    data2 = pd.read_csv(u_file[1])
    data3 = pd.read_csv(u_file[2])

    x = np.arange(24)
    y1 = data1.ix[:,2]
    y2 = data2.ix[:,2]
    y3 = data3.ix[:,2]

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    plt.plot(x,y1,'rD-',markersize = 6,markerfacecolor = 'none',linewidth = 0.8,label = u_file[0][-46:-4])
    plt.plot(x,y2,'ks-',markersize = 6,markerfacecolor = 'none',linewidth = 0.8,label = u_file[1][-46:-4])
    plt.plot(x,y3,'b^-',markersize = 6,markerfacecolor = 'none',linewidth = 0.8,label = u_file[2][-46:-4])
            
    plt.xlim(0,24) #表示x轴的范围设置为0到24
    plt.ylim(22,46)
    plt.xlabel('time',fontsize = 12)
    plt.ylabel('T(℃)',rotation = 90,fontsize = 12)
    plt.minorticks_on()
    xticks = ax.set_xticks([0,4,8,12,16,20,24])  #此命令行可以确定x轴标签的位置
    xlabels = ax.set_xticklabels(['0:00','4:00','8:00','12:00','16:00','20:00','24:00'])  #此命令行可以命名x坐标轴的标签内容
    yticks = ax.set_yticks([22,26,30,34,38,42,46])
    ylabels = ax.set_yticklabels(['22','26','30','34','38','42','46'])
        
    plt.legend(loc='best',fontsize = 10)
        
    plt.savefig('e:\py_output\\'+u_file[0][-36]+'-sand model-'+u_file[0][-12:-4]+'.png')
    plt.close()

#创建最终存放分析图的文件夹
pathadress = r'C:\Users\DELL\Desktop\处理数据\picture\ibutton\对比不同高度'
a = os.path.exists(pathadress)
if not a:
    os.mkdir(pathadress)
else:
    pass
 
folderaddress = 'e:\\py_output'      #目标路径
file_all = os.listdir(folderaddress) #路径下所有文件名
folderlist = []                      #存放文件夹的命名
os.chdir('e:\\py_output')            #修改工作目录

#创建指定文件夹
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
            #复制文件到目标文件夹
            shutil.copyfile(folderaddress+'\\'+i,folderaddress+'\\'+j+'\\'+i)
            #删除原来位置的文件
            os.remove(folderaddress+'\\'+i)

#把图移动到指定文件夹  
movename = os.listdir('e:\\py_output')
for file in movename:
    shutil.move('e:\\py_output\\'+file,r'C:\Users\DELL\Desktop\处理数据\picture\ibutton\对比不同高度')

#-----------------------清除输入数据文件夹的数据-----------------------------------
inputfile = os.listdir('e:\\py_data\\ibutton')
for filename in inputfile:
    shutil.rmtree('e:\\py_data\\ibutton\\'+filename)  #os.rmdir也可以删除文件夹，但只能删除空的文件夹

        

            
