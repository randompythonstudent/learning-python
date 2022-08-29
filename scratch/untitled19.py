# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 16:15:53 2022

@author: jorge
"""
word = input('Enter Word')
if word < 'banana':
    print('Your word,' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word,' + word + ', comes after banana.')
else:
    print('All right, bananas.')