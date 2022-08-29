# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 12:32:49 2022

@author: jorge
"""

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1: continue
    print(line)