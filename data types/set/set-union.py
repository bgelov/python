n = int(input())
arr1 = set(map(int, input().split()))
b = int(input())
arr2 = set(map(int, input().split()))

arrUnion = arr1.union(arr2)

print(len(arrUnion))
