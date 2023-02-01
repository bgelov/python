#https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem

import numpy as np

nm = list(map(int, input().split()))
arr = np.array([input().split() for _ in range(nm[0])], int)

print(np.transpose(arr))
print(arr.flatten())