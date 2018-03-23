# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 14:39:51 2018

@author: DELL
"""

#此程序用于批量作图-热电偶-10min平均的数据-对比不同高度-north model-facing north
import os
import glob
import shutil
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#-------------------------------获取数据---------------------------------------#
#将需要处理的文件移动到工作目录
fname = os.listdir(r'C:\Users\DELL\Desktop\处理数据\分析数据\thermo\10min_average')
for f in fname[0:4]:
    try:
        shutil.copytree(r'C:\Users\DELL\Desktop\处理数据\分析数据\thermo\10min_average\\' + f,r'e:\py_data\thermo\\' + f) #这里如果用copyfile的话只能复制文件而不是文件夹，文件夹只能用shutil.copytree或者shutil.move
    except:
        pass
#将csv文件遍历出来   
qfile = os.listdir(r'e:\py_data\thermo')
for q in qfile:
    wfile = os.listdir(r'e:\py_data\thermo\\'+q)
    for w in wfile:
        ufile = os.listdir(r'e:\py_data\thermo\\'+q+'\\'+w)
        for u in ufile:
            if u[-3:] == 'csv':
                
                try:
                    shutil.move(r'e:\py_data\thermo\\'+q+'\\'+w+'\\'+u,r'e:\py_data\thermo\\'+u)
                    
                except:
                    pass                        
    shutil.rmtree(r'e:\py_data\thermo\\'+q)
#------------------------------分类存放数据-------------------------------------#
#按照日期进行分类
tfile = os.listdir(r'e:\py_data\thermo')
for t in tfile:
    if t[-3:] == 'csv':
        qExist = os.path.exists(r'e:\py_data\thermo\\'+t[-12:-4])
        if not qExist:
            try:
                os.mkdir(r'e:\py_data\thermo\\'+t[-12:-4])
                shutil.move(r'e:\py_data\thermo\\'+t,r'e:\py_data\thermo\\'+t[-12:-4]+'\\'+t)
            except:
                pass
        else:
            try:
                shutil.move(r'e:\py_data\thermo\\'+t,r'e:\py_data\thermo\\'+t[-12:-4]+'\\'+t)
            except:
                pass
#创建ABCDEF文件夹
pfile = os.listdir(r'e:\py_data\thermo')
l = ['A','B','C','D','E','F']
for p in pfile:
    for i in l:
        aExist = os.path.exists(r'e:\py_data\thermo\\'+p+'\\'+i)
        if not aExist:
            try:
                os.mkdir(r'e:\py_data\thermo\\'+p+'\\'+i)
            except:
                pass
        else:
            pass
#将对应的文件放入对应的文件夹中
gfile = os.listdir(r'e:\py_data\thermo')
for g in gfile:
    hfile = os.listdir(r'e:\py_data\thermo\\'+g)
    for h in hfile:
        if h[-3:] == 'csv':
            for j in l:
                if h[-29] == j:
                    shutil.move(r'e:\py_data\thermo\\'+g+'\\'+h,r'e:\py_data\thermo\\'+g+'\\'+j+'\\'+h)
                elif h[-30] == j:
                    shutil.move(r'e:\py_data\thermo\\'+g+'\\'+h,r'e:\py_data\thermo\\'+g+'\\'+j+'\\'+h)
                else:
                    pass
#-------------------------------画图-------------------------------------------#
num = 0
dfile = os.listdir(r'e:\py_data\thermo')
for d in dfile:
    cfile = os.listdir(r'e:\py_data\thermo\\'+d)
    for c in cfile:
        v = os.listdir(r'e:\py_data\thermo\\'+d+'\\'+c)
        
        if len(v) != 0:
            try:
                e_file = glob.glob(r'e:\py_data\thermo\\'+d+'\\'+c+'\\*.csv')
                #读取数据    
                data1 = pd.read_csv(e_file[1])
                data2 = pd.read_csv(e_file[2]) 
                data3 = pd.read_csv(e_file[3])
                data4 = pd.read_csv(e_file[0])
                #坐标轴数据
                x = np.arange(144)
                y1 = data1.ix[:,2]
                y2 = data2.ix[:,2]
                y3 = data3.ix[:,2]
                y4 = data4.ix[:,2]
                #由于点太密集--需要散点图另外加标记，感觉会更好看
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
                #设置图像属性
                fig = plt.figure(dpi = 160)
                ax = fig.add_subplot(1,1,1)
                
                if e_file[0][-24:-19] == 'empty':
                    plt.plot(x,y1,'x-',markersize = 0.5,linewidth = 1.,label = e_file[1][46:104])
                    plt.plot(x,y2,'D-',markersize = 0.5,linewidth = 1.,label = e_file[2][46:104])
                    plt.plot(x,y3,'<-',markersize = 0.5,linewidth = 1.,label = e_file[3][46:104])
                    plt.plot(x,y4,'s-',markersize = 0.5,linewidth = 1.,label = e_file[0][46:105])
                elif e_file[0][-23:-19] == 'sand':
                    plt.plot(x,y1,'x-',markersize = 0.5,linewidth = 1.,label = e_file[1][46:103])
                    plt.plot(x,y2,'D-',markersize = 0.5,linewidth = 1.,label = e_file[2][46:103])
                    plt.plot(x,y3,'<-',markersize = 0.5,linewidth = 1.,label = e_file[3][46:103])
                    plt.plot(x,y4,'s-',markersize = 0.5,linewidth = 1.,label = e_file[0][46:104])
                else:
                    pass
                    
                plt.scatter(b,p1,marker = 'x',s = 22)
                plt.scatter(b,p2,marker = 'D',s = 22)
                plt.scatter(b,p3,marker = '<',s = 22)
                plt.scatter(b,p4,marker = 's',s = 22)
   
                #设置坐标刻度和名称
                plt.xlim(0,144) 
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
                
                if e_file[0][-24:-19] == 'empty':
                    oExist = os.path.exists(r'e:\py_output\\'+d)
                    if not oExist:
                        os.mkdir(r'e:\py_output\\'+d)
                    else:
                        pass
                    plt.savefig('e:\py_output\\'+d+'\\'+e_file[0][30:70]+'-'+e_file[0][-30:-4]+'.png')
                    plt.savefig(r'e:\py_data\thermo\\'+d+'\\'+c+'\\'+e_file[0][30:70]+'-'+e_file[0][-30:-4]+'.png')
                elif e_file[0][-23:-19] == 'sand':
                    pExist = os.path.exists(r'e:\py_output\\'+d)
                    if not pExist:
                        os.mkdir(r'e:\py_output\\'+d)
                    else:
                        pass
                    plt.savefig('e:\py_output\\'+d+'\\'+e_file[0][30:70]+'-'+e_file[0][-29:-4]+'.png')
                    plt.savefig(r'e:\py_data\thermo\\'+d+'\\'+c+'\\'+e_file[0][30:70]+'-'+e_file[0][-29:-4]+'.png')
                else:
                    pass
                plt.close()
                    
            except:
                pass
        else:
            print('空文件夹:',str(d)+'-'+str(c))
            num = num + 1
print('空文件夹总数:',num)
#移动图片文件夹到指定文件夹
tExist = os.path.exists(r'C:\Users\DELL\Desktop\处理数据\picture\thermo\对比不同高度')
if not tExist:
    os.mkdir(r'C:\Users\DELL\Desktop\处理数据\picture\thermo\对比不同高度')
else:
    pass

b_file = os.listdir(r'e:\py_data\thermo')
for b in b_file:
    shutil.move(r'e:\py_data\thermo\\'+b,r'C:\Users\DELL\Desktop\处理数据\picture\thermo\对比不同高度'+'\\'+b)
    
mExist = os.path.exists(r'C:\Users\DELL\Desktop\处理数据\picture\thermo\对比不同高度\汇总')
if not mExist:
    os.mkdir(r'C:\Users\DELL\Desktop\处理数据\picture\thermo\对比不同高度\汇总')
else:
    pass

m_file = os.listdir(r'e:\py_output')
for m in m_file:
    shutil.move(r'e:\py_output\\'+m,r'C:\Users\DELL\Desktop\处理数据\picture\thermo\对比不同高度\汇总'+'\\'+m)

