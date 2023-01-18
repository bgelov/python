#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

sumArr = []
    
for i in range(4):
    for j in range(4):
        a = arr[i][j]
        b = arr[i][j+1]
        c = arr[i][j+2]
        d = arr[i+1][j+1]
        e = arr[i+2][j]
        f = arr[i+2][j+1]
        g = arr[i+2][j+2]
        sumArr.append(a+b+c+d+e+f+g)
    
print(max(sumArr))
