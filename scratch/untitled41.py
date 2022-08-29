# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 01:43:29 2022

@author: jorge
"""

fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence: 0.8475'):
        count = count + 1
    print(count)