# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 20:02:31 2022

@author: jorge
"""
desired_number = 2
numbers = [1, 2, 3, 4, 7, 2]
count = 0

for number in numbers:
    
    if number == desired_number:
        print(count)
        break
    count = count + 1
        