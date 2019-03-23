# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 19:18:52 2019

@author: DELL
"""
#-----------------------------v01---------------------------------------------#
# 此程序用于获取连续三天的热电偶温度数据,以便分析城市表面（屋顶、壁面、地面）的日循环特征
# 实现逻辑：（1）获取各表面空间平均温度，对此温度进行10min平均，再拼接3天的数据
#         （2）获取单个点温度的10min平均，再拼接3天的数据 -- 这个程序的功能就是这个，只是求了固定点的
# 先获取平均温度再拼接是因为 求出来的平均温度生成文件的时候，可以按照只有日期的格式进行存放，后面筛选连续3天的时候会比较方便

#-----------step 1--------------------#
# 运行 batch-thermo-rename.py
#-----------step 2--------------------#
# 运行此程序
#-----------------------------v02---------------------------------------------#
# 将上述功能封装成函数，实现的功能是 （1）获取各表面空间平均温度，对此温度进行10min平均，再拼接3天的数据

import os
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 工作路径 
ipath = r'E:\py_data\thermo'
opath = r'E:\py_output'


# 检查通道是否异常
def checknum(num,data):
    l = [] #异常通道
    k = [] #正常通道
    for i in num:
        if np.max(data.iloc[:,i]) >= 70 or np.min(data.iloc[:,i]) <= 0: # 温度数据范围在0-70℃视为正常，否则为异常
            l.append(i)
        else:
            k.append(i)
    return l,k

# 计算空间平均温度的 10min平均温度
def caltem(good,data):
    #good 正常通道 ； data 需要处理的数据
    if len(good) != 0:
        #--获取空间平均温度---#
        s = 0
        for i in good:
            s = s + data.iloc[:,i] 
        ave = s/len(good) # 获取城市单元空间平均温度
        
        #--获取时间平均温度，此处是10min---#
        ave_T=[] # 储存10min平均温度
        for j in range(144):
            tem = np.sum(ave[10*j:10*j+10].values)/10.
            ave_T.append(tem)
        
        #--获取间隔10min的时间
        t = data.iloc[:,2]
        time = []
        for k in range(144):
            tt = t[10*k][11:16]
            time.append(tt)
                
    return ave_T,time


# 创建文件保存路径，将dataframe输出为csv文件   
def newfile(new,fo,co,bo):
    #new 生成文件存放的路径
    #fo DataFrame，生成的数据
    #co 数据的列名
    #bo 生成的文件名
    tfile = opath+'\\'+new
    tExist = os.path.exists(tfile)
    if not tExist:
        os.makedirs(tfile)
        fo.to_csv(tfile+'\\'+bo,columns=co)
    else:
        fo.to_csv(tfile+'\\'+bo,columns=co)

# 拼接连续3天的温度数据
def concat_3days(npath):
    #npath 需要拼接数据所在的文件夹  例如opath + '\\'+ wall
    sfile = os.listdir(npath)    
    for s in sfile:
        ffile = glob.glob(npath+'\\'+s+'\\'+'*.csv')
        mfile = os.listdir(npath+'\\'+s)
        
        date = [] # 储存 以整数形式 表示的年月日, 例如 '20170511' -> 20170511
        for f in ffile:
            if f[-3:] == 'csv':
                date.append(int(f[-12:-4]))
            
        for i in list(range(len(date))):
            
            if i < (len(date)-2):
                
                if (date[i+1] - date[i] == 1) and (date[i+2] - date[i+1] == 1):
                    a1 = pd.read_csv(ffile[i])
                    a2 = pd.read_csv(ffile[i+1])
                    a3 = pd.read_csv(ffile[i+2])
                    
                    data1 = a1.iloc[:,2]
                    data2 = a2.iloc[:,2]
                    data3 = a3.iloc[:,2]
                    
                    y = pd.concat([data1,data2,data3])
                    
                    time = list(range(432))
                    cycle = pd.DataFrame({'3 days-Temperature':y,'Time':time})
                    columns = ['Time','3 days-Temperature']
                    
                    lpath = npath+'\\'+ '3 days temperature' + '\\'+s
                    lExist = os.path.exists(lpath)
                    if not lExist:
                        os.makedirs(lpath)
                        cycle.to_csv(lpath+'\\'+mfile[i][:-4]+'-'+mfile[i+2],columns=columns)
                    else:
                        cycle.to_csv(lpath+'\\'+mfile[i][:-4]+'-'+mfile[i+2],columns=columns)
                
                else:
                    pass
                
            else:
                pass    

def repeat(face,n,data,path,filename):
    # face 哪个表面（wall,road,roof)
    # n 表面对应的通道号
    # data 数据集
    # path 存储数据的路径
    # filename 新生成的文件名
    k = checknum(n,data)[1]
    T = caltem(k,data)[0]
    time = caltem(k,data)[1]
    result = pd.DataFrame({(face+' '+'Temperature'):T,'Time':time})
    columns = ['Time',face+' '+'Temperature']
    path = path
    newfile(path,result,columns,filename)

#------------------------------主程序------------------------------------------#
qfile = os.listdir(ipath)
for q in qfile:
    wfile = glob.glob(ipath+'\\'+q+'\\'+'*.csv')
    for w in wfile:
        if os.path.basename(w)[-3:] == 'csv':
            a = pd.read_csv(w)
            fname = os.path.basename(w)[-12:]
            
            # 壁面
            num_wall = list(range(31,39)) # 侧壁对应通道数
            wall_path = 'Wall'+'\\'+q[2:]
            repeat('Wall',num_wall,a,wall_path,fname)
            
            # 屋顶
            num_roof = list(range(27,31)) + list(range(39,43)) # 屋顶对应通道
            roof_path = 'Roof'+'\\'+q[2:]
            repeat('Roof',num_roof,a,roof_path,fname)
            
            # 地面
            if os.path.basename(w)[2:11] == 'HW3-empty':
                num_road = list(range(13,18)) # 地面对应通道数
            else:
                num_road = list(range(3,8)) # 地面对应通道数

            road_path = 'Road'+'\\'+q[2:]
            repeat('Road',num_road,a,road_path,fname)

# 拼接3天连续温度数据
vfile = os.listdir(opath)
for v in vfile:
    concat_3days(opath+'\\'+v)

       
    
    
    
    
    
    
'''    
#------------------------------主程序------------------------------------------#
qfile = os.listdir(ipath)
for q in qfile:
    wfile = glob.glob(ipath+'\\'+q+'\\'+'*.csv')
    for w in wfile:
        if os.path.basename(w)[-3:] == 'csv':
            a = pd.read_csv(w)
            fname = os.path.basename(w)[-12:]
            #--------------------获取10min平均温度数据---------------------------#
            # 壁面
            num_wall = list(range(31,39)) # 侧壁对应通道数
            k_wall = checknum(num_wall,a)[1] # 侧壁正常通道
            wall_T = caltem(k_wall,a)[0] # 空间平均的侧壁温度取10min平均
            wall_time = caltem(k_wall,a)[1] # 间隔10min的时间
            wall = pd.DataFrame({'Wall Temperature':wall_T,'Time':wall_time})
            columns_wall = ['Time','Wall Temperature']
            
            wall_path = 'wall'+'\\'+q[2:]
            newfile(wall_path,wall,columns_wall,fname)
            
            # 屋顶
            num_roof = list(range(27,31)) + list(range(39,43)) # 屋顶对应通道
            k_roof = checknum(num_roof,a)[1] # 屋顶正常通道
            roof_T = caltem(k_roof,a)[0] # 空间平均的屋顶温度取10min平均
            roof_time = caltem(k_roof,a)[1] #间隔10min的时间
            roof = pd.DataFrame({'Roof Temperature':roof_T,'Time':roof_time})
            columns_roof = ['Time','Roof Temperature']
            
            roof_path = 'roof'+'\\'+q[2:]
            newfile(roof_path,roof,columns_roof,fname)
            
            # 地面
            if os.path.basename(w)[2:11] == 'HW3-empty':
                num_road = list(range(13,18)) # 地面对应通道数
                k_road = checknum(num_road,a)[1] # 地面正常通道
                road_T = caltem(k_road,a)[0] # 空间平均的地面温度取10min平均
                road_time = caltem(k_road,a)[1] # 间隔10min的时间
            else:
                num_road = list(range(3,8)) # 地面对应通道数
                k_road = checknum(num_road,a)[1] # 地面正常通道
                road_T = caltem(k_road,a)[0] # 空间平均的地面温度取10min平均
                road_time = caltem(k_road,a)[1] # 间隔10min的时间
            road = pd.DataFrame({'Road Temperature':road_T,'Time':road_time})
            columns_road = ['Time','Road Temperature']
            
            road_path = 'road'+'\\'+q[2:]
            newfile(road_path,road,columns_road,fname)


# 拼接3天连续温度数据
vfile = os.listdir(opath)
for v in vfile:
    concat_3days(opath+'\\'+v)
    
'''

























'''
# 测试-- 计算10min平均温度
def temtry(good,data):
    if len(good) != 0:
        for j in good:
            a = data.iloc[:,j]
            
            ave = []
            for i in range(144):
                tem = np.sum(a[10*i:10*i+10].values)/10.
                ave.append(tem)
            
            t = data.iloc[:,2]
            time = []
            for k in range(144):
                tt = t[10*k][11:16]
                time.append(tt)
            
    return ave,time
'''

