# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 21:51:52 2022

@author: jorge
"""

fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp))
print(inp[:20])