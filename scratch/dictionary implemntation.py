# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 20:14:49 2022

@author: jorge
"""

word = 'brontosaurus'
d = dict()
for c in word:
    if c in word:
        if c not in d:
            d[c] = 1
        else:
            d[c] = d[c] + 1
print(d)