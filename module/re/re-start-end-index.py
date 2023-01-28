#https://www.hackerrank.com/challenges/re-start-re-end/problem

import re

string = str(input())
substring = str(input())

regexpStr = re.compile(substring)

if regexpStr.search(string):
    i = 0
    substringLen = len(substring)
    while i < len(string) - substringLen:
        searchSubstring = regexpStr.search(string[i:])
        startIndex = searchSubstring.start()+i
        endIndex = searchSubstring.end()+i-1
        print(f"({startIndex}, {endIndex})")
        if (substringLen!=1):
            i = endIndex
        else:
            i = endIndex+1
else:
    print("(-1, -1)")
    

