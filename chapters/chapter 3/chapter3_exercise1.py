# -*- coding: utf-8 -*-
"""
Created on Sun May 22 19:04:44 2022

@author: jorge
"""
overtime_threshold_hours = 40
rate_modifyer = 1.5
hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))

if hours >= overtime_threshold_hours:
    pay = ((hours - overtime_threshold_hours) * rate * rate_modifyer) + (overtime_threshold_hours * rate)
else:
    pay = hours * rate
print('Pay: ', pay)
