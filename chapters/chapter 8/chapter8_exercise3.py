import sys
numlist = list()
while (True):
    inp = input('Enter a number: ')
    if inp == 'done': break
    try:
        value = float(inp)
    except:
        print('Please enter a number')
        sys.exit()
    numlist.append(value)
    
average = sum(numlist) / len(numlist)
print('Average:', average)
print('Maximum', max(numlist))
print('Minimum', min(numlist))
