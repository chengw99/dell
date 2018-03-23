# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 09:12:54 2018

@author: DELL
"""
#ibutton-对比不同高度的空气温度图v02版本
#增加的功能是：有图的同时有对应的温度数据，方便以后用origin画图，并且有汇总的图（按日期分开）
import os
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

s_file = os.listdir(r'e:\py_data\ibutton')

for s in s_file:
    
    #先创建相应的文件夹
    m = ['empty model','sand model']
    n = ['HW1','HW2','HW3']
    for i in m:
        mExist = os.path.exists(r'e:\py_data\ibutton\\'+s+'\\'+i)
        if not mExist:
            os.mkdir(r'e:\py_data\ibutton\\'+s+'\\'+i)
        else:
            pass
        for j in n:
            nExist = os.path.exists(r'e:\py_data\ibutton\\'+s+'\\'+i+'\\'+j)
            if not nExist:
                os.mkdir(r'e:\py_data\ibutton\\'+s+'\\'+i+'\\'+j)
            else:
                pass
    #将中空模型文件和装沙模型文件分隔开
    d_file = os.listdir(r'e:\py_data\ibutton\\'+s)
    for d in d_file:
        if d[-3:] == 'csv':
            if d[13:17] == 'sand':
                shutil.move(r'e:\py_data\ibutton\\'+s+'\\'+d,r'e:\py_data\ibutton\\'+s+'\\'+r'sand model'+'\\'+d)
            elif d[13:18] == 'empty':
                shutil.move(r'e:\py_data\ibutton\\'+s+'\\'+d,r'e:\py_data\ibutton\\'+s+'\\'+r'empty model'+'\\'+d)
                
    #将不同高宽比的文件放入对应的高宽比文件夹
    for q in m:    
        f_file = os.listdir(r'e:\py_data\ibutton\\'+s+'\\'+q)
        for f in f_file:
            if f[-3:] == 'csv':
                for w in n:
                    if f[23:26] == w or f[24:27] == w:
                        shutil.move(r'e:\py_data\ibutton\\'+s+'\\'+q+'\\'+f,r'e:\py_data\ibutton\\'+s+'\\'+q+'\\'+w+'\\'+f)
    
    #画图-中空模型
    for h in n:
        ename = os.listdir(r'e:\py_data\ibutton\\'+s+'\\'+r'empty model'+'\\'+h)
        #获取满足条件的csv文件
        p = []
        for e in ename:
            if e[28] == 'h':
                p.append(e)
            else:
                pass
            
        #读取数据
        path = r'e:\py_data\ibutton\\'+s+'\\'+r'empty model'+'\\'+h+'\\'
        data1 = pd.read_csv(path + p[0])
        data2 = pd.read_csv(path + p[1])
        data3 = pd.read_csv(path + p[2])
        data4 = pd.read_csv(path + p[3])
        #坐标数据
        x = np.arange(24)
        y1 = data1.ix[:,2]
        y2 = data2.ix[:,2]
        y3 = data3.ix[:,2]
        y4 = data4.ix[:,2]

        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        
        #注意装沙模型与中空模型文件的字符长度不一样
        plt.plot(x,y1,'rD-',markersize = 6,markerfacecolor = 'none',linewidth = 0.8,label = p[0][:-4])
        plt.plot(x,y2,'ks-',markersize = 6,markerfacecolor = 'none',linewidth = 0.8,label = p[1][:-4])
        plt.plot(x,y3,'b^-',markersize = 6,markerfacecolor = 'none',linewidth = 0.8,label = p[2][:-4])
        plt.plot(x,y4,'mo-',markersize = 6,markerfacecolor = 'none',linewidth = 0.8,label = p[3][:-4])
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
        plt.savefig('e:\py_output\\'+p[0][10]+'-empty model-'+p[0][24:27]+'-'+p[0][-12:-4]+'.png')
        plt.savefig(r'e:\py_data\ibutton\\'+s+'\\'+r'empty model'+'\\'+h+'\\'+p[0][10]+'-empty model-'+p[0][24:27]+'-'+p[0][-12:-4]+'.png')
        plt.close()
        
    #画图-装沙模型
        
    for ll in n:
                #由于E模型缺测导致要分开，若不缺测可去掉这一段代码   
        if ll == 'HW1':
            fname = os.listdir(r'e:\py_data\ibutton\\'+s+'\\'+r'sand model'+'\\'+ll)
            v=[] #E模型的数据
            for f in fname:
                if f[27] == 'h':
                    v.append(f)
         
            #读取数据
            path = r'e:\py_data\ibutton\\'+s+'\\'+r'sand model'+'\\'+ll+'\\'
            data1 = pd.read_csv(path + v[0])
            data2 = pd.read_csv(path + v[1])
            data3 = pd.read_csv(path + v[2])
            #坐标数据
            x = np.arange(24)
            y1 = data1.ix[:,2]
            y2 = data2.ix[:,2]
            y3 = data3.ix[:,2]
            
            fig = plt.figure()
            ax = fig.add_subplot(1,1,1)
            
            #注意装沙模型与中空模型文件的字符长度不一样
            plt.plot(x,y1,'rD-',markersize = 6,markerfacecolor = 'none',linewidth = 0.8,label = v[0][:-4])
            plt.plot(x,y2,'ks-',markersize = 6,markerfacecolor = 'none',linewidth = 0.8,label = v[1][:-4])
            plt.plot(x,y3,'b^-',markersize = 6,markerfacecolor = 'none',linewidth = 0.8,label = v[2][:-4])
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
            plt.savefig('e:\py_output\\'+v[0][10]+'-sand model-'+v[0][23:26]+'-'+v[0][-12:-4]+'.png')
            plt.savefig(r'e:\py_data\ibutton\\'+s+'\\'+r'sand model'+'\\'+ll+'\\'+v[0][10]+'-sand model-'+v[0][23:26]+'-'+v[0][-12:-4]+'.png')
            plt.close()
        
        else:
            pass
             
    for hh in ['HW2','HW3']:
        gname = os.listdir(r'e:\py_data\ibutton\\'+s+'\\'+r'sand model'+'\\'+hh)
        l=[] #A和D模型的数据
        for g in gname:
            if g[10] == 'A' or 'D':
                if g[27] == 'h':
                    l.append(g)
        
        #读取数据
        path = r'e:\py_data\ibutton\\'+s+'\\'+r'sand model'+'\\'+hh+'\\'
        data1 = pd.read_csv(path + l[0])
        data2 = pd.read_csv(path + l[1])
        data3 = pd.read_csv(path + l[2])
        data4 = pd.read_csv(path + l[3])
        #坐标数据
        x = np.arange(24)
        y1 = data1.ix[:,2]
        y2 = data2.ix[:,2]
        y3 = data3.ix[:,2]
        y4 = data4.ix[:,2]

        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        
        #注意装沙模型与中空模型文件的字符长度不一样
        plt.plot(x,y1,'rD-',markersize = 6,markerfacecolor = 'none',linewidth = 0.8,label = l[0][:-4])
        plt.plot(x,y2,'ks-',markersize = 6,markerfacecolor = 'none',linewidth = 0.8,label = l[1][:-4])
        plt.plot(x,y3,'b^-',markersize = 6,markerfacecolor = 'none',linewidth = 0.8,label = l[2][:-4])
        plt.plot(x,y4,'mo-',markersize = 6,markerfacecolor = 'none',linewidth = 0.8,label = l[3][:-4])
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
        plt.savefig('e:\py_output\\'+l[0][10]+'-sand model-'+l[0][23:26]+'-'+l[0][-12:-4]+'.png')
        plt.savefig(r'e:\py_data\ibutton\\'+s+'\\'+r'sand model'+'\\'+hh+'\\'+l[0][10]+'-sand model-'+l[0][23:26]+'-'+l[0][-12:-4]+'.png')
        plt.close()
#创建最终存放图片的额文件夹
rExist = os.path.exists(r'C:\Users\DELL\Desktop\处理数据\picture\ibutton\对比不同高度')
if not rExist:
    os.mkdir(r'C:\Users\DELL\Desktop\处理数据\picture\ibutton\对比不同高度')
else:
    pass

#移动文件夹到指定文件夹
t_file = os.listdir(r'e:\py_data\ibutton')
for t in t_file:
    shutil.move(r'e:\py_data\ibutton\\'+t,r'C:\Users\DELL\Desktop\处理数据\picture\ibutton\对比不同高度'+'\\'+t)
    

#创建汇总文件夹，并移动图片按日期分类，再移动到汇总文件夹
u_file = os.listdir(r'e:\py_output')
for u in u_file:
    if u[-3:] == 'png':
        uExist = os.path.exists(r'e:\py_output\\'+u[-12:-4])
        if not uExist:
            os.mkdir(r'e:\py_output\\'+u[-12:-4])
        else:
            pass
        
b_file = os.listdir(r'e:\py_output')
for b in b_file:
    if b[-3:] == 'png':
        shutil.move(r'e:\py_output\\'+b,r'e:\py_output\\'+b[-12:-4]+'\\'+b)

qExist = os.path.exists(r'C:\Users\DELL\Desktop\处理数据\picture\ibutton\对比不同高度\汇总')
if not qExist:
    os.mkdir(r'C:\Users\DELL\Desktop\处理数据\picture\ibutton\对比不同高度\汇总')
else:
    pass

h_file = os.listdir(r'e:\py_output')
for file in h_file:
    shutil.move(r'e:\py_output\\'+file,r'C:\Users\DELL\Desktop\处理数据\picture\ibutton\对比不同高度\汇总'+'\\'+file)
