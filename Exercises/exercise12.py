# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 09:17:32 2017

@author: Matthew Sokolovsky
"""

def fibo(x):
    if x > 1:
        return fibo(x-1) + fibo(x-2)
    else:
        return 1
    
print(fibo(0))
print(fibo(1))
print(fibo(2))
print(fibo(3))
print(fibo(4))
print(fibo(5))
print(fibo(6))
print(fibo(7))
print(fibo(30))
print(fibo(40))