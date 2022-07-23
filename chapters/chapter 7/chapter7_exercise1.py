# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 17:15:09 2022

@author: jorge
"""

fname = input('Enter file name: ')
fhand = open(fname)
inp = fhand.read().upper()

print(inp)