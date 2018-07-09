# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 10:17:26 2018

@author: DELL
"""

#用于检查 高宽比3:1 模型朝南侧壁顺序是否正确

import pandas as pd
import os 
import matplotlib.pyplot as plt
import numpy as np

os.chdir(r'e:\py_output')
data = pd.read_csv('test2.csv',names=np.arange(480))
a = np.array(data)

dy = 1500 / (8320 -1) 
dx = dy

x = np.arange(0,dx*480,dx)
y = np.linspace(0,1500,8320)
X,Y = np.meshgrid(x,y)

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(1,1,1)

plt.pcolormesh(X,Y,a,cmap='jet',vmin=20,vmax=44)
plt.gca().set_aspect('equal')
plt.ylabel('height (mm)',fontsize=16,fontname='Times New Roman')
plt.xticks([])
ytciks = ax.set_yticks(np.arange(0,1800,300))
ylabels = ax.set_yticklabels([str(i) for i in np.arange(0,1800,300)]) 
plt.colorbar(ticks=[20,24,28,32,36,40,44])
#plt.show()
plt.savefig(r'e:\py_output\test.png')