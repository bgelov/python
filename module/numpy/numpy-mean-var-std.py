#https://www.hackerrank.com/challenges/np-mean-var-and-std/problem

import numpy

n,m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
        
npArr = numpy.array(arr)

print(numpy.mean(npArr,axis=1))
print(numpy.var(npArr,axis=0))
print(round(numpy.std(npArr,axis=None),11))

