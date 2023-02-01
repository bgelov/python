#https://www.hackerrank.com/challenges/np-concatenate/problem

import numpy as np

nmp = list(map(int, input().split()))
A = np.array([input().split() for _ in range(nmp[0])], int)
B = np.array([input().split() for _ in range(nmp[1])], int)

print(np.concatenate((A,B), axis=0))