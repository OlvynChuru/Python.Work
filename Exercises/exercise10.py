# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 21:04:31 2017

@author: Matthew Sokolovsky
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 2, .001)
y = (np.sin(x - 2) ** 2) * (np.e ** (-1 * (x ** 2)))
plt.title("Exercise 1")
plt.xlabel("x")
plt.ylabel("(sin(x - 2))^2 * e^(-x^2)")

plt.plot(x, y)