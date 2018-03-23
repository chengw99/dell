# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 09:16:14 2017

@author: DELL
"""

import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

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

data1 = pd.read_csv('test1.csv')
data2 = pd.read_csv('test2.csv')
data3 = pd.read_csv('test3.csv')
#data=data3.T.append(data2.T)
#dataa = data.append(data1.T)
dataa = pd.concat([data3.T,data2.T,data1.T]) #另外一种合并数据的方式
a = np.array(dataa)
x = np.arange(480)
y = np.arange(1920)
X,Y = np.meshgrid(x,y)
#plt.figure(figsize=(8,12))  #所以需要修改画布大小！
#plt.figure()   #直接pcolor看起来有些扁的原因是使用了默认画布大小参数
plt.pcolor(X,Y,a,cmap='jet',vmin=20,vmax=36)  #vmin和vmax用来限定数据的画图颜色范围，只是改colorbar是没用的
plt.gca().set_aspect('equal')  ##打脸##---对上面画布两行打脸！###直接pcolor看起来有些扁主要是数据的坐标轴没有等刻度，
#----------------------                                       #即x轴和y轴对于同一个区间长度不等，有了这行命令可以不用把画图调大
#----------------设置色标参数-----------------#
#plt.colorbar(extend='both')#extend起的作用只是让色标首尾是否显示箭头的模样，其中min尾端显示箭头，max首端显示箭头，both则首尾端显示箭头
#plt.colorbar(extendfrac='length')  #这个参数暂时没发现有什么变化
#plt.colorbar(spacing='proportional')  #此参数说明是填色的位置，但我们是按格点填色，这个参数应该不影响
#plt.colorbar(extendrect='True')
#plt.colorbar(ticks=[18,24,36]，boundaries=[18,36],values=[18,24,36]) #这个只会也仅会改变色标的属性和显示，改不了数据显示颜色
plt.colorbar(ticks=[20,24,28,32,36])  #与matlab有所区别，这个只能改色标的属性，改这个刻度是改不了数据的显示的颜色范围的
plt.show()
#plt.axis('equal')  #可以实现坐标等比例
#plt.savefig('4.png')