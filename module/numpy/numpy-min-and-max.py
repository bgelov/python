#https://www.hackerrank.com/challenges/np-min-and-max/problem

import numpy as np

nm = list(map(int, input().split()))
arr = np.array([input().split() for _ in range(nm[0])], int)

print(max(np.min(arr, axis=1)))