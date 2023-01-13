from itertools import combinations

n = int(input())
s = input().split(" ")
k = int(input())

countA = 0

CombList = list(combinations(s, k))
for comb in CombList:
    if ("a" in comb): countA += 1

result = countA / len(CombList)
print(result)

