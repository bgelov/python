#https://www.hackerrank.com/challenges/np-dot-and-cross/problem

import numpy as np

#https://numpy.org/doc/stable/reference/generated/numpy.dot.html

#np.dot(array a, array b): returns the scalar or dot product of two arrays
#np.matmul(array a, array b): returns the matrix product of two arrays
#np.multiply(array a, array b): returns the element-wise matrix multiplication of two arrays

n = int(input())

A = np.array([input().split() for _ in range(n)], int)
B = np.array([input().split() for _ in range(n)], int)

print(np.dot(A,B))
