#https://www.hackerrank.com/challenges/re-sub-regex-substitution

import re

n = int(input())
trigger = True
pattern1 = re.compile(r"\s\&\&\s")
pattern2 = re.compile(r"\s\|\|\s")

for i in range(n):
    string = str(input())
    if (re.search(pattern1,string)) or (re.search(pattern2,string)):
        trigger = True
    while trigger == True:
        string = re.sub(pattern1," and ",string)
        string = re.sub(pattern2," or ",string)
        if (re.search(pattern1,string)) or (re.search(pattern2,string)):
            trigger = True
        else:
            trigger = False
    print(string)
