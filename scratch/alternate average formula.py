# -*- coding: utf-8 -*

numlist = list()
while (True):
    inp = input('enter a number: ')
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)
    
    average = sum(numlist) / len(numlist)
    print('Average: ', average)