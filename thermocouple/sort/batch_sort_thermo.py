# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 13:21:59 2017

@author: DELL
"""

#此程序针对的是在同一个文件里有不同日期的数据
import pandas as pd
import os

os.chdir('e:\\py_data\\thermo')

'''dates = pd.date_range('20171101',periods=6)
df = pd.DataFrame(np.arange(24).reshape(6,4),index = dates,columns = ['A','B','C','D'])

a = df.loc['20171103':'20171106']  #本来想通过这个来确定索引范围的，却发现时间这一列不是索引--->那我可以指定此列为指引吗？
print(a)                                                                                #有个问题是这种是精确到秒的，递增方式不知道怎么处理
prinf.to_csv('e:\\py_output\\20170513.csv')t(type(a))'''


data = pd.read_csv('B.csv')

#a = data[(data.Time == '06/26/2017 00:00:03:287')].index.tolist()  #这样就可以得到对应时间段的index
#b = data[(data.Time == '06/26/2017 23:59:03:287')].index.tolist()  #需要这个tolist才可以得到列表

#f = data.ix[a[0]:b[0],:]
#f.to_csv('e:\\py_output\\1.csv')



p = data.Time.values
sample = p[1]
target = sample[17:24]
for i in range(10,11):  #范围根据日期年月日中的’日‘的时间来修改
    po = str(i)
    start = '12/'+po+'/2017 00:00:' + target    #这样可以得到所需的时段
    end = '12/'+po+'/2017 23:59:' + target

    a = data[(data.Time == start)].index.tolist()  
    b = data[(data.Time == end)].index.tolist()  
    f = data.ix[a[0]:b[0],:]
    f.to_csv('e:\\py_output\\'+'201712'+str(i)+'.csv')
    

