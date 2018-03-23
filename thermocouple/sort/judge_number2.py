# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 11:03:40 2017

@author: DELL
"""

#用来判断热电偶通道数对应的列数
#这个程序是基于CH01对应的列数是3的时候，前一版本的程序是基于CH01对应的列数是2的情况，发生改变的原因是我程序选取了规定日期的数据，另外生成
#一个新的csv文件的时候增加了一列，实际上也可以删掉这列，但是也可以改这里的判断程序，在原来的基础上＋1就好，都可以
number = int(input('Please input your number:'))
condition = number - 100
if condition < 21:
    a = number - 100 + 2
    print(a)
elif 100<condition<121:
    b = number - 200 + 22
    print(b)
elif 200<condition<221:
    c = number - 300 + 42
    print(c)