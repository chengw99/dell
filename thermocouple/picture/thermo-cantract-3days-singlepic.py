# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 14:32:13 2018

@author: DELL
"""

import os
import glob
import shutil
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#此程序用于做批量画日循环图片
#但这个程序只能画其中连续三天的
#将需要处理的文件移动到工作目录
fname = os.listdir(r'C:\Users\DELL\Desktop\处理数据\分析数据\thermo\10min_average')
for f in fname[12:16]: #不同模型的不同朝向只需要修改这个切片范围，选取相应的文件夹
    try:
        shutil.copytree(r'C:\Users\DELL\Desktop\处理数据\分析数据\thermo\10min_average\\' + f,r'e:\py_data\thermo\\' + f) #这里如果用copyfile的话只能复制文件而不是文件夹，文件夹只能用shutil.copytree或者shutil.move
    except:
        pass

l = ['30cm','60cm','90cm','110cm']
k = ['A','B','C','D','E','F']
for i in l:
    qExist = os.path.exists(r'e:\py_output\\'+i)    
    if not qExist:
        os.mkdir(r'e:\py_output\\'+i)
    else:
        pass
    for j in k:
        wExist = os.path.exists(r'e:\py_output\\'+i+'\\'+j)
        if not wExist:
            os.mkdir(r'e:\py_output\\'+i+'\\'+j)
        else:
            pass

wname = os.listdir(r'e:\py_data\thermo')
for w in wname:
    tname = os.listdir(r'e:\py_data\thermo\\'+w)
    for t in tname[3:6]:
        uname = os.listdir(r'e:\py_data\thermo\\'+w+'\\'+t)
        for u in uname:
            for i in l[0:3]:
                for j in k:
                    if u[43:47] == i:
                        if u[48] == j:
                            try:
                                shutil.copyfile(r'e:\py_data\thermo\\'+w+'\\'+t+'\\'+u,r'e:\py_output\\'+i+'\\'+j+'\\'+u)
                            except:
                                pass
            
            for j in k:
                if u[43:48] == '110cm':
                    if u[49] == j:
                        try:
                            shutil.copyfile(r'e:\py_data\thermo\\'+w+'\\'+t+'\\'+u,r'e:\py_output\110cm'+'\\'+j+'\\'+u)
                        except:
                            pass


qfile = os.listdir(r'e:\py_output')
for q in qfile:
    wfile = os.listdir(r'e:\py_output'+'\\'+q)
    for w in wfile:
        efile = glob.glob(r'e:\py_output'+'\\'+q+'\\'+w+'\\'+'*.csv')
        
        data1 = pd.read_csv(efile[0])
        data2 = pd.read_csv(efile[1])
        data3 = pd.read_csv(efile[2])
        
        y1 = data1.iloc[:,2]
        y2 = data2.iloc[:,2]
        y3 = data3.iloc[:,2]
        
        y = pd.concat([y1,y2,y3])
        
        x = np.arange(432)
        fig = plt.figure(dpi=160)
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
        zExist = os.path.exists(r'e:\py_output\\'+efile[0][-12:-4]+'-'+efile[2][-12:-4])
        if not zExist:
            os.mkdir(r'e:\py_output\\'+efile[0][-12:-4]+'-'+efile[2][-12:-4])
        else:
            pass
        
        cExist = os.path.exists(r'e:\py_output\\'+efile[0][-12:-4]+'-'+efile[2][-12:-4]+'\\'+'picture')
        if not cExist:
            os.mkdir(r'e:\py_output\\'+efile[0][-12:-4]+'-'+efile[2][-12:-4]+'\\'+'picture')
        else:
            pass
        
        bExist = os.path.exists(r'e:\py_output\\'+efile[0][-12:-4]+'-'+efile[2][-12:-4]+'\\'+'Initial data')
        if not bExist:
            os.mkdir(r'e:\py_output\\'+efile[0][-12:-4]+'-'+efile[2][-12:-4]+'\\'+'Initial data')
        else:
            pass
        plt.savefig(r'e:\py_output\\'+efile[0][-12:-4]+'-'+efile[2][-12:-4]+'\\'+'picture'+'\\'+str(q)+'-'+str(w)+'.png')
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
        
        vExist = os.path.exists(r'e:\py_output\\'+efile[0][-12:-4]+'-'+efile[2][-12:-4]+'\\'+'gather data')
        if not vExist:
            os.mkdir(r'e:\py_output\\'+efile[0][-12:-4]+'-'+efile[2][-12:-4]+'\\'+'gather data')
        else:
            pass
        result.to_csv(r'e:\py_output'+'\\'+efile[0][-12:-4]+'-'+efile[2][-12:-4]+'\\'
                      +'gather data'+'\\'+str(q)+'-'+str(w)+'.csv',columns=columns)
        
        
bExist = os.path.exists(r'C:\Users\DELL\Desktop\处理数据\picture\thermo\日循环')
if not bExist:
    os.mkdir(r'C:\Users\DELL\Desktop\处理数据\picture\thermo\日循环')
else:
    pass

            
        
                    
                
                    
            