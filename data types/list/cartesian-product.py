from itertools import product

list1 = list2 = ()
list1 = map(int, input().split(" "))
list2 = map(int, input().split(" "))

result = list(product(list1,list2))
for i in range(len(result)):
    print(result[i], end = ' ')
