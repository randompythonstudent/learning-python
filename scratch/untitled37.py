# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 14:36:48 2022

@author: jorge
"""

fout = open('output.txt', 'w')
print(fout)

line1 = "This here's the wattle.\n"
fout.write(line1)
print(fout.write(line1))

line2 = 'the emblem of our land.\n'
fout.write(line2)
print(fout.write(line2))

fout.close()