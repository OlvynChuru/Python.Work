# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 21:30:34 2017

@author: Matthew Sokolovsky
"""
# (a)
print(float(123))
# It prints 123.0
# It converted the integer 123 to a float.

# (b)
print(float('123'))
# It prints 123.0
# It converted the string '123' to a float.

# (c)
print(float('123.23'))
# It prints 123.23
# It converted the string '123.23' to a float.

# (d)
print(int(123.23))
# It prints 123
# It converted the float 123.23 to an integer,
#  removing the fractional part.

# (e)
# print(int('123.23'))
# It causes an error:
#  ValueError: invalid literal for int() with base 10: '123.23'
# The string '123.23' needs two steps to be turned into an integer:
#  first it must be turned into a number, then it must be turned
#  into an integer. A single cast can only do one step. This is
#  why it causes an error.

# (f)
print(int(float('123.23')))
# It prints 123
# It converted the string '123.23' to a float 123.23
# Then it converted that float to an integer.

# (g)
print(str(12))
# It prints 12
# It converted the integer 12 to a string.
# The output is not in quotes, but I can show
#  that the str() function does indeed convert
#  numbers to strings. When I do the code below:
print(str(12) + str(12))
# It prints 1212
# That is something specific to strings.

# (h)
print(str(12.2))
# It prints 12.2
# It converted the float 12.2 to a string.

# (i)
print(bool('a'))
# It prints True
# I wasn't sure what to make of this when I
#  saw the output, so I did some more tests:
print(bool('False'))
# It prints True
print(bool('0'))
# It prints True
print(bool('\t'))
# It prints True
print(bool('\n'))
# It prints True
print(bool(''))
# It prints False

# My guess is that an empty string is the only string
#  that evaluates as False when turned into a boolean.

# (j)
print(bool(0))
# It prints False
# Maybe 0 is False and 1 is True? Let's test it.
print(bool(1))
# It prints True
# What about other numbers?
print(bool(2))
# It prints True
print(bool(-1))
# It prints True

# My guess is that all nonzero integers evaluate to True
#  when converted to a boolean.

# (k)
print(bool(0.1))
# It prints True
# I'm guessing that all nonzero floats are True as well.
# But let's just test one more thing.
print(bool(0.0))
# It prints False