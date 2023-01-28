#https://www.hackerrank.com/challenges/introduction-to-regex/problem

import re

t = int(input())

# verify that N is a floating point number in "+-num.num" format
for n in range(t):
    n = input()
    print(bool(re.match(r"^[+-]?\d*\.\d*$",n)))