from itertools import permutations

sk = input().split(" ")
s = list(sk[0])
k = int(sk[1])

s.sort()
result = list(permutations(s,k))

for string in result:
    print(string[0]+string[1])
