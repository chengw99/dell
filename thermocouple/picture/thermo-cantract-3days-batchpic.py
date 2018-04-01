# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 11:11:30 2018

@author: DELL
"""

#此程序用于批量处理5月份的热电偶数据-三天连续的温度数据
import os
import glob
import shutil
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

l = ['30cm','60cm','90cm','110cm']
k = ['A','B','C','D','E','F']
h = ['Initial data','gather data','picture']
fpath = r'C:\Users\DELL\Desktop\处理数据\分析数据\thermo\10min_average' #原数据位置
ipath = r'e:\py_data\thermo' #数据处理的工作目录

#------------------------------------------对数据进行分类--------------------------------------------------------#
wname = os.listdir(fpath)
for w in wname[12:16]: # 选择哪个朝向的模型
    tname = os.listdir(fpath+'\\'+w)
    #准备创建文件夹的信息--控制连续日期的长度和范围
    m=[]
    for i in range(9): #根据实际日期所有的连续数据来定这个值
        m.append(int(i))
    b=[] #里面是分类好的需要数据的日期
    for j in m:
        q = []
        for g in tname[j+3:j+6]: #根据实际日期所有的连续数据来定这个值，这里代表数据都是连续三天的，并且以20170513开始
            q.append(g)
        b.append(q)
    #如果有其他的范围要求，需要修改的是上面的代码
    #-----------------------------创建文件夹------------------------------------#
    for file in b:
        #创建时间范围的文件夹
        qExist = os.path.exists(ipath+'\\'+file[0]+'-'+file[2])
        if not qExist:
            os.mkdir(ipath+'\\'+file[0]+'-'+file[2])
        else:
            pass
        #分三类文件夹：初始数据，整合数据，图片
        for f in h:
            tExist = os.path.exists(ipath+'\\'+file[0]+'-'+file[2]+'\\'+f)
            if not tExist:
                os.mkdir(ipath+'\\'+file[0]+'-'+file[2]+'\\'+f)
            else:
                pass
        #按高度和模型类型分类
        for i in l:
            wExist = os.path.exists(ipath+'\\'+file[0]+'-'+file[2]+'\\'+r'Initial data'+'\\'+i)
            if not wExist:
                os.mkdir(ipath+'\\'+file[0]+'-'+file[2]+'\\'+r'Initial data'+'\\'+i)
            else:
                pass
            for j in k:
                tExist = os.path.exists(ipath+'\\'+file[0]+'-'+file[2]+'\\'+r'Initial data'+'\\'+i+'\\'+j)
                if not tExist:
                    os.mkdir(ipath+'\\'+file[0]+'-'+file[2]+'\\'+r'Initial data'+'\\'+i+'\\'+j)
                else:
                    pass
        #--------------------将对应文件放入文件夹中-------------------------------#
        #这里记得需要复制文件，不能是移动文件，因为是直接从原数据处进行操作
        qname = os.listdir(ipath)
        for c in qname:
            if file[0] == c[0:8]:
                for dfile in file:
                    pname = os.listdir(fpath+'\\'+w+'\\'+dfile)
                    for p in pname:
                        for i in l[0:3]:
                            for j in k:
                                if p[43:47] == i:
                                    if p[48] == j:
                                        try:
                                            shutil.copyfile(fpath+'\\'+w+'\\'+dfile+'\\'+p,
                                                            ipath+'\\'+file[0]+'-'+file[2]+'\\'+r'Initial data'+'\\'+i+'\\'+j+'\\'+p)
                                        except:
                                            pass
                        for j in k:
                            if p[43:48] == '110cm':
                                if p[49] == j:
                                    try:
                                        shutil.copyfile(fpath+'\\'+w+'\\'+dfile+'\\'+p,
                                                        ipath+'\\'+file[0]+'-'+file[2]+'\\'+r'Initial data'+'\\'+r'110cm'+'\\'+j+'\\'+p)
                                    except:
                                        pass
            
#-------------------------------------------------批量画图---------------------------------------------------------#
total = os.listdir(ipath)
for t in total:
    qtotal = os.listdir(ipath+'\\'+t+'\\'+h[0])
    for q in qtotal:
        wtotal = os.listdir(ipath+'\\'+t+'\\'+h[0]+'\\'+q)
        for w in wtotal:
            rtotal = glob.glob(ipath+'\\'+t+'\\'+h[0]+'\\'+q+'\\'+w+'\\'+'*.csv')
            
            data1 = pd.read_csv(rtotal[0])
            data2 = pd.read_csv(rtotal[1])
            data3 = pd.read_csv(rtotal[2])

            y1 = data1.iloc[:,2]
            y2 = data2.iloc[:,2]
            y3 = data3.iloc[:,2]
            
            y = pd.concat([y1,y2,y3])
            x = np.arange(432)
            
            fig = plt.figure()
            ax = fig.add_subplot(1,1,1)
            
            plt.plot(x,y,'rD-',markersize = 0.5,linewidth = 1,label = 'Diurnal Cycle Temperature')
            
            plt.xlim(0,432)
            plt.ylim(22,46)
            plt.xlabel('time',fontsize = 12)
            plt.ylabel('T(℃)',rotation = 90,fontsize = 12)
            plt.minorticks_on()
            xticks = ax.set_xticks([0,48,96,144,
                                    192,240,288,
                                    336,384,431])
            xlabels = ax.set_xticklabels(['0:00','8:00','16:00',
                                          '0:00','8:00','16:00',
                                          '0:00','8:00','16:00','24:00'])
            yticks = ax.set_yticks([22,26,30,34,38,42,46])
            ylabels = ax.set_yticklabels(['22','26','30','34','38','42','46'])
            plt.legend(loc='best',fontsize=12)
            plt.grid(True,linestyle='--')
            
            plt.savefig(ipath+'\\'+t+'\\'+h[2]+'\\'+str(w)+'-'+str(q)+'.png')
            plt.close()
            
            time = []
            for k in range(3):
                for i in range(24):
                    for j in np.linspace(0,60,num = 6,endpoint = False):
                        if j == 0:
                            time.append(str(int(i))+':0'+str(int(j)))
                        else:
                            time.append(str(int(i))+':'+str(int(j)))
        
            result = pd.DataFrame({'Temperature':y,'time':time})
            columns = ['time','Temperature']
            
            result.to_csv(ipath+'\\'+t+'\\'+h[1]+'\\'+str(w)+'-'+str(q)+'.csv',columns = columns)

#------------------------------移动最终文件夹到指定目录---------------------------#
mExist = os.path.exists(r'C:\Users\DELL\Desktop\处理数据\picture\thermo\日循环')
if not mExist:
    os.mkdir(r'C:\Users\DELL\Desktop\处理数据\picture\thermo\日循环')
else:
    pass

jfile = os.listdir(ipath)
for j in jfile:
    shutil.move(ipath+'\\'+j,r'C:\Users\DELL\Desktop\处理数据\picture\thermo\日循环'+'\\'+j)




            