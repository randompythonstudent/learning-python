# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 15:27:17 2022

@author: jorge
"""
#I set the string that was given to me for the purpose of slicing the required portion to str
str = 'X-D8PAM-Confidence:0.8475'
#I called the method to find the position of the character ":" since everything after this
#character is the portion I want to slice
atpos = str.find(':')
print(atpos)
#I called the method to find the position of the last character in the string since that marked
#the end of the portion I want to slice 
sppos = str.find('5',atpos)
print(sppos)
#I formatted this like in the example in the book and improvised on the variable sppos+1 since
#that was the first thing that came to my mind though I think I could've done that more efficiently
host = str[atpos+1:sppos+1]
print(float(host))
#I once again improvised until it looked correct, I'm not actually sure if this converted the 
#extracted string to a float but it looked right 
print(type(float(host)))