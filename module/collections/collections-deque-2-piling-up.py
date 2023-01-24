#https://www.hackerrank.com/challenges/piling-up/problem

from collections import deque
#https://docs.python.org/3/library/collections.html#deque-objects

for _ in range(int(input())):

    n = int(input())
    sideLengths = deque(map(int, input().split()))

    while sideLengths:
    
        if sideLengths[0] >= sideLengths[-1]:
            topBlock = sideLengths.popleft()
        else:
            topBlock = sideLengths.pop()
        
        if len(sideLengths) == 0:
            status = "Yes"
            break
        if (topBlock < sideLengths[0]) or (topBlock < sideLengths[-1]):
            status = "No"
            break
        
    print(status)