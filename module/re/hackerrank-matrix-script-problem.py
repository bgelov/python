#https://www.hackerrank.com/challenges/matrix-script/problem

#!/bin/python3

import math
import os
import random
import re
import sys


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

string = ""
for i in range(m):
    for j in range(n):
        string += (matrix[j][i])
 
string = re.sub(r"\b\W+\b", " ", string)

#very clean string
#string = re.sub(r"[\W]", " ", string)
#string = re.sub(r" +", " ", string)
#but not for this task

#one bad testcase:
#string = re.sub(r"(\w*?)\W+(\w\W*?)", r"\1 \2", string)

print(string)