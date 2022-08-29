# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 15:27:17 2022

@author: jorge
"""

str = 'X-D8PAM-Confidence:0.8475'
atpos = str.find(':')
print(atpos)

sppos = str.find('5',atpos)
print(sppos)

host = str[atpos+1:sppos+1]
print(float(host))

print(type(float(host)))