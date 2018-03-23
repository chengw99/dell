# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 17:17:00 2017

@author: DELL
"""

'''import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

os.chdir('e:\\py_output')

data = pd.read_csv('e:\\py_data\\T_average_perhour_A.csv')

x = np.arange(24)
y1 = data.ix[:,2]

plt.plot(x,y1,linewidth = 2.5)
plt.xlim(0,25)
plt.ylim(26,34)
plt.xlabel('hour')
plt.ylabel('℃',rotation = 0)
plt.xticks(np.arange(0,24,2))
plt.yticks(np.arange(26,34))
plt.title('Tem-perhour',fontsize = 18)

#plt.show()
plt.savefig('t.png')'''

#此程序用于批量作图，针对多个csv文件，内含已经求得的每小时平均的温度数据
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob


os.chdir('e:\py_output')
csv_filenames = glob.glob('e:\\py_data\\pic\\*.csv') #得到要处理的文件路径，此路径可修改

for filename in csv_filenames:  #循环处理列举的文件
    data = pd.read_csv(filename)
    x = np.arange(24)
    y = data.ix[:,2]
    
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)  #貌似引入这个才可以调用后面的方法set_xticks
    plt.plot(x,y,'ro-',linewidth = 2.5,label = 'Temperature')
    plt.xlim(0,24) #表示x轴的范围设置为0到24
    plt.ylim(25,40)
    plt.xlabel('time')
    plt.ylabel('T(℃)',rotation = 90)
    #plt.xticks(np.arange(0,26,2))
    plt.yticks(np.arange(25,40,2))
    

    xticks = ax.set_xticks([0,4,8,12,16,20,24])  #此命令行可以确定x轴标签的位置
    xlabels = ax.set_xticklabels(['0:00','4:00','8:00','12:00','16:00','20:00','24:00'])  #此命令行可以命名x坐标轴的标签内容
    #plt.xticklabels(['0:00','2:00','4:00','6:00','8:00','10:00','12:00','14:00','16:00','18:00','20:00','22:00'])
    #plt.title('Tem-perhour',fontsize = 18)
    plt.legend(loc='best')
    plt.savefig('e:\\py_output\\'+filename[33]+'.png') 
    #filename[33]=A,此处视文件名而定
    plt.close()
    