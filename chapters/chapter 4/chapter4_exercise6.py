# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 17:22:16 2022

@author: jorge
"""

overtime_threshold_hours = 40
rate_modifyer = 1.5
input1 = (input('Enter Hours: '))
input2 = (input('Enter Rate: '))
# def computepay(hours, rate):
#     try:
#         hours = float(hours)
#         rate = float(rate)
#         if hours >= overtime_threshold_hours:
#             pay = ((hours - overtime_threshold_hours) * rate * rate_modifyer) + (overtime_threshold_hours * rate)
#         else:
#             pay = hours * rate
#         print("Pay: " , pay)
#     except:
#         print("Error, please enter numeric input and restart")
# computepay(input1, input2)
def computepay2(hours, rate):
    if hours >= overtime_threshold_hours:
        pay =((hours - overtime_threshold_hours) * rate * rate_modifyer) + (overtime_threshold_hours * rate)
    else:
        pay = hours * rate
    return pay
try:
    hours = float(input1)
    rate = float(input2)
    pay = computepay2(hours,rate)
    print("Pay: " , pay)
except:
    print("Error, please enter numeric input and restart")

# regular_hours = float(input("Enter Hours: "))
# regular_rate = float(input("Enter Rate: "))
# overtime_hours = float(input("Enter overtime hours: "))
# regular_pay = hours * rate
# overtime_pay = overtime_hours * regular_rate * 1.5
# total_pay = regular_pay + overtime_pay
# print("total_pay")
    