setA = set(map(int,input().split()))
countSets = int(input())

result = True
for i in range(countSets):
    setB = set(map(int,input().split()))
    result = setA.issuperset(setB)
    if (result == False): break

print(result)
