#https://www.hackerrank.com/challenges/maximize-it/problem

from itertools import product

K, M = map(int, input().split())
arr = []
for _ in range(K):
    inputN = input().split(" ", maxsplit=1)
    N = inputN[0]
    arr.append(list(map(lambda x : int(x)**2, inputN[1].split())))
#print(arr)
  
sum_arr = list(map(sum, list(product(*arr))))
#print(sum_arr)

result = 0
for maxSum in sum_arr:
    maxSumM = maxSum % M
    if (maxSumM > result):
        result = maxSumM
print(result)
