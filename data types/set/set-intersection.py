n = int(input())
arr1 = set(map(int, input().split()))
b = int(input())
arr2 = set(map(int, input().split()))

arrIntersec = arr1.intersection(arr2)

print(len(arrIntersec))
