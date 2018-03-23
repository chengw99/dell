# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 16:09:50 2018

@author: DELL
"""

#此程序用于批量分离提取不同位置不同天数ibutton的24小时数据
#此程序用于ibutton原数据命名为 A+数字
import pandas as pd
import os
import glob
import shutil

#----------------------将待处理数据输入工作目录------------------------------------
file_data = os.listdir(r'C:\Users\DELL\Desktop\处理数据\源数据\ibutton数据\20170608-20170622')
for file in file_data:
    if file[-3:] == 'csv':
        #复制文件到指定文件夹
        shutil.copyfile(r'C:\Users\DELL\Desktop\处理数据\源数据\ibutton数据\20170608-20170622\\'+file,'e:\\py_data\\ibutton\\'+file)
#----------------------用于分离不同日期的文件--------------------------------------
os.chdir('e:\py_data\ibutton')
csv_filenames = glob.glob('e:\\py_data\\ibutton\\*.csv') #获得目标文件的路径，此路径可修改

for filename in csv_filenames:  
    
    #读取数据
    data = pd.read_csv(filename,names = ['0','1','2'])
    #每个日期时间序列里文本不同的地方，因为ibutton比较难设置整点开始采集数据
    #获取样本，为获得数据对应的起始和终止编号
    sample = data.ix[22,0][-4:]
    #获取同一个csv文件中不同日期，按照日期分割成不同的文件，最终得到不同日期24小时的ibutton温度数据  
    for i in range(9,23):  #范围根据日期的时间来修改，左边是起点，右边是终点，但不取右边的终点值
        po = str(i)
        start = '17-'+'6'+'-'+po+' 0:0' + sample   #这样可以得到所需的时段
        end = '17-'+'6'+'-'+po+' 23:5' + sample    #只需要修改月份的数字
        a = data[(data.ix[:,0] == start)].index.tolist()  
        b = data[(data.ix[:,0] == end)].index.tolist()  
        f = data.ix[a[0]:b[0],:]
        if i < 10:
            f.to_csv('e:\\py_output\\'+filename[-6:-4]+'-2017060'+str(i)+'.csv')
        elif i >= 10:
            f.to_csv('e:\\py_output\\'+filename[-6:-4]+'-201706'+str(i)+'.csv')

#---------------------------移动文件到指定文件夹-----------------------------------
folderaddress = 'e:\\py_output'      #目标路径
file_all = os.listdir(folderaddress) #路径下所有文件名
folderlist = []                      #存放文件夹的命名
os.chdir('e:\\py_output')            #修改工作目录

#创建指定文件夹
for name in file_all:
    if name[-3:] == 'csv':            #此处可设定移动文件的类型 
        folderlist.append(name[:2])  #此处获取所需对应的文件夹名
        isExists = os.path.exists(name[0:2]) #判断文件夹是否存在
        if not isExists:                     #加一个判断语句，就不会因为文件已存在而报错
            os.mkdir(folderaddress+'\\'+name[0:2])
        else:
            pass

#移动文件    
for i in file_all:                    #遍历所有目标文件
    for j in folderlist:              #遍历文件夹 
        #判断文件是否存在以及文件名与文件夹名是否一致，进行定向筛选
        if os.path.isfile(folderaddress+'\\'+i) == True and i[0:2] == j:
            #复制文件到目标文件夹
            shutil.copyfile(folderaddress+'\\'+i,folderaddress+'\\'+j+'\\'+i)
            #删除原来位置的文件
            os.remove(folderaddress+'\\'+i)
            
#------------------------将整理好的文件夹移动到指定的文件夹--------------------------
filenames = os.listdir('e:\\py_output')
for file in filenames:
    #移动某个文件夹到另一个文件夹
    shutil.move('e:\\py_output\\'+file,r'C:\Users\DELL\Desktop\处理数据\按日期排序\ibutton\6月份')

#-----------------------清除输入数据文件夹的数据-----------------------------------
inputfile = os.listdir('e:\\py_data\\ibutton')
for filename in inputfile:
    os.remove('e:\\py_data\\ibutton\\'+filename)

