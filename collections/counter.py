from collections import Counter

k = int(input())
roomNum = list(map(int,input().split()))

roomNumCounter = Counter(roomNum)
result = min(roomNumCounter, key=roomNumCounter.get)
print(result)

# print(roomNumCounter[result])
