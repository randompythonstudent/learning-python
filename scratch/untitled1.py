# -*- coding: utf-8 -*-
"""
Created on Sat May 28 18:03:09 2022

@author: jorge
"""

hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))

rate = 10
regularpay = hours * rate
overtimerate = 10 * 1.5
overtimepay = (hours - 40) * overtimerate + (40 * rate)

if hours <= 40:
    pay = hours * rate
else:
    pay = (hours - 40) * overtimerate + (40 * rate)
print("Pay: " , pay)