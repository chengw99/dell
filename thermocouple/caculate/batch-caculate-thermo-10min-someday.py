# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 10:52:32 2018

@author: DELL
"""

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
            num = np.arange(23,43) #相应地修改通道数
            #这个是今天最好的思路！
            #添加字典后，后面生成文件夹或者文件的时候可以调用，根据通道数来精确匹配！
            dict = {'23':'north model-facing north-h=30cm','24':'north model-facing north-h=60cm',\
                    '25':'north model-facing north-h=90cm','26':'north model-facing north-h=110cm',\
                    '27':'north model-roof-east','28':'north model-roof-south',\
                    '29':'north model-roof-west','30':'north model-roof-north',\
                    '31':'north model-facing south-h=110cm','32':'north model-facing south-h=90cm',\
                    '33':'north model-facing south-h=60cm','34':'north model-facing south-h=30cm',\
                    '35':'south model-facing north-h=30cm','36':'south model-facing north-h=60cm',\
                    '37':'south model-facing north-h=90cm','38':'south model-facing north-h=110cm',\
                    '39':'south model-roof-east','40':'south model-roof-south',\
                    '41':'south model-roof-west','42':'south model-roof-north'}
           
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

                    qExist = os.path.exists(r'e:\py_output\\'+dict[str(n)]+r'-10min_average')
                    if not qExist:
                        os.mkdir(r'e:\py_output\\'+dict[str(n)]+r'-10min_average')
                    else:
                        pass
                                
                    wExist = os.path.exists(r'e:\py_output\\'+dict[str(n)]+r'-10min_average'+'\\'+file[-12:-4])
                    if not wExist:
                        os.mkdir(r'e:\py_output\\'+dict[str(n)]+r'-10min_average'+'\\'+file[-12:-4])
                        result.to_csv(r'e:\py_output\\'+dict[str(n)]+r'-10min_average'+'\\'+file[-12:-4]+'\\'+'T_average_10min-'+dict[str(n)]+'-'+f+'-'+file,columns = columns)
                    else:
                        result.to_csv(r'e:\py_output\\'+dict[str(n)]+r'-10min_average'+'\\'+file[-12:-4]+'\\'+'T_average_10min-'+dict[str(n)]+'-'+f+'-'+file,columns = columns)
                
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
                
                


