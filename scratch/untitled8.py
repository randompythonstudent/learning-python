# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 21:07:39 2022

@author: jorge
"""

input1 = input('Enter score: ')
def computegrade (score):
    if score >= 0.9:
        grade = 'A'
    elif score >= 0.8:
        grade = 'B'
    elif score >= 0.7:
        grade = 'C'
    elif score >= 0.6:
        grade = 'D'
    else:
        grade = 'F'
    return grade
try:
    score = float(input1)
    if score >= 0 and score <= 1.0:
        grade = computegrade(score)
        print("Grade: " , grade)
    else: 
        print('bad score')
except:
    print('Enter numeric value')