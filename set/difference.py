n = int(input())
arr1 = set(map(int, input().split()))
b = int(input())
arr2 = set(map(int, input().split()))

arrDiff = arr1.difference(arr2)

print(len(arrDiff))
