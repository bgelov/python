happiness = 0

nCount,mCount = map(int, input().split())
arrN = list(map(int, input().split()))
arrA = set(map(int, input().split()))
arrB = set(map(int, input().split()))

for N in arrN:
    if N in arrA: happiness += 1
    if N in arrB: happiness -= 1

print(happiness)
