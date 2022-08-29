# -*- coding: utf-8 -*-
"""
Created on Fri May 27 18:31:13 2022

@author: jorge
"""
hours = input("Enter Hours: ")
try:
    int (hours)
    rate = input("Enter Rate: ")
    int(rate)
    pay = int(hours) * int(rate)
    int(pay)
    print ("Pay: ")
    print(pay)
except:
    print("Error, please enter a number. Please run the program again.")