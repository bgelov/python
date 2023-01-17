#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    
arr.reverse()
for i in range(n):
    print(arr[i], end = " ")
