#https://www.hackerrank.com/challenges/np-array-mathematics/problem

import numpy as np

nm = list(map(int, input().split()))
A = np.array([input().split() for _ in range(nm[0])], int)
B = np.array([input().split() for _ in range(nm[0])], int)

print(np.add(A,B))
print(np.subtract(A,B))
print(np.multiply(A,B))
print(np.floor_divide(A,B))
print(np.mod(A,B))
print(np.power(A,B))