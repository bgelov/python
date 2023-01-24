#https://www.hackerrank.com/challenges/py-collections-deque/problem

from collections import deque
#https://docs.python.org/3/library/collections.html#deque-objects

deqCollect = deque()

n = int(input())

for i in range(n):
    command = input().split()
    if command[0] == "append":
        deqCollect.append(command[1])
    elif command[0] == "appendleft":
        deqCollect.appendleft(command[1])
    elif command[0] == "pop":
        deqCollect.pop()
    elif command[0] == "popleft":
        deqCollect.popleft()

[print(x, end=" ") for x in deqCollect]