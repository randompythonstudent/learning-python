# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 17:34:55 2022

@author: jorge
"""
import os

parent_dir = "C:\\Users\\jorge\\Documents\\learning-python"
file_path = os.path.join(parent_dir, "source\\romeo.txt")
source_file = open(file_path)
unique = list()
for line in source_file:
    words = line.split()
    for word in words:
        if word not in unique:
            unique.append(word)
unique.sort()
print(unique)
        
