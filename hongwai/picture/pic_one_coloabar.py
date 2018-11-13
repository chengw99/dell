# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 10:03:34 2018

@author: DELL
"""

import pandas as pd
import os 
import matplotlib.pyplot as plt
import numpy as np

os.chdir(r'E:\py_output\one-facing south') # 适用os.chdir会导致占用文件而无法删除干净，需要用其他来指定分析文件夹位置
data = pd.read_csv('one-facing south-23.csv',names=np.arange(480))
a = np.array(data)

dy = 1350 / (1920 -1) 
dx = dy

x = np.arange(0,dx*480,dx)
y = np.linspace(0,1350,1920)
X,Y = np.meshgrid(x,y)

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(1,1,1)

plt.pcolormesh(X,Y,a,cmap='jet',vmin=24,vmax=36)
plt.gca().set_aspect('equal')
plt.ylabel('height (mm)',fontsize=16,fontname='Times New Roman')
plt.xticks([])
ytciks = ax.set_yticks(np.arange(0,1800,300))
ylabels = ax.set_yticklabels([str(i) for i in np.arange(0,1800,300)]) 
plt.colorbar()
plt.show()