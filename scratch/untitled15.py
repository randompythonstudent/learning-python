# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 10:46:16 2022

@author: jorge
"""

while True:
    line = input('>')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')