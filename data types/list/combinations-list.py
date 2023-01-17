from itertools import combinations

sk = input().split(" ")
s = list(sk[0])
k = int(sk[1])
result = []

s.sort()
for i in range(1,k+1):
    result += list(combinations(s,i))

for string in result:
    print("".join(string))
