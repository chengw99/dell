# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 09:51:49 2018

@author: DELL
"""

# 此程序为红外+热电偶对比 提供图像帮助
# 用于检查 由坐标反推位置 是否正确 —— 显示图像看是否选到想要的区域
# 24小时的顶盖高度对应的数据可能都不同，因此只能分开运算，不能批量处理
# 可与pic-three.py搭配使用，由它获取合适的图像高度值，即 m 的值，不可根据这个程序生成的图片判断顶盖的位置是否为1.2m，其实就是判断取数据的方向和范围，大概是否正确

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ipath = r'E:\py_data\hongwai'

data = pd.read_csv(ipath+'\\'+'three-facing south-23.csv',names=np.arange(480)) # 选择不同时段的红外数据文件
#a = np.array(data)[1500:1600,:] # 此数据范围根据推算得出，图像高度数据是1460时，发现刻度1200与顶盖几乎重合，则认为1460可用，对应坐标为 1200*1919/1460=1577
#m = 1460 # 图像高度 - 调整这个数字，以实现顶盖高度h=1.2m
#dy = m / (100 -1)# 100 对应的是纵向数据的个数，不同高宽比拍的红外相片数量不一样，纵向数据的个数也不同

t = 10
h = 8800
a = np.array(data)[t:h,:]
m = 1380
dy = m / (h-t-1)
dx = dy

x = np.arange(0,dx*480,dx) # 横向数据个数是480，这个值不变
# y = np.linspace(0,m,100) # 最后一个数字100代表的是生成多少个数据，此处是 0-m 区间内生成100个数据
y = np.linspace(0,m,(h-t))
X,Y = np.meshgrid(x,y)

fig = plt.figure(figsize=(16,12))
ax = fig.add_subplot(1,1,1)

plt.pcolormesh(X,Y,a,cmap='jet',vmin=20,vmax=36)
plt.gca().set_aspect('equal')
plt.ylabel('height (mm)',fontsize=16,fontname='Times New Roman')
plt.xticks([])
ytciks = ax.set_yticks(np.arange(0,1800,300))
ylabels = ax.set_yticklabels([str(i) for i in np.arange(0,1800,300)]) 
plt.colorbar(ticks=[20,24,28,32,36])
plt.show()
print('data range:',str(t)+':'+str(h))
print('face average:',np.mean(a))

#==============================================================================
# number = [300,600,900,1100,1200] # 单位mm，对应热电偶测点位置
# calculation = []
# for num in number:
#     cal = num * 1919 / m
#     calculation.append(cal)
#     print(str(num)+'mm'+': '+str(cal))
#==============================================================================
