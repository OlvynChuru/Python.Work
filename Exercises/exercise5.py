# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 11:33:48 2017

@author: Matthew Sokolovsky
"""
# I would have made this a function if I
#  knew how to make a function with an indefinite
#  number of parameters.
divisors = [5, 7, 11]
count = 0
x = max(divisors)
inc = x
while count < 20:
    isCommonMultiple = True
    for i in divisors:
        if (x % i != 0):
            isCommonMultiple = False
    if isCommonMultiple:
        print(x)
        count += 1
    x += inc