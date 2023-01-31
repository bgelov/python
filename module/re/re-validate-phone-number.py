# https://www.hackerrank.com/challenges/validating-the-phone-number/problem

regex_pattern = r"^[789]\d{9}$"    

import re

n = int(input())

for i in range(n):
    if (bool(re.match(regex_pattern, input()))):
        print("YES")
    else:
        print("NO")