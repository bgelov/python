#https://www.hackerrank.com/challenges/np-inner-and-outer/problem

import numpy as np

A = np.array(input().split(), int)
B = np.array(input().split(), int)

print(np.inner(A,B))
print(np.outer(A,B))