# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 13:35:28 2022

@author: jorge
"""
score = input("Enter Score: ")
try:
  def computegrade():
    if float(score) >= 0.9 and float(score) <= 1.0:
      print("A")
    elif float(score) >= 0.8 and float(score) <= 0.9:
      print("B")
    elif float(score) >= 0.7 and float(score) <= 0.8:
      print("C")
    elif float(score) >= 0.6 and float(score) <= 0.7:
      print("D")
    elif float(score) > 0 and float(score) <= 0.6:
      print("F")
    else:
      print("Bad score.  Please run the program again.")  
  computegrade()
except: 
    print("Bad score.  Please run the program again.")