# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 09:35:04 2018

@author: DELL
"""

#批量作图-热电偶-10min平均温度数据-对比不同高宽比
#程序有待提升，需要修改两个地方的切片范围，才能处理类似的数据
import os
import glob
import shutil
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#将需要处理的文件移动到工作目录
fname = os.listdir(r'C:\Users\DELL\Desktop\处理数据\分析数据\thermo\10min_average')
for name in fname[12:16]:#
    try:
        shutil.copytree(r'C:\Users\DELL\Desktop\处理数据\分析数据\thermo\10min_average\\' + name,r'e:\py_data\thermo\\' + name)
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
#按照装沙模型和中空模型分类
pfile = os.listdir(r'e:\py_data\thermo')
l = ['empty model','sand model']
k = ['30cm','60cm','90cm','110cm']
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
        
        for j in k:
            bExist = os.path.exists(r'e:\py_data\thermo\\'+p+'\\'+i+'\\'+j)
            if not bExist:
                try:
                    os.mkdir(r'e:\py_data\thermo\\'+p+'\\'+i+'\\'+j)
                except:
                    pass
            else:
                pass
#将文件移动到指定文件夹
#先移动到装沙模型和中空模型
dfile = os.listdir(r'e:\py_data\thermo')
for d in dfile:
    ffile = os.listdir(r'e:\py_data\thermo\\'+d)
    for file in ffile:
        if file[-3:] == 'csv':
            if file[-23:-19] == 'sand':
                shutil.move(r'e:\py_data\thermo\\'+d+'\\'+file,r'e:\py_data\thermo\\'+d+'\\'+r'sand model'+'\\'+file)
            else:
                shutil.move(r'e:\py_data\thermo\\'+d+'\\'+file,r'e:\py_data\thermo\\'+d+'\\'+r'empty model'+'\\'+file)
#
q_file = os.listdir(r'e:\py_data\thermo')
for q in q_file:
    w_file = os.listdir(r'e:\py_data\thermo\\'+q)
    for w in w_file:
        r_file = os.listdir(r'e:\py_data\thermo\\'+q+'\\'+w)
        for r in r_file:
            if r[-3:] == 'csv':
                for i in k[0:3]:
                    if r[43:47] == i:
                        shutil.move(r'e:\py_data\thermo\\'+q+'\\'+w+'\\'+r,r'e:\py_data\thermo\\'+q+'\\'+w+'\\'+i+'\\'+r)
                if r[43:48] == k[-1]:
                    shutil.move(r'e:\py_data\thermo\\'+q+'\\'+w+'\\'+r,r'e:\py_data\thermo\\'+q+'\\'+w+'\\'+k[-1]+'\\'+r)
#画图
num = 0
k=[]
cfile = os.listdir(r'e:\py_data\thermo')
for c in cfile:
    bfile = os.listdir(r'e:\py_data\thermo\\'+c)
    for b in bfile:
        nfile = os.listdir(r'e:\py_data\thermo\\'+c+'\\'+b)
        for n in nfile:
            m = os.listdir(r'e:\py_data\thermo\\'+c+'\\'+b+'\\'+n)
            if len(m) == 3:
                try:
                    e_file = glob.glob(r'e:\py_data\thermo\\'+c+'\\'+b+'\\'+n+'\\*.csv')
                    
                    if b == 'empty model':
                        data1 = pd.read_csv(e_file[0])
                        data2 = pd.read_csv(e_file[2])
                        data3 = pd.read_csv(e_file[1])
                    else:
                        data1 = pd.read_csv(e_file[2])
                        data2 = pd.read_csv(e_file[0])
                        data3 = pd.read_csv(e_file[1])
                         #坐标轴数据
                    x = np.arange(144)
                    y1 = data1.ix[:,2]
                    y2 = data2.ix[:,2]
                    y3 = data3.ix[:,2]
                    #由于点太密集--需要散点图另外加标记，感觉会更好看
                    bb = np.array([0,12,24,36,48,60,72,84,96,108,120,132,143])
                    l1=[]
                    for i in bb:
                        result1 = data1.ix[i,2]
                        l1.append(result1)
                    p1 = np.array(l1)
                    l2=[]
                    for i in bb:
                        result2 = data2.ix[i,2]
                        l2.append(result2)
                    p2 = np.array(l2)
                    l3=[]
                    for i in bb:
                        result3 = data3.ix[i,2]
                        l3.append(result3)
                    p3 = np.array(l3)
                    
                    #设置图像属性
                    fig = plt.figure(dpi = 160)
                    ax = fig.add_subplot(1,1,1)
                    
                    if b == 'empty model':
                        if n == '110cm':
                            plt.plot(x,y1,'D-',markersize = 0.5,linewidth = 1.,label = e_file[0][62:121])
                            plt.plot(x,y2,'x-',markersize = 0.5,linewidth = 1.,label = e_file[2][62:121])
                            plt.plot(x,y3,'s-',markersize = 0.5,linewidth = 1.,label = e_file[1][62:121])
                        else:    
                            plt.plot(x,y1,'D-',markersize = 0.5,linewidth = 1.,label = e_file[0][61:119])
                            plt.plot(x,y2,'x-',markersize = 0.5,linewidth = 1.,label = e_file[2][61:119])
                            plt.plot(x,y3,'s-',markersize = 0.5,linewidth = 1.,label = e_file[1][61:119])
                    else:
                        if n == '110cm':
                            plt.plot(x,y1,'D-',markersize = 0.5,linewidth = 1.,label = e_file[2][61:119])
                            plt.plot(x,y2,'x-',markersize = 0.5,linewidth = 1.,label = e_file[0][61:119])
                            plt.plot(x,y3,'s-',markersize = 0.5,linewidth = 1.,label = e_file[1][61:119])
                        else:
                            plt.plot(x,y1,'D-',markersize = 0.5,linewidth = 1.,label = e_file[2][60:117])
                            plt.plot(x,y2,'x-',markersize = 0.5,linewidth = 1.,label = e_file[0][60:117])
                            plt.plot(x,y3,'s-',markersize = 0.5,linewidth = 1.,label = e_file[1][60:117])
                
                    plt.scatter(bb,p1,marker = 'D',s = 22)
                    plt.scatter(bb,p2,marker = 'x',s = 22)
                    plt.scatter(bb,p3,marker = 's',s = 22)
                    
                    plt.xlim(0,144) 
                    plt.ylim(22,46)
                    plt.xlabel('time',fontsize = 12)
                    plt.ylabel('T(℃)',rotation = 90,fontsize = 12)
                    plt.minorticks_on()
                    xticks = ax.set_xticks([0,24,48,72,96,120,143])  #此命令行可以确定x轴标签的位置
                    xlabels = ax.set_xticklabels(['0:00','4:00','8:00','12:00','16:00','20:00','24:00'])  #此命令行可以命名x坐标轴的标签内容
                    yticks = ax.set_yticks([22,26,30,34,38,42,46])
                    ylabels = ax.set_yticklabels(['22','26','30','34','38','42','46'])
                    
                    plt.legend(loc='best',fontsize = 10)
                    plt.grid(True,linestyle='--')
                    
                        
                    if b == 'empty model':
                        oExist = os.path.exists(r'e:\py_output\\'+c)
                        if not oExist:
                            os.mkdir(r'e:\py_output\\'+c)
                        else:
                            pass
                        if n == '110cm':    
                            plt.savefig('e:\py_output\\'+c+'\\'+e_file[0][46:94]+'-'+e_file[0][-24:-4]+'.png')
                            plt.savefig(r'e:\py_data\thermo\\'+c+'\\'+b+'\\'+n+'\\'+e_file[0][46:94]+'-'+e_file[0][-24:-4]+'.png')
                        else:
                            plt.savefig('e:\py_output\\'+c+'\\'+e_file[0][45:92]+'-'+e_file[0][-24:-4]+'.png')
                            plt.savefig(r'e:\py_data\thermo\\'+c+'\\'+b+'\\'+n+'\\'+e_file[0][45:92]+'-'+e_file[0][-24:-4]+'.png')
                    else:
                        oExist = os.path.exists(r'e:\py_output\\'+c)
                        if not oExist:
                            os.mkdir(r'e:\py_output\\'+c)
                        else:
                            pass
                        if n == '110cm':    
                            plt.savefig('e:\py_output\\'+c+'\\'+e_file[0][45:93]+'-'+e_file[0][-23:-4]+'.png')
                            plt.savefig(r'e:\py_data\thermo\\'+c+'\\'+b+'\\'+n+'\\'+e_file[0][45:93]+'-'+e_file[0][-23:-4]+'.png')
                        else:
                            plt.savefig('e:\py_output\\'+c+'\\'+e_file[0][44:91]+'-'+e_file[0][-23:-4]+'.png')
                            plt.savefig(r'e:\py_data\thermo\\'+c+'\\'+b+'\\'+n+'\\'+e_file[0][44:91]+'-'+e_file[0][-23:-4]+'.png')
                    plt.close()
                        
                            
                except:
                    pass                    
            else:
                kk = str(c)+'-'+str(b)+'-'+str(n)
                k.append(kk)
                print('空文件夹:',kk)
                num = num + 1
print('空文件夹总数:',num)
    
#移动图片文件夹到指定文件夹
tExist = os.path.exists(r'C:\Users\DELL\Desktop\处理数据\picture\thermo\对比不同高宽比')
if not tExist:
    os.mkdir(r'C:\Users\DELL\Desktop\处理数据\picture\thermo\对比不同高宽比')
else:
    pass

lfile = os.listdir(r'C:\Users\DELL\Desktop\处理数据\分析数据\thermo\10min_average')
for l in lfile[12:16]:#
    zExist = os.path.exists(r'C:\Users\DELL\Desktop\处理数据\picture\thermo\对比不同高宽比\\'+l[:24])
    if not zExist:
        os.mkdir(r'C:\Users\DELL\Desktop\处理数据\picture\thermo\对比不同高宽比\\'+l[:24])
    else:
        pass
    mExist = os.path.exists(r'C:\Users\DELL\Desktop\处理数据\picture\thermo\对比不同高宽比\\'+l[:24]+'\\'+r'汇总')
    if not mExist:
        os.mkdir(r'C:\Users\DELL\Desktop\处理数据\picture\thermo\对比不同高宽比\\'+l[:24]+'\\'+r'汇总')
    else:
        pass
    
    j_file = os.listdir(r'e:\py_output')
    for file in j_file:
        shutil.move(r'e:\py_output\\'+file,r'C:\Users\DELL\Desktop\处理数据\picture\thermo\对比不同高宽比\\'+l[:24]+'\\'+r'汇总'+'\\'+file)
    gfile = os.listdir(r'e:\py_data\thermo')
    for g in gfile:
        shutil.move(r'e:\py_data\thermo\\'+g,r'C:\Users\DELL\Desktop\处理数据\picture\thermo\对比不同高宽比\\'+l[:24]+'\\'+g)
   
dt = '空文件夹总数:'+str(num)
k.append(dt)
with open(r'C:\Users\DELL\Desktop\处理数据\picture\thermo\对比不同高宽比'+'\\'+l[:24]+'\\'+r'empty folder.txt','w') as f:
    for i in k:
        f.write(i)
        f.write('\n')   
    
    
    
    
    
    
    
    
    
    
    
    