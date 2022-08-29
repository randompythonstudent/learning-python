# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 17:07:55 2022

@author: jorge
"""

overtime_threshold_hours = 40
rate_modifyer = 1.5
input1 = input('Enter Hours: ')
input2 = input('Enter Rate: ')

def compute_pay_usd(hours, rate):
    if hours >= overtime_threshold_hours:
        pay_usd = ((hours - overtime_threshold_hours) * rate * rate_modifyer) + (overtime_threshold_hours * rate) * 0.96
    else:
        pay_usd = hours * rate * 0.96
    return pay_usd
def dollar_to_euro(dollars):
    euros = dollars * 0.96
    return euros
try:
    hours = float(input1)
    rate = float(input2)
    pay_usd = compute_pay_usd(hours,rate)
    dollars_usd = pay_usd
    converstion = dollar_to_euro(dollars_usd)
    print("Pay (USD): " , dollars_usd)
    print ("Pay (Euros): " , converstion)
except:
    print("Error, please enter numeric input and restart")
    