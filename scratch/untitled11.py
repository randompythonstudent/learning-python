# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 13:16:26 2022

@author: jorge
"""

overtimehours = 40
rate_modifyer = 1.5
input1 = input("Enter Hours: ")
input2 = input("Enter Rate: ")

def computepay(hours, rate):
    if hours >= overtimehours:
        pay =((hours - overtimehours)) * rate * rate_modifyer + (overtimehours * rate)
    else:
        pay = hours * rate
    return pay
try:
    hours = float(input1)
    rate = float(input2)
    pay = computepay(hours, rate)
    print("Pay: " , pay)
except:
    print("Please Enter a Numeric value")
        