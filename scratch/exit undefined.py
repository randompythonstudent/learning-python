# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 14:11:52 2022

@author: jorge
"""

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject: '):
        count = count + 1
print('Three were', count, 'subject lines in', fname)