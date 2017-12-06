# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 22:06:31 2017

@author: Matthew Sokolovsky
"""

print(range(5))
# It prints range(0, 5)

print(type(range(5)))
# It prints <class 'range'>

for i in range(5):
    print('oogleblah')
# It prints
#  oogleblah
#  oogleblah
#  oogleblah
#  oogleblah
#  oogleblah
    
# The parameter is the number of times to iterate.
# The number to start at is 0 by default,
#  hence range(5) printing out range(0, 5)
    
# If you put two parameters:
for i in range(1, 5):
    print('oogleblah')
# It prints
#  oogleblah
#  oogleblah
#  oogleblah
#  oogleblah
    
# The first parameter is the starting number;
#  the second parameter is the ending number.
# It is identical to the Java for loop:
#  for (int i = 1; i < 5; i++)
#      System.out.println("oogleblah");

# If you put three parameters:
for i in range(0, 5, 2):
    print('oogleblah')
# It prints
#  oogleblah
#  oogleblah
#  oogleblah
    
# The third parameter is the amount to increment i
#  after each iteration.
# It is identical to the Java for loop:
#  for (int i = 0; i < 5; i += 2)
#      System.out.println("oogleblah");