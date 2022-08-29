# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 16:34:36 2022

@author: jorge
"""
score = input('Enter score: ')
def computegrade(score):
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
         
    
try:
        str(computegrade(score))
except:
    print('Enter numeric value')
computegrade(score)
                

    