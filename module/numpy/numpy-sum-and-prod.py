#https://www.hackerrank.com/challenges/np-sum-and-prod/problem

import numpy as np

nm = list(map(int, input().split()))
arr = np.array([input().split() for _ in range(nm[0])], int)

sumArr = np.sum(arr, axis = 0)
print(np.prod(sumArr))