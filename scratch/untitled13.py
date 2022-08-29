# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 16:11:03 2022

@author: jorge
"""

overtime_threshold_hours = 40
rate_modifyer = 1.5
input1 = input('Enter Hours: ')
input2 = input('Enter Rate: ')

def computepay(hours, rate):
    if hours >= overtime_threshold_hours:
        pay = ((hours - overtime_threshold_hours) * rate * rate_modifyer) + (overtime_threshold_hours * rate)
    else:
        pay = hours * rate
    return pay
try:
    hours = float(input1)
    rate = float(input2)
    pay = computepay(hours,rate)
    print("Pay: " , computepay(hours, rate))
except:
    print("Error, please enter numeric input and restart")
    