# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 14:01:54 2022

@author: jorge
"""

fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
    print('There were', count, 'subject lines in', fname)