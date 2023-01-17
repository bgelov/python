m = int(input())
arrM = set(map(int, input().split()))
n = int(input())
arrN = set(map(int, input().split()))

result = []
result += list(arrM.difference(arrN))
result += list(arrN.difference(arrM))
result.sort()

for res in result:
    print(res)
