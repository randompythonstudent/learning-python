# -*- coding: utf-8 -*-
"""
Created on Sun May 29 18:47:05 2022

@author: jorge
"""

input1 = (input('Enter Score: '))

try:
    score = float(input1)

    if score >= 0 and score <= 1.0:
        if score >= 0.9:
            print('A')
        elif score >= 0.8:
            print ('B')
        elif score >= 0.7:
            print ('C')
        elif score >= 0.6:
            print ('D')
        else:
            print ('F')
    else:
        print('Bad Score')
except:
    print('Enter numeric value')