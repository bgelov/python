#https://www.hackerrank.com/challenges/np-zeros-and-ones/problem

import numpy as np

nmp = list(map(int, input().split()))

print(np.zeros(nmp,dtype=int))
print(np.ones(nmp,dtype=int))