# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 01:18:02 2022

@author: jorge
"""
import os

parent_dir = "C:\\Users\\jorge\\Documents\\learning-python"
file_path = os.path.join(parent_dir, "source\\romeo.txt")
source_file = open(file_path)
source = open(source_file)

try:
    source = open('romeo.txt')
except:
    print('File cannot be opened:' , source)
    exit()

counts = dict()
for line in source:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
    print(counts)
    