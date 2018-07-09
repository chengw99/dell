# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 09:16:14 2017

@author: DELL
"""

import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

os.chdir('e:\py_output')

#data = pd.read_csv('test.csv')
#红外数据首次处理成功！  #------v01----------#
#a = np.array(data)
#x = np.arange(480)
#y = np.arange(640)
#c = np.arange(307200).reshape(640,480)   
#X,Y = np.meshgrid(x,y)  #形成格点，可以理解为x=0:479，y=0:639，以1为间隔，横坐标和纵坐标所有的交点就是格点
#plt.pcolor(X,Y,a.T)  #X,Y代表格点，也就是颜色数据的坐标或者说是位置，a.T就是颜色数据，这三者数据必须同样的维度或者X,Y的维度比a.T的维度要大一个
#如果没有界定坐标，直接pcolor（a.T)这样可以没有省略掉  #另外X,Y必须是数组，arrays
#plt.colorbar()

#--------v02---------------#
#把整个壁面的温度数据先聚合起来，再pcolor

data1 = pd.read_csv(r'test1.csv')
data2 = pd.read_csv(r'test2.csv')
data3 = pd.read_csv(r'test3.csv')
#data=data3.T.append(data2.T)
#dataa = data.append(data1.T)
dataa = pd.concat([data3.T,data2.T,data1.T]) #另外一种合并数据的方式
a = np.array(dataa)

#----------------------重新定义坐标刻度------------------------------------------#
#数据纵向有1920个数据，分为（1920-1）段，每段的长度为dy
dy = 1500 / (1920 -1) 
# 1500指的是模型的高度，通过调节这个参数来定义坐标轴的实际刻度，同时可以试验这个高度数据的范围是否可以让1.2m的位置对应图片中的顶盖
dx = dy

#---------------------真实刻度范围的xy坐标---------------------------------------#
x = np.arange(0,dx*479,dx)
# 使用np.arange，间隔是小数的时候，np.arange不取右端点，则右端点需要多加一个小数间隔，才可以取到想取的右端点
#y = np.arange(0,1501,dy)
#y = np.delete(y,-1)
y = np.linspace(0,1500,1920)
# 形成格点
X,Y = np.meshgrid(x,y)

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(1,1,1)
#plt.figure(figsize=(8,12))  #所以需要修改画布大小！
#plt.figure()   #直接pcolor看起来有些扁的原因是使用了默认画布大小参数 figsize=(6.0,4.0) -- 见下面的解释可以知道这个原因是错的
# cmap 指的是彩色映像表，可以换成其他类型的，它对应的实际就是色标能表示的颜色范围，可以有不同的颜色板
# 详细可见 https://matplotlib.org/tutorials/colors/colormaps.html
plt.pcolormesh(X,Y,a,cmap='jet',vmin=20,vmax=42) # poclormesh 瞬间出图。。。。它的用法与pcolor类似
#plt.pcolor(X,Y,a,cmap='jet',vmin=20,vmax=42)  #vmin和vmax用来限定数据的画图颜色范围，只是改colorbar是没用的
# pcolor()有个norm参数，此参数内含vmin和vmax，默认是按照线性标准化plt.colors.Normalize，映射到（0，1）获取colormap
# 此处就不管norm参数了，直接按默认就好，只使用vmin和vmax就可以控制色标范围，当不是以线性标准化的时候（例如对数标准化，此时色标范围是对数值）就可以调用norm参数
# https://matplotlib.org/tutorials/colors/colormapnorms.html?highlight=normalize
plt.gca().set_aspect('equal')  ##打脸##---对上面画布两行打脸！###直接pcolor看起来有些扁主要是数据的坐标轴没有等刻度，
# #----------------------                                       #即x轴和y轴对于同一个区间长度不等，有了这行命令可以不用把画图调大

plt.ylabel('height (m)',fontsize=16,fontname='Times New Roman') # 可通过fontname指定字体类型
#xticks = ax.set_xticks([0,120,240,360,480])
#xlabels = ax.set_xticklabels(['0','120','240','360','480'])
plt.xticks([]) # 关闭x轴刻度
#ax.set_xticks([]) 也可以使用这个命令
ytciks = ax.set_yticks(np.arange(0,1800,300))
# ylabels = ax.set_yticklabels(['0','300','600','900','1200','1500']) 这种写法可以被取代了
ylabels = ax.set_yticklabels([str(i) for i in np.arange(0,1800,300)]) 
plt.colorbar(ticks=[20,24,28,32,36,40,42])  #与matlab有所区别，这个只能改色标的属性，改这个刻度是改不了数据的显示的颜色范围的
# #----------------设置色标参数-----------------#
# #plt.colorbar(extend='both')#extend起的作用只是让色标首尾是否显示箭头的模样，其中min尾端显示箭头，max首端显示箭头，both则首尾端显示箭头
# #plt.colorbar(extendfrac='length')  #超出最值部分的长度选择
# #plt.colorbar(spacing='proportional')  #此参数说明是填色的位置，但我们是按格点填色，这个参数应该不影响
# #plt.colorbar(extendrect='True') 此参数说明超出最值部分的形状，True的时候为矩形，False的时候为三角形
# #plt.colorbar(ticks=[18,24,36]，boundaries=[18,36],values=[18,24,36]) #这个只会也仅会改变色标的属性和显示，改不了数据显示颜色
# format='%.2f'可以修改色标刻度的格式
# drawedges=True 色标是否显示刻度线
plt.show()
#==============================================================================
#plt.axis('equal')  #可以实现坐标等比例
#plt.savefig('4.png')
#---也可以写成这种形式来调用色标
#c = ax.pcolor(X,Y,a,cmap='jet',vmin=20,vmax=42)  #vmin和vmax用来限定数据的画图颜色范围，只是改colorbar是没用的
#fig.colorbar(c,ax=ax,ticks=[20,24,28,32,36,40,42])