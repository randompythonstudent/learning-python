# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 23:59:59 2022

@author: jorge
"""
total = 0
count = 0
#setting these to empty value so I can update their value later
largest = None
smallest = None
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
        number = float(number)
        total = total + number
        count = count + 1
        if largest is None or number > largest:
            largest = number
        if  smallest is None or number < smallest:
            smallest = number
    except:
        print("Please Enter a Numerical Value")

print("Total: " ,total, "Count: " , count, "Largest: " , largest, "Smallest: ", smallest)
