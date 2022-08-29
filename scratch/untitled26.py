# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 18:05:00 2022

@author: jorge
"""

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)