# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 13:15:32 2018

@author: DELL
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def showRoseWind(values,datatime,max_value): # max_value为整型，指定最大的蓝色值
    N = 8
    theta = np.arange(0.,2 * np.pi, 2 * np.pi / N)
    radii = np.array(values) # values数组指的是想为其作图的数据，这里是指hist数组
    
    plt.axes([0.025,0.025,0.95,0.95],polar=True) # polar不为True时，则为直方图
    colors = [(1-x/max_value,1-x/max_value,0.8) for x in radii] 
    plt.bar(theta,radii,width=(2*np.pi/N),bottom=0.0,color=colors)
    plt.title(datatime,x=0.2,fontsize=20) # datatime为字符串类型，指定图表标题的名称
    
data = pd.read_csv(r'C:\Users\DELL\Desktop\处理数据\按日期排序\station\north station\201705\20170515.csv',engine='python')
wind_deg = data['WDIR']
hist,bins = np.histogram(wind_deg,8,[0,360]) # 创建一个直方图，将360度分为八个面元，每个面元45度，把所有的数据点分到这八个面元中
# 返回结果中的数组hist为落在每个面元的数据点数量，数组bins定义了360度范围内各面元的边界

showRoseWind(hist,'20170511',max(hist))

# 整个360度的范围被分成八个区域，每个区域弧长为45度，此外每个区域还有一列呈放射状排列的刻度值，在每个区域中，用半径长度可以改变的扇形表示一个数值
# 半径越长，扇形所表示的数值就越大，为了增强图表的可读性，我们使用与扇形半径相对应的颜色表
# 半径越长，扇形跨度越大，颜色越接近于深蓝色