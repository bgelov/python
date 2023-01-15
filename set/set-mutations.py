n = int(input())
arr1 = set(map(int, input().split()))
operationsCount = int(input())

for i in range(operationsCount):
    inputString = input()
    arg = inputString.split(' ')
    arr2 = set(map(int, input().split()))
    if arg[0] == 'intersection_update':
        arr1.intersection_update(arr2)
    elif arg[0] == 'update':
        arr1.update(arr2)
    elif arg[0] == 'symmetric_difference_update':
        arr1.symmetric_difference_update(arr2)
    elif arg[0] == 'difference_update':
        arr1.difference_update(arr2)
          
print(sum(arr1))

