# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 19:26:41 2017

@author: Matthew Sokolovsky
"""
# (a)
# I figured that you don't wan't me to
#  just print out the list; that would be
#  to easy. I wasn't sure of the format you
#  expected of the output, though. The
#  function below prints out the elements on
#  one line with no brackets or commas.
def print_list(lis):
    lis_str = ''
    for i in lis:
        lis_str += str(i)
        lis_str += ' '
    print(lis_str)

print_list([])
print_list([4, 5, 8, 2])

# (b)
# I realized I could also just do lis.reverse(),
#  but I was worried you would take off points
#  for such a lazy answer.
def print_list_reverse(lis):
    lisr = []
    for i in lis:
        lisr.insert(0, i)
    print_list(lisr)

print_list_reverse([])
print_list_reverse([4, 5, 8, 2])

def list_length(lis):
    count = 0
    for i in lis:
        count += 1
        
    return count

print(list_length([]))
print(list_length(['a', 'b']))