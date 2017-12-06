# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 21:08:18 2017

@author: Matthew Sokolovsky
"""
# (a)
# print(2000.3 ** 200)
# This calculation causes an overflow error
#  because the result is too big to fit in a variable.

# However, it also had to do with the fact that a
#  floating point (2000.3) was used.
# When I do the code below:
print(2000 ** 200)
# it does not cause an error; instead, it prints out
#  a really big number.

# (b)
print(1.0 + 1.0 - 1.0)
# This prints out 1.0
#  which is what I expected.

# (c)
print(1.0 + 1.0e20 - 1.0e20)
# This prints out 0.0
#  which is NOT what I expected.
# The 1.0 seems to be rounded off because it is
#  so miniscule compared to the number it's being
#  added to (like significant figures in science).

# I did some experiments below to see exactly
#  how the rounding off works.

print(1.0 + 1.0e15)
# This does not round off the 1.0
print(1.0 + 1.0e16)
# This DOES round off the 1.0
print(10.0 + 1.0e16)
# This does not round off the 10.0

# My conclusion is that the smaller number gets
#  rounded off if it is at least 16 orders of magnitude
#  smaller than the larger number.