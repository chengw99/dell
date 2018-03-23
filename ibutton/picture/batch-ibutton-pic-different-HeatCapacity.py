# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 14:33:03 2018

@author: DELL
"""
#此程序用于批量画图-ibutton空气温度数据-比较不同建筑热容
import os
import glob
import shutil
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


folderfile = os.listdir(r'C:\Users\DELL\Desktop\处理数据\分析数据\ibutton') #只需要在此文件夹中输入数据
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

qname = os.listdir(r'e:\py_data\ibutton')
for q in qname:
    #创建需要分类的空文件夹
    mfile = ['10cm','30cm','60cm','144cm'] #分类为高度
    nfile = ['HW1','HW2','HW3'] #分类为高宽比
    for m in mfile:
        mExist = os.path.exists(r'e:\py_data\ibutton\\'+q+'\\'+m)
        if not mExist:
            os.mkdir(r'e:\py_data\ibutton\\'+q+'\\'+m)
        else:
            pass
        for n in nfile:
            nExist = os.path.exists(r'e:\py_data\ibutton\\'+q+'\\'+m+'\\'+n)
            if not nExist:
                os.mkdir(r'e:\py_data\ibutton\\'+q+'\\'+m+'\\'+n)
            else:
                pass
    #将文件移动到对应的高度文件夹
    wfile = os.listdir(r'e:\py_data\ibutton\\'+q)
    pfile = ['10cm','30cm','60cm']
    for w in wfile:
        if w[-3:] == 'csv':
            for p in pfile:
                if w[-17:-13] == p:
                    shutil.move(r'e:\py_data\ibutton\\'+q+'\\'+w,r'e:\py_data\ibutton\\'+q+'\\'+p+'\\'+w)
                    
            if w[-18:-13] == '144cm':
                shutil.move(r'e:\py_data\ibutton\\'+q+'\\'+w,r'e:\py_data\ibutton\\'+q+'\\'+r'144cm\\'+w)
    #将文件移动到对应的高宽比文件夹
    #移动到10cm，30cm,60cm文件夹
    xfile = ['10cm','30cm','60cm']
    yfile = ['HW1','HW2','HW3']
    for x in xfile:
        tfile = os.listdir(r'e:\py_data\ibutton\\'+q+'\\'+x)
        for t in tfile:
            if t[-3:] == 'csv':
                for y in yfile:
                    if t[-23:-20] == y:
                        shutil.move(r'e:\py_data\ibutton\\'+q+'\\'+x+'\\'+t,r'e:\py_data\ibutton\\'+q+'\\'+x+'\\'+y+'\\'+t)
    #另外考虑144cm的原因是由于字符的长度不一样   
    gfile = os.listdir(r'e:\py_data\ibutton\\'+q+'\\'+r'144cm')
    jfile = ['HW1','HW2','HW3']
    for g in gfile:
        if g[-3:] == 'csv':
            for j in jfile:
                if g[-24:-21] == j or g[-26:-23]  == j: #新技能，用语句or增加筛选条件
                    shutil.move(r'e:\py_data\ibutton\\'+q+'\\'+r'144cm\\'+g,r'e:\py_data\ibutton\\'+q+'\\'+r'144cm\\'+j+'\\'+g)
    for i in xfile:
        hname = os.listdir(r'e:\py_data\ibutton\\'+q+'\\'+i)
        for h in hname:
            data = glob.glob(r'e:\py_data\ibutton\\'+q+'\\'+i+'\\'+h+'\\*.csv')
            if data[0][-34:-29] == 'empty':
                
                data1 = pd.read_csv(data[0])
                data2 = pd.read_csv(data[1])
                
                x = np.arange(24)
                y1 = data1.ix[:,2]
                y2 = data2.ix[:,2]
                
                fig = plt.figure()
                ax = fig.add_subplot(1,1,1)
            
                plt.plot(x,y1,'rD-',markersize = 6,markerfacecolor = 'none',linewidth = 1.8,label = data[0][-47:-4])
                plt.plot(x,y2,'ko-',markersize = 6,markerfacecolor = 'none',linewidth = 1.8,label = data[1][-46:-4])
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
                #plt.show()
                plt.savefig(r'e:\py_output\empty-sand model'+data[0][-23:-4]+'.png')
                plt.savefig(r'e:\py_data\ibutton\\'+q+'\\'+i+'\\'+h+'\\'+r'empty-sand model'+data[0][-23:-4]+'.png')
                plt.close()
                
            elif data[0][-33:-29] == 'sand':
                
                data1 = pd.read_csv(data[1])
                data2 = pd.read_csv(data[0])
                
                x = np.arange(24)
                y1 = data1.ix[:,2]
                y2 = data2.ix[:,2]
                            
                fig = plt.figure()
                ax = fig.add_subplot(1,1,1)
            
                plt.plot(x,y1,'rD-',markersize = 6,markerfacecolor = 'none',linewidth = 1.8,label = data[1][-47:-4])
                plt.plot(x,y2,'ko-',markersize = 6,markerfacecolor = 'none',linewidth = 1.8,label = data[0][-46:-4]) #原来可以连续使用保存图片的命令
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
                #plt.show()
                plt.savefig(r'e:\py_output\empty-sand model'+data[1][-23:-4]+'.png')
                plt.savefig(r'e:\py_data\ibutton\\'+q+'\\'+i+'\\'+h+'\\'+r'empty-sand model'+data[0][-23:-4]+'.png')
                plt.close()
    #144cm高的由于命名不一样，在后续批量处理的字符长度选取不一样导致不能一起循环，想改进的话可以考虑改名         
    #此部分因为中空1:1的E模型缺测，所以不能像上面作三个不同高宽比的遍历        
    file_2 = glob.glob(r'e:\py_data\ibutton\\'+q+'\\'+r'144cm\HW2\*.csv')
    data3 = pd.read_csv(file_2[0])
    data4 = pd.read_csv(file_2[3])
                
    x2 = np.arange(24)
    y3 = data3.ix[:,2]
    y4 = data4.ix[:,2]
    
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
            
    plt.plot(x,y3,'rD-',markersize = 6,markerfacecolor = 'none',linewidth = 1.8,label = file_2[0][-47:-4])
    plt.plot(x,y4,'ko-',markersize = 6,markerfacecolor = 'none',linewidth = 1.8,label = file_2[3][-48:-4]) #原来可以连续使用保存图片的命令
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
    #plt.show()
    plt.savefig(r'e:\py_output\empty-sand model'+file_2[3][-24:-4]+'.png')
    plt.savefig(r'e:\py_data\ibutton\\'+q+'\\'+r'144cm\HW2'+'\\'+r'empty-sand model'+file_2[3][-24:-4]+'.png')
    plt.close()
    
    #
    file_3 = glob.glob(r'e:\py_data\ibutton\\'+q+'\\'+r'144cm\HW3\*.csv')
    data5 = pd.read_csv(file_3[3])
    data6 = pd.read_csv(file_3[0])
                
    x3 = np.arange(24)
    y5 = data5.ix[:,2]
    y6 = data6.ix[:,2]
    
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
            
    plt.plot(x,y5,'rD-',markersize = 6,markerfacecolor = 'none',linewidth = 1.8,label = file_3[3][-47:-4])
    plt.plot(x,y6,'ko-',markersize = 6,markerfacecolor = 'none',linewidth = 1.8,label = file_3[0][-48:-4]) #原来可以连续使用保存图片的命令
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
    #plt.show()
    plt.savefig(r'e:\py_output\empty-sand model'+file_3[3][-24:-4]+'.png')
    plt.savefig(r'e:\py_data\ibutton\\'+q+'\\'+r'144cm\HW3'+'\\'+r'empty-sand model'+file_3[3][-24:-4]+'.png')
    plt.close()

Yexist = os.path.exists(r'C:\Users\DELL\Desktop\处理数据\picture\ibutton\对比不同建筑热容')
if not Yexist:
    os.mkdir(r'C:\Users\DELL\Desktop\处理数据\picture\ibutton\对比不同建筑热容')
else:
    pass

j_file = os.listdir(r'E:\py_data\ibutton')
for file in j_file:
    shutil.move(r'e:\py_data\ibutton\\'+file,r'C:\Users\DELL\Desktop\处理数据\picture\ibutton\对比不同建筑热容')
 
Uexist = os.path.exists(r'C:\Users\DELL\Desktop\处理数据\picture\ibutton\对比不同建筑热容\汇总')
if not Uexist:
    os.mkdir(r'C:\Users\DELL\Desktop\处理数据\picture\ibutton\对比不同建筑热容\汇总')
else:
    pass

t_file = os.listdir(r'e:\py_output')
for t in t_file:
    if t[-3:] == 'png':
        Pexist = os.path.exists(r'e:\py_output\\'+t[-12:-4])
        if not Pexist:
            os.mkdir(r'e:\py_output\\'+t[-12:-4])
        else:
            pass
        
lname = os.listdir('e:\py_output')
for l in lname:
    if l[-3:] == 'png':
        shutil.move(r'e:\py_output\\'+l,r'e:\py_output\\'+l[-12:-4]+'\\'+l)

l_file = os.listdir('e:\py_output')
for k in l_file:
    shutil.move(r'e:\py_output\\'+k,r'C:\Users\DELL\Desktop\处理数据\picture\ibutton\对比不同建筑热容\汇总'+'\\'+k)
        
            
        