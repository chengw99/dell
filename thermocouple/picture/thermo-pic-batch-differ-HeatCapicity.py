# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 09:31:28 2018

@author: DELL
"""

import os
import glob
import shutil
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#将需要处理的文件移动到工作目录
fname = os.listdir(r'C:\Users\DELL\Desktop\处理数据\分析数据\thermo\10min_average')
for f in fname[4:8]: #不同模型的不同朝向只需要修改这个切片范围，选取相应的文件夹
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
#将文件移动到指定文件夹         
wfile = os.listdir(r'e:\py_data\thermo')
l = ['30cm','60cm','90cm','110cm']
p = ['HW1','HW2','HW3']
for w in wfile:
    for i in l:
        wExist = os.path.exists(r'e:\py_data\thermo\\'+w+'\\'+i)
        if not wExist:
            os.mkdir(r'e:\py_data\thermo\\'+w+'\\'+i)
        else:
            pass
        for j in p:
            rExist = os.path.exists(r'e:\py_data\thermo\\'+w+'\\'+i+'\\'+j)
            if not rExist:
                os.mkdir(r'e:\py_data\thermo\\'+w+'\\'+i+'\\'+j)
            else:
                pass
    tname = os.listdir(r'e:\py_data\thermo\\'+w)
    for t in tname:
        if t[-3:] == 'csv':
            for a in l[0:3]:
                for s in p:
                    if t[43:47] == a and t[50:53] == s:
                        shutil.move(r'e:\py_data\thermo\\'+w+'\\'+t,r'e:\py_data\thermo\\'+w+'\\'+a+'\\'+s+'\\'+t)
            for n in p:
                if t[43:48] == '110cm' and t[51:54] == n:
                    shutil.move(r'e:\py_data\thermo\\'+w+'\\'+t,r'e:\py_data\thermo\\'+w+'\\'+r'110cm'+'\\'+n+'\\'+t)

#画图
num = 0
mk=[]
pfile = os.listdir(r'e:\py_data\thermo')
for p in pfile:
    ufile = os.listdir(r'e:\py_data\thermo\\'+p)
    for u in ufile:
        sfile = os.listdir(r'e:\py_data\thermo\\'+p+'\\'+u)
        for s in sfile:
            cfile = os.listdir(r'e:\py_data\thermo\\'+p+'\\'+u+'\\'+s)
            if len(cfile) == 2:
                try:
                    e_file = glob.glob(r'e:\py_data\thermo\\'+p+'\\'+u+'\\'+s+'\\*.csv')
                    
                    if s == 'HW2':
                        data1 = pd.read_csv(e_file[1])
                        data2 = pd.read_csv(e_file[0])
                    else:
                        data1 = pd.read_csv(e_file[0])
                        data2 = pd.read_csv(e_file[1])
                    
                    x = np.arange(144)
                    y1 = data1.ix[:,2]
                    y2 = data2.ix[:,2]
                    
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
                    
                    fig = plt.figure(dpi = 160)
                    ax = fig.add_subplot(1,1,1)
                    
                    if u == '110cm':
                        if s == 'HW2':
                            plt.plot(x,y1,'D-',markersize = 0.5,linewidth = 1.,label = e_file[1][-63:-4])
                            plt.plot(x,y2,'x-',markersize = 0.5,linewidth = 1.,label = e_file[0][-62:-4])
                        else:
                            plt.plot(x,y1,'D-',markersize = 0.5,linewidth = 1.,label = e_file[0][-63:-4])
                            plt.plot(x,y2,'x-',markersize = 0.5,linewidth = 1.,label = e_file[1][-62:-4])
                    else:
                        if s == 'HW2':
                            plt.plot(x,y1,'D-',markersize = 0.5,linewidth = 1.,label = e_file[1][-62:-4])
                            plt.plot(x,y2,'x-',markersize = 0.5,linewidth = 1.,label = e_file[0][-61:-4])
                        else:
                            plt.plot(x,y1,'D-',markersize = 0.5,linewidth = 1.,label = e_file[0][-62:-4])
                            plt.plot(x,y2,'x-',markersize = 0.5,linewidth = 1.,label = e_file[1][-61:-4])
                    
                    plt.scatter(bb,p1,marker = 'D',s = 22)
                    plt.scatter(bb,p2,marker = 'x',s = 22)
                    
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
                    
                    #plt.show()
                    
                    if u == '110cm':
                        oExist = os.path.exists(r'e:\py_output\\'+p)
                        if not oExist:
                            os.mkdir(r'e:\py_output\\'+p)
                        else:
                            pass
                        if s == 'HW2':
                            
                            plt.savefig(r'e:\py_output\\'+p+'\\'+e_file[1][-79:-31]+r'-'+e_file[1][-28:-25]+r'-'+e_file[1][-12:-4]+r'.png')
                            plt.savefig(r'e:\py_data\thermo\\'+p+'\\'+u+'\\'+s+'\\'+e_file[1][-79:-31]+'-'+e_file[1][-28:-25]+'-'+e_file[1][-12:-4]+r'.png')
                        else:
                            plt.savefig(r'e:\py_output\\'+p+'\\'+e_file[0][-79:-31]+r'-'+e_file[0][-28:-25]+r'-'+e_file[0][-12:-4]+r'.png')
                            plt.savefig(r'e:\py_data\thermo\\'+p+'\\'+u+'\\'+s+'\\'+e_file[0][-79:-31]+'-'+e_file[0][-28:-25]+'-'+e_file[0][-12:-4]+r'.png')
                    else:
                        oExist = os.path.exists(r'e:\py_output\\'+p)
                        if not oExist:
                            os.mkdir(r'e:\py_output\\'+p)
                        else:
                            pass
                        if s == 'HW2':
                            plt.savefig(r'e:\py_output\\'+p+'\\'+e_file[1][-78:-31]+'-'+e_file[1][-28:-25]+'-'+e_file[1][-12:-4]+r'.png')
                            plt.savefig(r'e:\py_data\thermo\\'+p+'\\'+u+'\\'+s+'\\'+e_file[1][-78:-31]+'-'+e_file[1][-28:-25]+'-'+e_file[1][-12:-4]+r'.png')
                        else:
                            plt.savefig(r'e:\py_output\\'+p+'\\'+e_file[0][-78:-31]+'-'+e_file[0][-28:-25]+'-'+e_file[0][-12:-4]+r'.png')
                            plt.savefig(r'e:\py_data\thermo\\'+p+'\\'+u+'\\'+s+'\\'+e_file[0][-78:-31]+'-'+e_file[0][-28:-25]+'-'+e_file[0][-12:-4]+r'.png')
                    
                    plt.close()
                    
                    
                        

                            
                except:
                    pass
            else:
                oo = str(p) + '-' + str(u) +'-' + str(s)
                mk.append(oo)
                print('空文件夹:',oo)
                num = num + 1
print('空文件夹总数:',num)

#移动图片文件夹到指定文件夹
tExist = os.path.exists(r'C:\Users\DELL\Desktop\处理数据\picture\thermo\对比不同建筑热容')
if not tExist:
    os.mkdir(r'C:\Users\DELL\Desktop\处理数据\picture\thermo\对比不同建筑热容')
else:
    pass

lfile = os.listdir(r'C:\Users\DELL\Desktop\处理数据\分析数据\thermo\10min_average')
for l in lfile[4:8]:#
    zExist = os.path.exists(r'C:\Users\DELL\Desktop\处理数据\picture\thermo\对比不同建筑热容\\'+l[:24])
    if not zExist:
        os.mkdir(r'C:\Users\DELL\Desktop\处理数据\picture\thermo\对比不同建筑热容\\'+l[:24])
    else:
        pass
    mExist = os.path.exists(r'C:\Users\DELL\Desktop\处理数据\picture\thermo\对比不同建筑热容\\'+l[:24]+'\\'+r'汇总')
    if not mExist:
        os.mkdir(r'C:\Users\DELL\Desktop\处理数据\picture\thermo\对比不同建筑热容\\'+l[:24]+'\\'+r'汇总')
    else:
        pass
    
    j_file = os.listdir(r'e:\py_output')
    for file in j_file:
        shutil.move(r'e:\py_output\\'+file,r'C:\Users\DELL\Desktop\处理数据\picture\thermo\对比不同建筑热容\\'+l[:24]+'\\'+r'汇总'+'\\'+file)
    gfile = os.listdir(r'e:\py_data\thermo')
    for g in gfile:
        shutil.move(r'e:\py_data\thermo\\'+g,r'C:\Users\DELL\Desktop\处理数据\picture\thermo\对比不同建筑热容\\'+l[:24]+'\\'+g)
   
dt = '空文件夹总数:'+str(num)
mk.append(dt)
with open(r'C:\Users\DELL\Desktop\处理数据\picture\thermo\对比不同建筑热容'+'\\'+l[:24]+'\\'+r'empty folder.txt','w') as f:
    for i in mk:
        f.write(i)
        f.write('\n')   



