# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 16:36:49 2022

@author: jorge
"""

fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)