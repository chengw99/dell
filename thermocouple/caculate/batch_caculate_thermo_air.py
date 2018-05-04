# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 09:17:05 2018

@author: DELL
"""
#此程序用于筛选热电偶测量空气位置的温度数据
#对热电偶取10分钟平均
import os
import shutil
import pandas as pd
import numpy as np


#------------------------批量计算热电偶温度数据10min平均---------------------------#
f_file = os.listdir(r'e:\py_data\thermo') #这里需要往这个文件夹输入24小时数据
for f in f_file:
    csv_names = os.listdir(r'e:\py_data\thermo'+'\\'+f)
    os.chdir(r'e:\py_data\thermo\\'+f) #这个转换工作目录简直是太棒了！这样在后面读取数据的时候就可以直接输入文字名
    for file in csv_names:
        
        if file[-3:] == 'csv':
            #--------------------------选择进行分析的通道-------------------------#
            num = np.arange(8,12) #相应地修改通道数
            dict = {'8':'The air temperature at position 1','9':'The air temperature at position 2',
                    '10':'The air temperature at position 3','11':'The air temperature at position 4'} 
            # 1 : 10cm ; 2 : 30cm; 3: 60cm ; 4 : 144cm
            # 为了跟ibutton数据相匹配，找更多的共同点，简化共同特征，方便后面进行批量处理
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

#==============================================================================
#                     qExist = os.path.exists(r'e:\py_output\\'+dict[str(n)]+r'-10min_average')
#                     if not qExist:
#                         os.mkdir(r'e:\py_output\\'+dict[str(n)]+r'-10min_average')
#                     else:
#                         pass
#==============================================================================
                                
                    wExist = os.path.exists(r'e:\py_output\\'+dict[str(n)]+'\\'+file[-12:-4])
                    if not wExist:
                        os.makedirs(r'e:\py_output\\'+dict[str(n)]+'\\'+file[-12:-4])
                        result.to_csv(r'e:\py_output\\'+dict[str(n)]+'\\'+file[-12:-4]+'\\'+'thermo-'+dict[str(n)]+'-'+f+'-'+file,columns = columns)
                    else:
                        result.to_csv(r'e:\py_output\\'+dict[str(n)]+'\\'+file[-12:-4]+'\\'+'thermo-'+dict[str(n)]+'-'+f+'-'+file,columns = columns)
                
                except:
                    
                    print('Error read')
hExist = os.path.exists(r'C:\Users\DELL\Desktop\处理数据\分析数据\thermo\10min_average')
if not hExist:
    os.mkdir(r'C:\Users\DELL\Desktop\处理数据\分析数据\thermo\10min_average')
else:
    pass

g_file = os.listdir(r'e:\py_output')
for g in g_file:
    shutil.move(r'e:\py_output\\'+g,r'C:\Users\DELL\Desktop\处理数据\分析数据\thermo\10min_average\\'+g)                    
            