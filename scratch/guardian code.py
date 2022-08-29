# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 14:16:07 2022

@author: jorge
"""
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
print(words[2])