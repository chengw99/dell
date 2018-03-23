# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 09:30:32 2018

@author: DELL
"""

#此程序用于批量处理ibutton24小时数据，对其进行每小时平均，并将生成的文件移动到指定文件夹

import os
import shutil
import pandas as pd
import numpy as np

os.chdir('e:\\py_data\\ibutton')

#---------复制文件到工作目录，这一步其实可以没有，只是想学一下怎么移动文件-----------------
folder_file = os.listdir(r'C:\Users\DELL\Desktop\处理数据\按日期排序\ibutton\5月份')
for i in folder_file:
    data_file = os.listdir(r'C:\Users\DELL\Desktop\处理数据\按日期排序\ibutton\5月份\\'+i)
    for file in data_file:
        isExist = os.path.exists('e:\\py_data\\ibutton\\'+i)
        if not isExist:
            os.mkdir(i)
        else:
            pass
        shutil.copyfile(r'C:\Users\DELL\Desktop\处理数据\按日期排序\ibutton\5月份\\'+i+'\\'+file,'e:\\py_data\\ibutton\\'+i+'\\'+file)

#----------------遍历数据文件夹，求温度数据的每小时平均-------------------------------
batch_filenames = os.listdir('e:\\py_data\\ibutton')  #文件夹名
for j in batch_filenames:
    csv_filenames = os.listdir('e:\\py_data\\ibutton\\'+j)  #文件名
    os.chdir('e:\\py_data\\ibutton\\'+j) #更改工作目录
    
    for file in csv_filenames:
        if file[-3:] == 'csv': #筛选csv格式文件
            
            a = pd.read_csv(file,names = ['0','1','2']) #读取数据
            data = a.ix[:,2].values.astype(np.float) #取数据列
            #计算温度数据每小时平均
            tem = []
            for i in range(24):
                data_mean = sum(data[i*6:i*6+6])/6.
                tem.append(data_mean)
            #原文件的时间序列不好提取，生成新的时间序列
            time = []
            for j in range(24):
                t = str(j) + ':00'
                time.append(t)
            #生成新的csv文件
            #新的方法，在生成新文件的同时把它塞进对应的文件夹里
            '''isExist = os.path.exists('e:\\py_output\\'+file[:2])
            if not isExist:
                os.mkdir('e:\\py_output\\'+file[:2])
                
                result = pd.DataFrame({'time':time,'Temperature':tem})
                columns = ['time','Temperature']  #指定列的排列
                result.to_csv('e:\\py_output\\'+file[:2]+'\\T_average_perhour_'+file[:11]+'.csv',columns = columns)
            else:
                result = pd.DataFrame({'time':time,'Temperature':tem})
                columns = ['time','Temperature']  #指定列的排列
                result.to_csv('e:\\py_output\\'+file[:2]+'\\T_average_perhour_'+file[:11]+'.csv',columns = columns)'''
            
#---------------------------移动文件到指定文件夹-----------------------------------   
     
            result = pd.DataFrame({'time':time,'Temperature':tem})
            columns = ['time','Temperature']  #指定列的排列
            result.to_csv('e:\\py_output\\T_average_perhour_'+file[:11]+'.csv',columns = columns)
            
#上一段代码更简洁，而且可以实现同样的功能
#这里是按位置生成文件夹A1，A2，B1...，按位置筛选
'''folderaddress = 'e:\\py_output'      #目标路径
file_all = os.listdir(folderaddress) #路径下所有文件名
folderlist = []                      #存放文件夹的命名
os.chdir('e:\\py_output')            #修改工作目录

#创建指定文件夹
for name in file_all:
    if name[-3:] == 'csv':            #此处可设定移动文件的类型 
        folderlist.append(name[-15:-13])  #此处获取所需对应的文件夹名
        isExists = os.path.exists(name[-15:-13]) #判断文件夹是否存在
        if not isExists:                     #加一个判断语句，就不会因为文件已存在而报错
            os.mkdir(folderaddress+'\\'+name[-15:-13])
        else:
            pass

#移动文件    
for i in file_all:                    #遍历所有目标文件
    for j in folderlist:              #遍历文件夹 
        #判断文件是否存在以及文件名与文件夹名是否一致，进行定向筛选
        if os.path.isfile(folderaddress+'\\'+i) == True and i[-15:-13] == j:
            #移动文件到目标文件夹
            shutil.copyfile(folderaddress+'\\'+i,folderaddress+'\\'+j+'\\'+i)
            #删除原来位置的文件
            os.remove(folderaddress+'\\'+i)'''
            
#---------------------按日期生成文件夹，筛选相同日期的所有文件-------------------------
#只需要修改文件名(提供分类标志）以及name[]内数字的范围即可进行任意文件夹分类
folderaddress = 'e:\\py_output'      #目标路径
file_all = os.listdir(folderaddress) #路径下所有文件名
folderlist = []                      #存放文件夹的命名
os.chdir('e:\\py_output')            #修改工作目录

for name in file_all:
    if name[-3:] == 'csv':            #此处可设定移动文件的类型 
        folderlist.append(name[-12:-4])  #此处获取所需对应的文件夹名
        isExists = os.path.exists(name[-12:-4]) #判断文件夹是否存在
        if not isExists:                     #加一个判断语句，就不会因为文件已存在而报错
            os.mkdir(folderaddress+'\\'+name[-12:-4])
        else:
            pass

#移动文件    
for i in file_all:                    #遍历所有目标文件
    for j in folderlist:              #遍历文件夹 
        #判断文件是否存在以及文件名与文件夹名是否一致，进行定向筛选
        if os.path.isfile(folderaddress+'\\'+i) == True and i[-12:-4] == j:
            #移动文件到目标文件夹
            shutil.copyfile(folderaddress+'\\'+i,folderaddress+'\\'+j+'\\'+i)
            #删除原来位置的文件
            os.remove(folderaddress+'\\'+i)
            
#批量重命名
#写得好啰嗦，看以后这里能不能改进
fname = os.listdir('e:\\py_output')
for f in fname:
    goodname = os.listdir('E:\\py_output\\'+f)

    for name in goodname:
        if name[18:20] == 'A1':
            shutil.move('E:\\py_output\\'+f+'\\'+name,'e:\py_output\\'+f+'\\'+'T_perhour_A1_sandmodel-HW2-h=10cm-'+name[21:29]+'.csv')
        if name[18:20] == 'A2':
            shutil.move('E:\\py_output\\'+f+'\\'+name,'e:\py_output\\'+f+'\\'+'T_perhour_A2_sandmodel-HW2-h=30cm-'+name[21:29]+'.csv')
        if name[18:20] == 'A3':
            shutil.move('E:\\py_output\\'+f+'\\'+name,'e:\py_output\\'+f+'\\'+'T_perhour_A3_sandmodel-HW2-h=60cm-'+name[21:29]+'.csv')
        if name[18:20] == 'A4':
            shutil.move('E:\\py_output\\'+f+'\\'+name,'e:\py_output\\'+f+'\\'+'T_perhour_A4_sandmodel-HW2-h=144cm-'+name[21:29]+'.csv')
        if name[18:20] == 'A5':
            shutil.move('E:\\py_output\\'+f+'\\'+name,'e:\py_output\\'+f+'\\'+'T_perhour_A5_sandmodel-HW2-N-h=144cm-'+name[21:29]+'.csv')
        if name[18:20] == 'A6':
            shutil.move('E:\\py_output\\'+f+'\\'+name,'e:\py_output\\'+f+'\\'+'T_perhour_A6_sandmodel-HW2-S-h=144cm-'+name[21:29]+'.csv')
        
        if name[18:20] == 'B1':
            shutil.move('E:\\py_output\\'+f+'\\'+name,'e:\py_output\\'+f+'\\'+'T_perhour_B1_emptymodel-HW1-h=10cm-'+name[21:29]+'.csv')
        if name[18:20] == 'B2':
            shutil.move('E:\\py_output\\'+f+'\\'+name,'e:\py_output\\'+f+'\\'+'T_perhour_B2_emptymodel-HW1-h=30cm-'+name[21:29]+'.csv')
        if name[18:20] == 'B3':
            shutil.move('E:\\py_output\\'+f+'\\'+name,'e:\py_output\\'+f+'\\'+'T_perhour_B3_emptymodel-HW1-h=60cm-'+name[21:29]+'.csv')
        if name[18:20] == 'B4':
            shutil.move('E:\\py_output\\'+f+'\\'+name,'e:\py_output\\'+f+'\\'+'T_perhour_B4_emptymodel-HW1-h=144cm-'+name[21:29]+'.csv')
        if name[18:20] == 'B5':
            shutil.move('E:\\py_output\\'+f+'\\'+name,'e:\py_output\\'+f+'\\'+'T_perhour_B5_emptymodel-HW1-N-h=144cm-'+name[21:29]+'.csv')
        if name[18:20] == 'B6':
            shutil.move('E:\\py_output\\'+f+'\\'+name,'e:\py_output\\'+f+'\\'+'T_perhour_B6_emptymodel-HW1-S-h=144cm-'+name[21:29]+'.csv')
         
        if name[18:20] == 'C1':
            shutil.move('E:\\py_output\\'+f+'\\'+name,'e:\py_output\\'+f+'\\'+'T_perhour_C1_emptymodel-HW3-h=10cm-'+name[21:29]+'.csv')
        if name[18:20] == 'C2':
            shutil.move('E:\\py_output\\'+f+'\\'+name,'e:\py_output\\'+f+'\\'+'T_perhour_C2_emptymodel-HW3-h=30cm-'+name[21:29]+'.csv')
        if name[18:20] == 'C3':
            shutil.move('E:\\py_output\\'+f+'\\'+name,'e:\py_output\\'+f+'\\'+'T_perhour_C3_emptymodel-HW3-h=60cm-'+name[21:29]+'.csv')
        if name[18:20] == 'C4':
            shutil.move('E:\\py_output\\'+f+'\\'+name,'e:\py_output\\'+f+'\\'+'T_perhour_C4_emptymodel-HW3-h=144cm-'+name[21:29]+'.csv')
        if name[18:20] == 'C5':
            shutil.move('E:\\py_output\\'+f+'\\'+name,'e:\py_output\\'+f+'\\'+'T_perhour_C5_emptymodel-HW3-N-h=144cm-'+name[21:29]+'.csv')
        if name[18:20] == 'C6':
            shutil.move('E:\\py_output\\'+f+'\\'+name,'e:\py_output\\'+f+'\\'+'T_perhour_C6_emptymodel-HW3-S-h=144cm-'+name[21:29]+'.csv')
        
        if name[18:20] == 'D1':
            shutil.move('E:\\py_output\\'+f+'\\'+name,'e:\py_output\\'+f+'\\'+'T_perhour_D1_sandmodel-HW3-h=10cm-'+name[21:29]+'.csv')
        if name[18:20] == 'D2':
            shutil.move('E:\\py_output\\'+f+'\\'+name,'e:\py_output\\'+f+'\\'+'T_perhour_D2_sandmodel-HW3-h=30cm-'+name[21:29]+'.csv')
        if name[18:20] == 'D3':
            shutil.move('E:\\py_output\\'+f+'\\'+name,'e:\py_output\\'+f+'\\'+'T_perhour_D3_sandmodel-HW3-h=60cm-'+name[21:29]+'.csv')
        if name[18:20] == 'D4':
            shutil.move('E:\\py_output\\'+f+'\\'+name,'e:\py_output\\'+f+'\\'+'T_perhour_D4_sandmodel-HW3-h=144cm-'+name[21:29]+'.csv')
        if name[18:20] == 'D5':
            shutil.move('E:\\py_output\\'+f+'\\'+name,'e:\py_output\\'+f+'\\'+'T_perhour_D5_sandmodel-HW3-N-h=144cm-'+name[21:29]+'.csv')
        if name[18:20] == 'D6':
            shutil.move('E:\\py_output\\'+f+'\\'+name,'e:\py_output\\'+f+'\\'+'T_perhour_D6_sandmodel-HW3-S-h=144cm-'+name[21:29]+'.csv')
        
        if name[18:20] == 'E1':
            shutil.move('E:\\py_output\\'+f+'\\'+name,'e:\py_output\\'+f+'\\'+'T_perhour_E1_sandmodel-HW1-h=10cm-'+name[21:29]+'.csv')
        if name[18:20] == 'E2':
            shutil.move('E:\\py_output\\'+f+'\\'+name,'e:\py_output\\'+f+'\\'+'T_perhour_E2_sandmodel-HW1-h=30cm-'+name[21:29]+'.csv')
        if name[18:20] == 'E3':
            shutil.move('E:\\py_output\\'+f+'\\'+name,'e:\py_output\\'+f+'\\'+'T_perhour_E3_sandmodel-HW1-h=60cm-'+name[21:29]+'.csv')
        if name[18:20] == 'E5':
            shutil.move('E:\\py_output\\'+f+'\\'+name,'e:\py_output\\'+f+'\\'+'T_perhour_E5_sandmodel-HW1-N-h=144cm-'+name[21:29]+'.csv')
        if name[18:20] == 'E6':
            shutil.move('E:\\py_output\\'+f+'\\'+name,'e:\py_output\\'+f+'\\'+'T_perhour_E6_sandmodel-HW1-S-h=144cm-'+name[21:29]+'.csv')
        
        if name[18:20] == 'F1':
            shutil.move('E:\\py_output\\'+f+'\\'+name,'e:\py_output\\'+f+'\\'+'T_perhour_F1_emptymodel-HW2-h=10cm-'+name[21:29]+'.csv')
        if name[18:20] == 'F2':
            shutil.move('E:\\py_output\\'+f+'\\'+name,'e:\py_output\\'+f+'\\'+'T_perhour_F2_emptymodel-HW2-h=30cm-'+name[21:29]+'.csv')
        if name[18:20] == 'F3':
            shutil.move('E:\\py_output\\'+f+'\\'+name,'e:\py_output\\'+f+'\\'+'T_perhour_F3_emptymodel-HW2-h=60cm-'+name[21:29]+'.csv')
        if name[18:20] == 'F4':
            shutil.move('E:\\py_output\\'+f+'\\'+name,'e:\py_output\\'+f+'\\'+'T_perhour_F4_emptymodel-HW2-h=144cm-'+name[21:29]+'.csv')
        if name[18:20] == 'F5':
            shutil.move('E:\\py_output\\'+f+'\\'+name,'e:\py_output\\'+f+'\\'+'T_perhour_F5_emptymodel-HW2-N-h=144cm-'+name[21:29]+'.csv')
        if name[18:20] == 'F6':
            shutil.move('E:\\py_output\\'+f+'\\'+name,'e:\py_output\\'+f+'\\'+'T_perhour_F6_emptymodel-HW2-S-h=144cm-'+name[21:29]+'.csv')

#------------------------将整理好的文件夹移动到指定的文件夹--------------------------
filenames = os.listdir('e:\\py_output')
for file in filenames:
    shutil.move('e:\\py_output\\'+file,r'C:\Users\DELL\Desktop\处理数据\分析数据\ibutton')
#在每个日期文件夹里创建一个文件夹命名为每小时平均
#这一步并不是必须的，而且算法上这样有点累赘，可以在前面生成预定的文件夹，从而减少代码量
filenames2 = os.listdir(r'C:\Users\DELL\Desktop\处理数据\分析数据\ibutton')
for file in filenames2:
    csv_filenames = os.listdir(r'C:\Users\DELL\Desktop\处理数据\分析数据\ibutton\\'+file)
    isExist = os.path.exists(r'C:\Users\DELL\Desktop\处理数据\分析数据\ibutton\\'+file+'\\'+r'每小时平均')
    if not isExist:
        os.mkdir(r'C:\Users\DELL\Desktop\处理数据\分析数据\ibutton\\'+file+'\\'+r'每小时平均')
        for i in csv_filenames:
            shutil.move(r'C:\Users\DELL\Desktop\处理数据\分析数据\ibutton\\'+file+'\\'+i,r'C:\Users\DELL\Desktop\处理数据\分析数据\ibutton\\'+file+'\\'+r'每小时平均'+'\\'+i)
    else:
        for i in csv_filenames:
            shutil.move(r'C:\Users\DELL\Desktop\处理数据\分析数据\ibutton\\'+file+'\\'+i,r'C:\Users\DELL\Desktop\处理数据\分析数据\ibutton\\'+file+'\\'+r'每小时平均'+'\\'+i)

#-----------------------清除输入数据文件夹的数据-----------------------------------
inputfile = os.listdir('e:\\py_data\\ibutton')
for filename in inputfile:
    shutil.rmtree('e:\\py_data\\ibutton\\'+filename)  #os.rmdir也可以删除文件夹，但只能删除空的文件夹
