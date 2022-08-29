# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 16:11:20 2022

@author: jorge
"""

def computepay(hours,  rate):
    return hours * rate

regular_rate = float(input("Hourly rate: "))
regular_hours = float(input("Regular hours: "))
overtime_hours = float(input("Overtime hours: "))

regular_pay = computepay(regular_hours, regular_rate)
overtime_pay = computepay(overtime_hours, regular_rate * 1.5)
total_pay = regular_pay + overtime_pay
print(total_pay)