# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 15:15:03 2022

@author: jorge
"""

while True:
    line = input('> ')
    if len(line) > 0 and line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')