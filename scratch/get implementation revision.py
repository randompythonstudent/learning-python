# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 01:09:09 2022

@author: jorge
"""

word = 'brontosaurus'
d = dict()
for c in word:
    d[c] = d.get(c, 0) + 1
print(d)