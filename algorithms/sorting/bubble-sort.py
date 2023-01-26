#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

allNumSwaps = 0
numSwaps = 0

for j in range(n-1):
    numSwaps = 0
    for i in range(n-1):
        numI = a[i]
        numNext = a[i+1]
        if numI>numNext:
            a[i] = numNext
            a[i+1] = numI
            allNumSwaps += 1
            numSwaps +=1
    if numSwaps == 0:
        break      
 
print(f"Array is sorted in {allNumSwaps} swaps.")
print(f"First Element: {a[0]}")
print(f"Last Element: {a[-1]}")