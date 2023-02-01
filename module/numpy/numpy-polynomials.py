#https://www.hackerrank.com/challenges/np-polynomials/problem

import numpy as np

#https://numpy.org/doc/stable/reference/generated/numpy.polyval.html#numpy.polyval

p = list(map(float, input().split()))
x = int(input())

print(np.polyval(p, x))