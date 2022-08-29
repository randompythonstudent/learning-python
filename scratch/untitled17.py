# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 11:47:02 2022

@author: jorge
"""

smallest = None
print('Before:', smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print('Loop:', itervar, smallest)
print('Smallest:', smallest)