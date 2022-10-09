# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 18:27:08 2022

@author: jorge
"""

fname = input('Enter the file name: ')
fhand = open(fname)
total = 0
count = 0
average = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        atpos = line.find(':')
        value = float(line[atpos+2:])
        total = total + value
average = total / count
print("Average: " , average)
