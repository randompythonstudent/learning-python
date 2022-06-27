# -*- coding: utf-8 -*-
"""
Created on Sun May 29 17:44:04 2022

@author: jorge
"""
overtime_threshold_hours = 40
rate_modifyer = 1.5
input1 = input('Enter Hours: ')
input2 = input('Enter Rate: ')

try:
    hours = float(input1)
    rate = float(input2)
    if hours >= overtime_threshold_hours:
        pay = ((hours - overtime_threshold_hours) * rate * rate_modifyer) + (overtime_threshold_hours * rate)
    else:
        pay = hours * rate
    print("Pay: " , pay)
except:
    print("Error, please enter numeric input and restart")
