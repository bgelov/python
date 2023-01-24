#https://www.hackerrank.com/challenges/word-order/problem

#https://docs.python.org/3/library/collections.html
from collections import Counter

n = int(input())

wordsArr = []

for i in range(n):
    wordsArr.append(input())
    
wCount = Counter(wordsArr)

print(len(list(wCount)))

[print(wCount[i], end = ' ') for i in wCount]