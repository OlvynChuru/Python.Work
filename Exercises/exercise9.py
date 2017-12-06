# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 20:48:52 2017

@author: Matthew Sokolovsky
"""
# This was easier than I expected.
def flatten_table(table):
    lis = []
    for i in table:
        for j in i:
            lis.append(j)
    return lis

print(flatten_table([[0, 9], ['a', 'z']]))