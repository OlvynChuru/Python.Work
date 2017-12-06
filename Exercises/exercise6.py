# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 13:24:39 2017

@author: Matthew Sokolovsky
"""
# (a)
def is_prime(n):
    if type(n) != int or n < 2:
        return False
    for i in range(2, n): # This gets skipped if n == 2
        if n % i == 0:
            return False
    # If it hasn't returned False yet, n is prime.
    return True

print(is_prime(1))
print(is_prime(2))
print(is_prime(3))
print(is_prime(4))
print(is_prime(3.5))

# (b)
# The code for part b is kind of awkward because it has
#  to increment i by varying amounts while iterating.
def is_prime_b(n):
    if type(n) != int or n < 2:
        return False
    elif n == 2 or n == 3:
        return True
    elif (n+1) % 6 != 0 or (n-1) % 6 != 0: # Checks if n is not of the form 6x +- 1
        return False
    
    i = 5
    while i < n: # This gets skipped if n == 2
        if n % i == 0:
            return False
        i += 2
        if i < n:
            if n % i == 0:
                return False
        i += 4
    # If it hasn't returned False yet, n is prime.
    return True

# (c)
# The idea of my code in (c) and (d) is that I can
#  use a list of primes to find out whether the
#  next number is prime. If it's prime, then I add
#  it to the list.
    
# However, my code still feels a bit too complicated.
    
def all_primes_up_to(n): # I interpret this as all primes < n
    prime_list = []
    n = int(n)
    if n > 2:
        prime_list.append(2)
    
    def is_prime_c(n):
        for index in range(len(prime_list)):
            if n % prime_list[index] == 0:
                return False
        return True

    for i in range(3, n, 2):
        if is_prime_c(i):
            prime_list.append(i)
    
    return prime_list


print(all_primes_up_to(2))
print(all_primes_up_to(3))
print(all_primes_up_to(11))
print(all_primes_up_to(128))

# (d)
def list_primes(n):
    prime_list = []
    n = int(n)
    count = 0
    if n > 0:
        prime_list.append(2)
        count += 1
    
    def is_prime_c(n):
        for index in range(len(prime_list)):
            if n % prime_list[index] == 0:
                return False
        return True
    
    i = 3
    while count < n:
        if is_prime_c(i):
            prime_list.append(i)
            count += 1
        i += 2
    return prime_list

print(list_primes(5))
print(list_primes(0))
print(list_primes(1))