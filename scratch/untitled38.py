# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 01:09:20 2022

@author: jorge
"""

fname = input('Enter file name: ')
fhand = open(fname)
inp = fhand.read().upper()

print(inp)