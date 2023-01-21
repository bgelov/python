#https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

from collections import defaultdict

n,m = map(int, input().split())

d = defaultdict(list)
r = defaultdict(list)

for i in range(n):
    d['A'].append(input())
for i in range(m):
    d['B'].append(input())

for i in d['B']:
    if i in d['A']:
        for j in range(len(d['A'])):
            if i == d['A'][j]:
                print(j+1, end = " ")
        print()
    else:
        print(-1)