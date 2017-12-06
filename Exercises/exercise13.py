# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 09:28:54 2017

@author: Matthew Sokolovsky
"""

# This program is a mess, and it doesn't account for all of the address syntax rules.

def in_list(char, char_list):
    if char_list.count(char) > 0:
        return True
    else:
        return False

# I check if a char is a valid char by looking it up in one of these lists.
localchar = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&\'*+-/=?^_`{|}~.'
quotechar = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&\'*+-/=?^_`{|}~.\"(),:;<>@[]\\'
domainchar = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-.'
whitespace = ' \n\t'

file = open("emails.txt", "r") # Replace with the file of your choice.
nextchar = None
address = ''

def valid_address(addre):
    if len(addre) < 5 or len(addre) > 320:
        return False
    
    quotemode = False
    plusmode = False
    hasamp = False
    hasdot = False
    DONOTHING = None
    i = 0
    while i < len(addre) and not(hasamp):
        if addre[i] == '@' and not(quotemode):
                hasamp = True
                plusmode = False
        elif plusmode:
            DONOTHING
        elif addre[i] == '\"' and not(hasamp):
            quotemode = not(quotemode)
        elif addre[i] == '+' and not(quotemode) and not(hasamp):
            plusmode = True
        elif in_list(addre[i], localchar):
            DONOTHING
        elif quotemode and in_list(addre[i], quotechar):
            DONOTHING
        else:
            return False
        i += 1
            
    if not(hasamp) or i > 64 or len(addre) - i > 255:
        return False
    
    while i < len(addre):
        if addre[i] == '.':
            hasdot = True
        if not in_list(addre[i], domainchar):
            return False
        i += 1
    
    if not(hasdot):
        return False
    
    return True
        
        


while nextchar != '':

    nextchar = file.read(1)
    if not in_list(nextchar, whitespace): # If nextchar is not whitespace
        address += nextchar
    else:
        if valid_address(address):
            print(address)
        address = ''
file.close()