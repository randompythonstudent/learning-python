# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 12:34:59 2022

@author: jorge
"""
total = 0
count = 0
average = 0
# number_list = [1, 2, 3, 4]

# for number in number_list:
#     total = total + number
#     count = count + 1
# average = total / count
# print(total, count, average)
while True:
    number = input("Input a Number: ")
    if number == 'done':
        break
    try:
        total = total + float(number)
        count = count + 1
    except:
        print("Please Enter a Numerical Value")
average = total / count
print("Total: " ,total, "Count: " , count, "Average: " , average)