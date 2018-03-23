# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 17:50:55 2018

@author: DELL
"""

#此程序用于批量分离提取不同位置不同天数ibutton的24小时数据
#此程序用于ibutton原数据命名为 A+数字
import pandas as pd
import os
import glob

os.chdir('e:\py_data\ibutton')
csv_filenames = glob.glob('e:\\py_data\\ibutton\\*.csv') #获得目标文件的路径，此路径可修改

for filename in csv_filenames:  #
    #读取数据
    data = pd.read_csv(filename,names = ['0','1','2'])
    #每个日期时间序列里文本不同的地方，因为ibutton比较难设置整点开始采集数据
    #获取样本，为获得数据对应的起始和终止编号
    sample = data.ix[22,0][-4:]
    #获取同一个csv文件中不同日期，按照日期分割成不同的文件，最终得到不同日期24小时的ibutton温度数据  
    for i in range(10,11):  #范围根据日期的时间来修改，左边是起点，右边是终点，但不取右边的终点值
        po = str(i)
        start = '17-'+'12'+'-'+po+' 0:0' + sample   #这样可以得到所需的时段
        end = '17-'+'12'+'-'+po+' 23:5' + sample    #只需要修改月份的数字
        a = data[(data.ix[:,0] == start)].index.tolist()  
        b = data[(data.ix[:,0] == end)].index.tolist()  
        f = data.ix[a[0]:b[0],:]
        
        if int(filename[-6:-4]) >= 10:
            if i < 10:
                f.to_csv('e:\\py_output\\'+filename[-6:-4]+'-2017120'+str(i)+'.csv')
            elif i >= 10:
                f.to_csv('e:\\py_output\\'+filename[-6:-4]+'-201712'+str(i)+'.csv')#'''
        
        '''if int(filename[-5]) < 10:
            if i < 10:
                f.to_csv('e:\\py_output\\'+filename[-5]+'-2017120'+str(i)+'.csv')
            elif i >= 10:
                f.to_csv('e:\\py_output\\'+filename[-5]+'-201712'+str(i)+'.csv')#'''