from itertools import combinations_with_replacement

sk = input().split(" ")
s = list(sk[0])
k = int(sk[1])
result = []

s.sort()
result = list(combinations_with_replacement(s,k))

for string in result:
    print("".join(string))
