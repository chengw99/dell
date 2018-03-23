# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 18:18:29 2017

@author: DELL
"""

#用来判断热电偶通道数对应的列数
#这个程序是基于CH01对应的列数是2的时候
number = int(input('Please input your number:'))
condition = number - 100
if condition < 21:
    a = number - 100 + 1
    print(a)
elif 100<condition<121:
    b = number - 200 + 21
    print(b)
elif 200<condition<221:
    c = number - 300 + 41
    print(c)