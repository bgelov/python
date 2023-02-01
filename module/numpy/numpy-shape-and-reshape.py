#https://www.hackerrank.com/challenges/np-shape-reshape/problem

import numpy as np


arr = np.array(input().split(), int)
arr.shape = (3,3)
print(arr)

