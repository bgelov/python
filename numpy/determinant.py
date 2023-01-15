import numpy as np

n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(float, input().split())))
    
matrix = np.matrix(arr)
result = np.linalg.det(matrix)
print(round(result,2))
