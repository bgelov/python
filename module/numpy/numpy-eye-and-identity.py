#https://www.hackerrank.com/challenges/np-eye-and-identity/problem

import numpy as np

np.set_printoptions(legacy='1.13')

nm = list(map(int, input().split()))

print(np.eye(nm[0],nm[1]))