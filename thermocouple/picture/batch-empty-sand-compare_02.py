# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 19:14:18 2018

@author: DELL
"""

#此程序用于批量处理中空模型和装沙模型温度差的24小时变化图
#程序有个缺点，删不了一个空文件夹，不知道为什么。。。
import os
import shutil 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

l = ['30cm','60cm','90cm','110cm']
k = ['HW1','HW2','HW3']
h = ['data','picture']
fpath = r'C:\Users\DELL\Desktop\处理数据\分析数据\thermo\10min_average' #原数据位置
ipath = r'e:\py_data\thermo' #进行数据处理的位置
opath = r'e:\py_output'

#------------------------------准备数据-----------------------------------------#
#复制数据到工作目录
qfile = os.listdir(fpath)
for q in qfile[4:8]: #修改这个切片范围可以获得不同的朝向
    try:
        shutil.copytree(fpath+'\\'+q,ipath+'\\'+q)
    except:
        pass
#将文件分类，不同高度，不同高宽比，每个高宽比文件夹里会有两个文件   
wfile = os.listdir(ipath)
for w in wfile: #w是朝向和高度文件夹
    tfile = os.listdir(ipath+'\\'+w)
    for t in tfile: #t是年月日文件夹       
        for i in k: #k是不同高宽比列表
            qExist = os.path.exists(ipath+'\\'+w+'\\'+t+'\\'+i)
            if not qExist:
                os.makedirs(ipath+'\\'+w+'\\'+t+'\\'+i)
            else:
                pass
        ufile = os.listdir(ipath+'\\'+w+'\\'+t)
        for u in ufile: #u是csv文件
            if u[-3:] == 'csv':
                for z in l[0:3]: #判断是否为30cm,60cm,90cm
                    if u[43:47] == z:           
                        for j in k:
                            if u[50:53] == j:
                                try:
                                    shutil.move(ipath+'\\'+w+'\\'+t+'\\'+u,ipath+'\\'+w+'\\'+t+'\\'+j+'\\'+u)
                                except:
                                    pass
                if u[43:48] == '110cm':
                    for p in k:
                        if u[51:54] == p:
                            try:
                                shutil.move(ipath+'\\'+w+'\\'+t+'\\'+u,ipath+'\\'+w+'\\'+t+'\\'+p+'\\'+u)
                            except:
                                pass
                    
                     
#-----------------------------批量画图-----------------------------------------#
pfile = os.listdir(ipath)
for p in pfile: # 不同朝向、不同高度的文件夹
    sfile = os.listdir(ipath+'\\'+p)
    for s in sfile: # 不同日期文件夹
        dfile = os.listdir(ipath+'\\'+p+'\\'+s)
        for d in dfile: #不同高宽比文件夹
            file = os.listdir(ipath+'\\'+p+'\\'+s+'\\'+d)
            try:
                if len(file) == 2:
                
                    os.chdir(ipath+'\\'+p+'\\'+s+'\\'+d)
                    gfile = os.listdir(ipath+'\\'+p+'\\'+s+'\\'+d)
                    
                    if d == 'HW2':
                  
                        empty = pd.read_csv(gfile[1])
                        sand  = pd.read_csv(gfile[0])
                    
                    else:
                        empty = pd.read_csv(gfile[0])
                        sand  = pd.read_csv(gfile[1])
                    
                    y1 = empty.loc[:,'Temperature']
                    y2 = sand.loc[:,'Temperature']
                    
                    y = y1 - y2 # empty - sand
                    
                    x = np.arange(144)
                    z = x * 0
                    
                    fig = plt.figure() 
                    ax  = fig.add_subplot(1,1,1)
                
                    if p[27:32] == '110cm':
                    
                        plt.plot(x,y,'rD-',markersize = 1,linewidth = 1.5,label = gfile[0][43:48]+'-'+gfile[0][51:54]+'-diffT-empty-sand'+gfile[0][-12:-4])
                   
                    else:
                    
                        plt.plot(x,y,'rD-',markersize = 1,linewidth = 1.5,label = gfile[0][43:47]+'-'+gfile[0][50:53]+'-diffT-empty-sand'+gfile[0][-12:-4])
                
                    plt.plot(x,z,'k--',linewidth = 1.1)
                    plt.xlim(0,143)
                    plt.ylim(-6,6)
                    plt.xlabel('time',fontsize = 12)
                    plt.ylabel('T(℃)',rotation = 90,fontsize = 12)
                    plt.minorticks_on()
                    xticks = ax.set_xticks([0,24,48,72,96,120,143])  #此命令行可以确定x轴标签的位置
                    xlabels = ax.set_xticklabels(['0:00','4:00','8:00','12:00','16:00','20:00','24:00'])  #此命令行可以命名x坐标轴的标签内容
                    yticks = ax.set_yticks([-6,-4,-2,0,2,4,6])
                    ylabels = ax.set_yticklabels(['-6','-4','-2','0','2','4','6'])
                    #设置图注
                    plt.legend(loc='best',fontsize = 13)
                    plt.grid(True,linestyle='--')
                
                    for n in h:
                        if p[27:32] == '110cm':
                            tExist = os.path.exists(opath+'\\'+p[27:32]+'\\'+n)
                            if not tExist:
                                os.makedirs(opath+'\\'+p[27:32]+'\\'+n)
                            else:
                                pass
                        else:
                        
                            tExist = os.path.exists(opath+'\\'+p[27:31]+'\\'+n)
                            if not tExist:
                                os.makedirs(opath+'\\'+p[27:31]+'\\'+n)
                            else:
                                pass
                
                    time = []
                    for ii in range(24):
                        for jj in np.linspace(0,60,num = 6,endpoint = False):
                            if jj == 0:
                                time.append(str(int(ii))+':0'+str(int(jj)))
                            else:
                                time.append(str(int(ii))+':'+str(int(jj)))
        
                    result = pd.DataFrame({'Temperature':y,'time':time})
                    columns = ['time','Temperature']     
                    #生成图片
                    if p[27:32] == '110cm':
                        plt.savefig(opath+'\\'+p[27:32]+'\\'+'picture'+'\\'+gfile[0][43:48]+'-'+gfile[0][51:54]+'-'+gfile[0][-12:-4]+'.png')
                        plt.savefig(ipath+'\\'+p+'\\'+s+'\\'+d+'\\'+gfile[0][43:48]+'-'+gfile[0][51:54]+'-'+gfile[0][-12:-4]+'.png')
                        result.to_csv(opath+'\\'+p[27:32]+'\\'+'data'+'\\'+gfile[0][43:48]+'-'+gfile[0][51:54]+'-'+gfile[0][-12:-4]+'.csv',columns = columns)
                    else:
                        plt.savefig(opath+'\\'+p[27:31]+'\\'+'picture'+'\\'+gfile[0][43:47]+'-'+gfile[0][50:53]+'-'+gfile[0][-12:-4]+'.png')
                        plt.savefig(ipath+'\\'+p+'\\'+s+'\\'+d+'\\'+gfile[0][43:47]+'-'+gfile[0][50:53]+'-'+gfile[0][-12:-4]+'.png')
                        result.to_csv(opath+'\\'+p[27:31]+'\\'+'data'+'\\'+gfile[0][43:47]+'-'+gfile[0][50:53]+'-'+gfile[0][-12:-4]+'.csv',columns = columns)

                        
                    plt.close()
                else:
                    shutil.rmtree(ipath+'\\'+p+'\\'+s+'\\'+d) #删除缺失文件夹
            except:
                pass
              
#-------------------移动到指定位置----------------------------------------------#

lpath = r'C:\Users\DELL\Desktop\处理数据\picture\thermo\中空-装沙'
bExist = os.path.exists(lpath+'\\'+qfile[4][:24]+'-'+r'汇总') #数字12可以修改，表示不同的朝向
if not bExist:
    os.makedirs(lpath+'\\'+qfile[4][:24]+'-'+r'汇总')
else:
    pass
kfile = os.listdir(ipath)
for hb in kfile:
    try:
        shutil.move(ipath+'\\'+hb,lpath+'\\'+hb)
    except:
        pass
mfile = os.listdir(opath)
for o in mfile:
    try:
        shutil.move(opath+'\\'+o,lpath+'\\'+qfile[4][:24]+'-'+r'汇总'+'\\'+o)
    except:
        pass





