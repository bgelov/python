T = int(input())
for i in range(T):
    setALen = int(input())
    setA = set(map(int,input().split()))
    setBLen = int(input())
    setB = set(map(int,input().split()))
    print(setA.issubset(setB))
