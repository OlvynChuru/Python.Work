# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 13:14:49 2017

@author: Matthew Sokolovsky
"""

def series_product_iteration(lis):
    p = 1
    for i in lis:
        p *= i
    return p

print(series_product_iteration([3, 5, 4]))
print(series_product_iteration([-1, 7, 2]))
print(series_product_iteration([5, 2, 0]))

def series_product_recursion(lis):
    if len(lis) != 0:
        return lis.pop() * series_product_recursion(lis)
        # The recursive call happens AFTER lis.pop() happens.
    else:
        return 1
    
print(series_product_recursion([3, 5, 4]))
print(series_product_iteration([-1, 7, 2]))
print(series_product_iteration([5, 2, 0]))