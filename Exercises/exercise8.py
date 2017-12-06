# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 20:25:53 2017

@author: Matthew Sokolovsky
"""

a = ['e', 'r', 'o', 'p']
b = a
print('a: ', a)
print('b: ', b)
b[1] = 'v'
print('a: ', a)
print('b: ', b)
# When I changed b[1], that also changed a[1].
#  I think the elements of Python lists are just pointers. When
#  I do b = a, I am copying all the pointers from a
#  into b. When I do b[1] = 'v', it changes the value
#  being pointed at to 'v'. Since a[1] uses the same
#  pointer as b[1], it will also point at 'v'.

c = a[:]
c[2] = 's'
print('a: ', a)
print('c: ', c)
# When I changed c[2], that did not change a[2].
# My hypthesis is that due to the statement c = a[:],
#  c uses a different set of pointers from a. When I do
#  c[2] = 's', I change the value that c[2] is pointing at,
#  but not the value that a[2] is pointing at.

def set_first_elem_to_zero(l):
    if len(l) > 0:
        l[0] = 0
    return l

d = [5, 12, 83]
set_first_elem_to_zero(d)
print(d)
# It prints out [0, 12, 83]
# The function changed the value that d[0] pointed at; it
# didn't make any change to the actual list.