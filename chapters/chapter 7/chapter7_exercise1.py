# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 17:15:09 2022

@author: jorge
"""

fname = input('Enter file name: ')
fhand = open(fname)
for line in fhand:
    line = line.rstrip().upper()
    print(line)
