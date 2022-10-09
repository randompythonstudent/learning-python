# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 14:30:58 2022

@author: jorge
"""
fname = open('romeo.txt')
fhand = fname.read()
unique = list()
words = fhand.split()
for word in words:
    if word not in unique:
        unique.append(word)
unique.sort()
print (unique)