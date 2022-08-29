# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 14:40:45 2022

@author: jorge
"""

data = 'From stephon.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ',atpos)
print(sppos)

host = data[atpos+1:sppos]
print(host)
