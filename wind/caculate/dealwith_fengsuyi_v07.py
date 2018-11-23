# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 12:03:03 2018

@author: DELL
"""

#--------------------------------------v07--------------------------------------#
# 看哪种筛选算法耗时更久
#--------------------------------------v05--------------------------------------#
# 用变量存储时间戳，不需要重复生成

#--结果-#
# 发现改善并不大，时间主要花在 判断是否相等 
#--------------------------------------v04--------------------------------------#
# 对代码进行性能分析，看哪部分运行时间长
# 使用 line_profiler 输出每行代码运行时间
# 输出说明
# 行：文件中的行号。
# 点击次数：执行该行的次数。
# 时间：在计时器单位中执行该行所花费的总时间。在表格之前的标题信息中，您将看到一行“Timer unit：”，将转换因子赋予秒。它可能在不同的系统上有所不同。
# 每次击中：在计时器单位中执行一次线的平均时间。
# ％Time：在该行上花费的时间相对于在函数中花费的总记录时间的百分比。
# 行内容：实际的源代码。请注意，在查看格式化结果时，始终从磁盘读取，而不是在执行代码时读取。如果您在此期间编辑了文件，则这些行将不匹配，并且格式化程序甚至可能无法找到要显示的功能。
# -----可以看到判断获取 同一秒内的数据 花费的时间最长---------------#
#--------------------------------------v03--------------------------------------#
# 此程序用于计算超声风速仪数据，获取24小时风速的秒平均（1秒有20个左右数据，对这20个数据进行平均，作为1秒的数据，但有时并不是1秒产生20个数据，需要进行判断
# 程序运行时间太长，在尝试速度变得更快,可以先处理一小时的数据，看哪种方式更快
# 将python内置函数sum修改为np.sum()，将ix修改为iloc,ix选择数据时效率比较低下

#------------------------------------v01-v02------------------------------------#
#long running
#do something other

# -----------------------------新算法------------------------------------------#
# 找出出现不同时间序列的区间点 
# 1小时的数据需要的时间是 4s
# 加上运算的时间是6s!!!!
import numpy as np
import pandas as pd
import datetime

starttime = datetime.datetime.now()
ipath = r'e:\py_data\wind'
opath = r'e:\py_output'

data = pd.read_csv(ipath+'\\'+'20170511.csv',names=range(11))
l=[]
for i in range(72061): # 72061对应的是 '01:00:00'，这里的数据范围只算了1个小时，做个测试
    
    
    if i < 72060:
        if data.loc[i,1] == data.loc[i+1,1]:
            pass
        else:
            l.append(i)
            
    else:
        pass
    
p=[]
for j in range(len(l)+1):
    if j == 0:
        s = data.loc[0:l[0],3]
        data_mean = np.sum(s.values)/np.float(len(s))
        p.append(data_mean)
        print('Now is:',data.loc[l[0],1])
    if 0< j <= (len(l)-1):
        s = data.loc[l[j-1]+1:l[j],3]
        data_mean = np.sum(s.values)/np.float(len(s))
        p.append(data_mean)
        print('Now is:',data.loc[l[j],1])
    if j == len(l):
        s = data.loc[l[-1]+1:72061-1,3]
        data_mean = np.sum(s.values)/np.float(len(s))
        p.append(data_mean)
        print('Now is:',data.loc[l[-1],1])
result = pd.DataFrame(p)
result.to_csv(opath+'\\'+'v07.csv')               
endtime = datetime.datetime.now()

print('The time you need is {0}s'.format((endtime - starttime).seconds))


#--------------------------=旧算法---------------------------------------------#
# 这种筛选算法（注释掉运算）所需的时间是514s
# 重新加上运算的时间是516s。。。
#==============================================================================
# import numpy as np
# import pandas as pd
# 
# import datetime
# 
# starttime = datetime.datetime.now()
# 
# ipath = r'e:\py_data\wind'
# 
# data = pd.read_csv(ipath+'\\'+ '20170511.csv',names = range(11))
# 
# 
# l=[] 
# p=[]
# for j in range(0,1):
#     if j < 10:
#         
#         for k in range(0,60):
#             if k < 10:
#                 for i in range(0,60):
#                     if i < 10:
#                         try:
#                             a = '0' + str(j) + ':0' + str(k) + ':0' + str(i)
#                             #print(a)
#                             u = data[data.loc[:,1] == a].index.tolist() # 每次都与全部数据进行比较，造成效率低下
#                             #l.append(u) 如果将此命令放在这里，那l里面会增加空列表
#                             #加上条件筛选后，可以去掉空列表
#                             if len(u) == 0:
#                                 print('无数据:',a)
#                             else:
#                                 l.append(u)
#                                 data_mean = np.sum(data.loc[u[0]:u[-1],3])/float(len(u))
#                                 p.append(data_mean)
#                                 
#                                 print('Now is:',a)
#                         except:
#                             pass
#                 
#                     else:
#                         try:
#                             b = '0' + str(j) + ':0' + str(k) + ':' + str(i)
#                             #print(b)
#                             u = data[data.loc[:,1] == b].index.tolist()
#                         
#                         
#                             if len(u) == 0:
#                                 print('无数据',b)
#                             
#                             else:
#                                 l.append(u)
#                                 data_mean = np.sum(data.loc[u[0]:u[-1],3])/float(len(u))
#                                 p.append(data_mean)
#                                 print('Now is:',b)
#                             
#                         except:
#                             pass
#            
#             
#             else:
#                 for i in range(0,60):
#                     if i < 10:
#                         try:
#                             a = '0' + str(j) + ':' + str(k) + ':0' + str(i)
#                             #print(a)
#                             u = data[data.loc[:,1] == a].index.tolist()
#                         
#                         
#                             if len(u) == 0:
#                                 print('无数据',a)
#                             else:
#                                 l.append(u)
#                                 data_mean = np.sum(data.loc[u[0]:u[-1],3])/float(len(u))
#                                 p.append(data_mean)
#                                 print('Now is:',a)
#                             
#                         except:
#                             pass
#                 
#                     else:
#                         try:
#                             b = '0' + str(j) + ':' + str(k) + ':' + str(i)
#                             #print(b)
#                             u = data[data.loc[:,1] == b].index.tolist()
#                         
#                         
#                             if len(u) == 0:
#                                 print('无数据',b)
#                             else:
#                                 l.append(u)
#                                 data_mean = np.sum(data.loc[u[0]:u[-1],3])/float(len(u))
#                                 p.append(data_mean)
#                                 print('Now is:',b)
#                             
#                         except:
#                             pass
#                         
#                         
#     else:
#          for k in range(0,60):
#             if k < 10:
#                 for i in range(0,60):
#                     if i < 10:
#                         try:
#                             a = str(j) + ':0' + str(k) + ':0' + str(i)
#                             print(a)
#                             u = data[data.loc[:,1] == a].index.tolist()
#                             #l.append(u) 如果将此命令放在这里，那l里面会增加空列表
#                             #加上条件筛选后，可以去掉空列表
#                             if len(u) == 0:
#                                 print('无数据',a)
#                             else:
#                                 l.append(u)
#                                 data_mean = np.sum(data.loc[u[0]:u[-1],3])/float(len(u))
#                                 p.append(data_mean)
#                                 print('Now is:',a)
#                         except:
#                             pass
#                 
#                     else:
#                         try:
#                             b = str(j) + ':0' + str(k) + ':' + str(i)
#                             #print(b)
#                             u = data[data.loc[:,1] == b].index.tolist()
#                         
#                         
#                             if len(u) == 0:
#                                 print('无数据',b)
#                             
#                             else:
#                                 l.append(u)
#                                 data_mean = np.sum(data.loc[u[0]:u[-1],3])/float(len(u))
#                                 p.append(data_mean)
#                                 print('Now is:',b)
#                             
#                         except:
#                             pass
#            
#             
#             else:
#                 for i in range(0,60):
#                     if i < 10:
#                         try:
#                             a = str(j) + ':' + str(k) + ':0' + str(i)
#                             #print(a)
#                             u = data[data.loc[:,1] == a].index.tolist()
#                         
#                         
#                             if len(u) == 0:
#                                 print('无数据',a)
#                             else:
#                                 l.append(u)
#                                 data_mean = np.sum(data.loc[u[0]:u[-1],3])/float(len(u))
#                                 p.append(data_mean)
#                                 print('Now is:',a)
#                             
#                         except:
#                             pass
#                 
#                     else:
#                         try:
#                             b = str(j) + ':' + str(k) + ':' + str(i)
#                             #print(b)
#                             u = data[data.loc[:,1] == b].index.tolist()
#                         
#                         
#                             if len(u) == 0:
#                                 print('无数据',b)
#                             else:
#                                 l.append(u)
#                                 data_mean = np.sum(data.loc[u[0]:u[-1],3])/float(len(u))
#                                 p.append(data_mean)
#                                 print('Now is:',b)
#                             
#                         except:
#                             pass
# endtime = datetime.datetime.now()
# 
# print('The time you need is {0}s'.format((endtime - starttime).seconds))
# result = pd.DataFrame(p)
# result.to_csv(r'e:\py_output\v07.csv')
#==============================================================================
