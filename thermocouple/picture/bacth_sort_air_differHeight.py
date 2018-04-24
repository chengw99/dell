# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 09:59:41 2018

@author: DELL
"""
#想想还是顺便把图也画出来好了
#此程序用于分类热电偶空气温度 - 同一街谷不同高度
#准备从生成csv文件的时候就进行分类 -- 力荐这种方式！！！就再也不用重新进行数据分类了

import os
import shutil
import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

spath = r'C:\Users\DELL\Desktop\处理数据\按日期排序\thermo'
ipath = r'e:\py_data\thermo'
opath = r'e:\py_output'

#-----------------------------准备数据-----------------------------------------#
#复制热电偶不同日期的数据到工作目录
qfile = os.listdir(spath) ###
for q in qfile:
    try:
        shutil.copytree(spath+'\\'+q,ipath+'\\'+q)
    except:
        pass
#创建存放数据文件夹
m = ['data','total picture']
for mm in m:
    qExist = os.path.exists(opath+'\\'+mm)
    if not qExist:
        os.mkdir(opath+'\\'+mm)
    else:
        pass
#------------------------批量计算热电偶温度数据10min平均---------------------------#
f_file = os.listdir(ipath) 
for f in f_file:
    csv_names = glob.glob(ipath+'\\'+f+'\\'+'*.csv') ###
    
    for file in csv_names:
        
        if file[-3:] == 'csv':
            #--------------------------选择进行分析的通道-------------------------#
            num = np.arange(8,12) #相应地修改通道数
            dict = {'8':'The air temperature at position 1','9':'The air temperature at position 2',
                    '10':'The air temperature at position 3','11':'The air temperature at position 4'} 
            # 1 : 10cm ; 2 : 30cm; 3: 60cm ; 4 : 144cm
            # 为了跟ibutton数据相匹配，找更多的共同点，简化共同特征，方便后面进行批量处理
            # 画图的时候也提倡这样进行分类数据，按照数字分类，赋予不同的意义，这样排序是确定的，图例的时候再加上去就行
            for n in num:
                
                try:
                    
                
                    a = pd.read_csv(file)
                    data = a.ix[:,n] #循环处理对应的通道数
            
                    tem = []
                    for k in range(144):
                        data_mean = sum(data[10*k:10*k+10])/10.
                        tem.append(data_mean)
                    
                    time = []
                    for i in range(24):
                        for j in np.linspace(0,60,num = 6,endpoint = False):
                            if j == 0:
                                time.append(str(int(i))+':0'+str(int(j)))
                            else:
                                time.append(str(int(i))+':'+str(int(j)))
                
                    result = pd.DataFrame({'time':time,'Temperature':tem})
                    columns = ['time','Temperature']
                    
                    wExist = os.path.exists(opath+'\\'+r'data'+'\\'+file[-12:-4]+'\\'+f)
                    if not wExist:
                        os.makedirs(opath+'\\'+r'data'+'\\'+file[-12:-4]+'\\'+f)
                        result.to_csv(opath+'\\'+r'data'+'\\'+file[-12:-4]+'\\'+f+'\\'+f[0]+dict[str(n)][-1]+'-'+file[-12:],columns = columns)
                        result.to_csv(opath+'\\'+r'data'+'\\'+file[-12:-4]+'\\'+f+'\\'+f[0]+dict[str(n)][-1]+'-'+file[-12:],columns = columns)
                    else:
                        result.to_csv(opath+'\\'+r'data'+'\\'+file[-12:-4]+'\\'+f+'\\'+f[0]+dict[str(n)][-1]+'-'+file[-12:],columns = columns)
                                           
                except:
                    
                    print('Erro read')
#------------------------画图--------------------------------------------------#                
wfile = os.listdir(opath+'\\'+r'data')
for w in wfile:
    tfile = os.listdir(opath+'\\'+r'data'+'\\'+w)
    for t in tfile:
        u = glob.glob(opath+'\\'+r'data'+'\\'+w+'\\'+t+'\\'+'*.csv')
        
        if len(u) == 4:
            data1 = pd.read_csv(u[0]) # 1-10cm
            data2 = pd.read_csv(u[1]) # 2-30cm
            data3 = pd.read_csv(u[2]) # 3-60cm
            data4 = pd.read_csv(u[3]) # 4-144cm
            
            x = np.arange(144)
            y1 = data1.ix[:,'Temperature'] 
            y2 = data2.ix[:,'Temperature']
            y3 = data3.ix[:,'Temperature']
            y4 = data4.ix[:,'Temperature']
                    
            fig = plt.figure(figsize=(12,9),dpi=160)
            ax = fig.add_subplot(1,1,1)
                    
            plt.plot(x,y1,linestyle='-',marker='D',markersize=5,markerfacecolor='none',markevery=6,linewidth=0.8,label='10cm'+'-'+w)
            plt.plot(x,y2,linestyle='-',marker='o',markersize=5,markerfacecolor='none',markevery=6,linewidth=0.8,label='30cm'+'-'+w)
            plt.plot(x,y3,linestyle='-',marker='s',markersize=5,markerfacecolor='none',markevery=6,linewidth=0.8,label='60cm'+'-'+w)
            plt.plot(x,y4,linestyle='-',marker='d',markersize=5,markerfacecolor='none',markevery=6,linewidth=0.8,label='144cm'+'-'+w)
            
            plt.xlim(0,144)
            plt.ylim(22,42)
            plt.xlabel('time',fontsize = 12)
            plt.ylabel('Temperature(℃)',rotation = 90,fontsize = 12)
            plt.minorticks_on()
            xticks = ax.set_xticks([0,24,48,72,96,120,144])  #此命令行可以确定x轴标签的位置
            xlabels = ax.set_xticklabels(['0:00','4:00','8:00','12:00','16:00','20:00','24:00'])  #此命令行可以命名x坐标轴的标签内容
            yticks = ax.set_yticks([22,26,30,34,38,42])
            ylabels = ax.set_yticklabels(['22','26','30','34','38','42'])
            plt.legend(loc='best',fontsize = 14,markerscale = 1) #这里可以修改legend中marker的大小
            plt.title('The air temperature',fontsize=12)
            plt.grid(True,linestyle='--')
        
            plt.savefig(opath+'\\'+r'total picture'+'\\'+'thermo-different height-'+t+'-'+w+'.png')
            plt.savefig(opath+'\\'+r'data'+'\\'+w+'\\'+t+'\\'+'thermo-different height-'+t+'-'+w+'.png')
            plt.close()
#--------------------------移动结果到最终文件夹-----------------------------------#                
kpath = r'C:\Users\DELL\Desktop\处理数据\picture\thermo\空气-对比不同高度'
gExist = os.path.exists(kpath)
if not gExist:
    os.makedirs(kpath)
else:
    pass

aafile = os.listdir(opath)
for aa in aafile:
    shutil.move(opath+'\\'+aa,kpath+'\\'+aa)
#清除输入数据
vfile = os.listdir(ipath)
for v in vfile:
    try:
        shutil.rmtree(ipath+'\\'+v)
    except:
        pass
                  