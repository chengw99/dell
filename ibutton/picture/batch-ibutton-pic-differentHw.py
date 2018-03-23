# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 20:20:24 2018

@author: DELL
"""

#此程序用于画图-ibutton温度数据-对比不同额高宽比

import os
import glob
import shutil
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#复制文件到指定文件夹
#注意：因为进行了文件操作以及遍历，如果路径发生改变，一些切片操作要进行相应的处理
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

zfile = os.listdir(r'e:\py_data\ibutton')
for z in zfile:
    #----------------------创建对应4个高度的文件夹---------------------------------
    number = [10,30,60,144]
    for i in number:
        isExist = os.path.exists(r'e:\py_data\ibutton\\'+z+'\\'+str(i)+r'cm')
        if not isExist:
            os.mkdir(r'e:\py_data\ibutton\\'+z+'\\'+str(i)+r'cm')
        else:
            pass
        asExist = os.path.exists(r'e:\py_data\ibutton\\'+z+'\\'+str(i)+r'cm'+'\\'+r'empty model')
        if not asExist:
            os.mkdir(r'e:\py_data\ibutton\\'+z+'\\'+str(i)+r'cm'+'\\'+r'empty model')
        else:
            pass
        bsExist = os.path.exists(r'e:\py_data\ibutton\\'+z+'\\'+str(i)+r'cm'+'\\'+r'sand model')
        if not bsExist:
            os.mkdir(r'e:\py_data\ibutton\\'+z+'\\'+str(i)+r'cm'+'\\'+r'sand model')
        else:
            pass
    #-------------------将对应高度的文件移动到对应的高度文件夹------------------------
    #先移动到高度文件夹里    
    file_all = os.listdir(r'e:\py_data\ibutton\\'+z)
    folderlist = [10,30,60]
    for file in file_all:
        if file[-3:] == 'csv':
            for a in folderlist:
                if file[-17:-15] == str(a):
                    shutil.copyfile(r'e:\py_data\ibutton\\'+z+'\\'+file,r'e:\py_data\ibutton\\'+z+'\\'+str(a)+r'cm'+'\\'+file)
                    os.remove(r'e:\py_data\ibutton\\'+z+'\\'+file)
            if file[-18:-15] == '144':
                shutil.copyfile(r'e:\py_data\ibutton\\'+z+'\\'+file,r'e:\py_data\ibutton\\'+z+'\\'+r'144cm'+'\\'+file)
                os.remove(r'e:\py_data\ibutton\\'+z+'\\'+file)
    #按照中空模型和装沙模型将文件分类放入文件夹
    tfile = os.listdir(r'e:\py_data\ibutton\\'+z)
    for t in tfile:
        qfile = os.listdir(r'e:\py_data\ibutton\\'+z+'\\'+t)
        for q in qfile:
            if q[-3:] == 'csv':
                if q[13:17] == 'sand':
                    shutil.copyfile(r'e:\py_data\ibutton\\'+z+'\\'+t+'\\'+q,r'e:\py_data\ibutton\\'+z+'\\'+t+'\\'+r'sand model\\'+q)
                    os.remove(r'e:\py_data\ibutton\\'+z+'\\'+t+'\\'+q)
                if q[13:18] == 'empty':
                    shutil.copyfile(r'e:\py_data\ibutton\\'+z+'\\'+t+'\\'+q,r'e:\py_data\ibutton\\'+z+'\\'+t+'\\'+r'empty model\\'+q)
                    os.remove(r'e:\py_data\ibutton\\'+z+'\\'+t+'\\'+q)
                    
    wfile = ['10cm','30cm','60cm']
    for w in wfile:
        efile = ['empty model','sand model']
        for e in efile:
            if e == 'empty model':
            
                empty_data=glob.glob(r'e:\py_data\ibutton\\'+z+'\\'+w+'\\'+e+'\\*.csv')
            
                data1 = pd.read_csv(empty_data[0])
                data2 = pd.read_csv(empty_data[2])
                data3 = pd.read_csv(empty_data[1])
                
                x = np.arange(24)
                y1 = data1.ix[:,2]
                y2 = data2.ix[:,2]
                y3 = data3.ix[:,2]
            
                fig = plt.figure()
                ax = fig.add_subplot(1,1,1)
            
                plt.plot(x,y1,'rD-',markersize = 6,markerfacecolor = 'none',linewidth = 0.8,label = empty_data[0][-47:-4])
                plt.plot(x,y2,'bo-',markersize = 6,markerfacecolor = 'none',linewidth = 0.8,label = empty_data[2][-47:-4])
                plt.plot(x,y3,'gs-',markersize = 6,markerfacecolor = 'none',linewidth = 0.8,label = empty_data[1][-47:-4])
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
                plt.savefig(r'e:\py_data\ibutton\\'+z+'\\'+w+'\\'+e+'\\'+'empty model-'+empty_data[0][-17:-4]+'.png')
                plt.close()
            
            
            else:
            
                sand_data=glob.glob(r'e:\py_data\ibutton\\'+z+'\\'+w+'\\'+e+'\\*.csv')
      
                data4 = pd.read_csv(sand_data[2])
                data5 = pd.read_csv(sand_data[0])
                data6 = pd.read_csv(sand_data[1])
            
                x2 = np.arange(24)
                y4 = data4.ix[:,2]
                y5 = data5.ix[:,2]
                y6 = data6.ix[:,2]
            
                fig = plt.figure()
                ax = fig.add_subplot(1,1,1)
            
                plt.plot(x2,y4,'rD-',markersize = 6,markerfacecolor = 'none',linewidth = 0.8,label = sand_data[2][-46:-4])
                plt.plot(x2,y5,'bo-',markersize = 6,markerfacecolor = 'none',linewidth = 0.8,label = sand_data[0][-46:-4])
                plt.plot(x2,y6,'gs-',markersize = 6,markerfacecolor = 'none',linewidth = 0.8,label = sand_data[1][-46:-4])
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
                plt.savefig(r'e:\\py_data\ibutton\\'+z+'\\'+w+'\\'+e+'\\'+r'sand model-'+sand_data[0][-17:-4]+r'.png')
                plt.close()
                
    ufile = ['empty model','sand model']
    for u in ufile:
        if u == 'empty model':
        
            p_data = glob.glob(r'e:\py_data\ibutton\\'+z+'\\144cm\\'+u+r'\*.csv')
        
            data7 = pd.read_csv(p_data[0])
            data8 = pd.read_csv(p_data[6])
            data9 = pd.read_csv(p_data[3])
                    
            x = np.arange(24)
            y7 = data7.ix[:,2]
            y8 = data8.ix[:,2]
            y9 = data9.ix[:,2]
                
            fig = plt.figure()
            ax = fig.add_subplot(1,1,1)
            
            plt.plot(x,y7,'rD-',markersize = 6,markerfacecolor = 'none',linewidth = 0.8,label = p_data[0][-48:-4])
            plt.plot(x,y8,'bo-',markersize = 6,markerfacecolor = 'none',linewidth = 0.8,label = p_data[6][-48:-4])
            plt.plot(x,y9,'gs-',markersize = 6,markerfacecolor = 'none',linewidth = 0.8,label = p_data[3][-48:-4])
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
            plt.savefig('e:\py_data\ibutton\\'+z+'\\144cm\\'+u+'\\'+r'empty model-'+p_data[0][-18:-4]+'.png')
            plt.close()
            
        else:
        
            l_data = glob.glob(r'e:\py_data\ibutton\\'+z+'\\144cm\\'+u+r'\*.csv')
        
            data10 = pd.read_csv(l_data[0])
            data11 = pd.read_csv(l_data[3])

            x = np.arange(24)
            y10 = data10.ix[:,2]
            y11 = data11.ix[:,2]
        
            fig = plt.figure()
            ax = fig.add_subplot(1,1,1)
        
            plt.plot(x,y10,'rD-',markersize = 6,markerfacecolor = 'none',linewidth = 0.8,label = l_data[0][-47:-4])
            plt.plot(x,y11,'ko-',markersize = 6,markerfacecolor = 'none',linewidth = 0.8,label = l_data[6][-47:-4])
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
            plt.savefig('e:\py_data\ibutton\\'+z+'\\144cm\\'+u+'\\'+r'sand model-'+l_data[0][-18:-4]+'.png')#这样既可以生成图片，又可以保存对应的数据文件，也省下了后面进行再次分类
            plt.close()

#创建最终存放分析图的文件夹
pathadress = r'C:\Users\DELL\Desktop\处理数据\picture\ibutton\对比不同高宽比'
a = os.path.exists(pathadress)
if not a:
    os.mkdir(pathadress)
else:
    pass

#移动图片文件夹到指定文件夹
cfile = os.listdir('e:\py_data\ibutton')
for c in cfile:
    shutil.move('e:\py_data\ibutton\\'+c,r'C:\Users\DELL\Desktop\处理数据\picture\ibutton\对比不同高宽比')
                    

#此部分程序用于生成图片汇总文件夹，并在文件夹中按日期分类，同一天的图片放入同一文件夹，而上面的程序是放入了更细致的对应文件夹，为的是后面使用origin画图                    
'''
fname = os.listdir(r'C:\Users\DELL\Desktop\处理数据\picture\ibutton\对比不同高宽比')
for f in fname:
    dname = os.listdir(r'C:\Users\DELL\Desktop\处理数据\picture\ibutton\对比不同高宽比\\'+f)
    for d in dname:
        hname = os.listdir(r'C:\Users\DELL\Desktop\处理数据\picture\ibutton\对比不同高宽比'+'\\'+f+'\\'+d)
        for h in hname:
            sname = os.listdir(r'C:\Users\DELL\Desktop\处理数据\picture\ibutton\对比不同高宽比\\'+f+'\\'+d+'\\'+h)
            for s in sname:
                if s[-3:] == 'png':
                    shutil.copyfile(r'C:\Users\DELL\Desktop\处理数据\picture\ibutton\对比不同高宽比\\'+f+'\\'+d+'\\'+h+'\\'+s,r'e:\py_output\\'+s)
        

uname = os.listdir('e:\py_output')
for u in uname:
    texist = os.path.exists('e:\py_output\\'+u[-12:-4])
    if not texist:
        os.mkdir('e:\py_output\\'+u[-12:-4])
    else:
        pass

lname = os.listdir('e:\py_output')
for l in lname:
    if l[-3:] == 'png':
        shutil.move(r'e:\py_output\\'+l,r'e:\py_output\\'+l[-12:-4]+'\\'+l)

isExist = os.path.exists(r'C:\Users\DELL\Desktop\处理数据\picture\ibutton\对比不同高宽比\汇总')
if not isExist:
    os.mkdir(r'C:\Users\DELL\Desktop\处理数据\picture\ibutton\对比不同高宽比\汇总')
else:
    pass

bfile = os.listdir('e:\py_output')
for file in bfile:
    shutil.move(r'e:\py_output\\'+file,r'C:\Users\DELL\Desktop\处理数据\picture\ibutton\对比不同高宽比\汇总'+'\\'+file)                    
                    
'''                 
                    
                    