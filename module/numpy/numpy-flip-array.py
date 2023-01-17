import numpy

def arrays(arr):
    npArr = numpy.array(arr,float)
    return numpy.flip(npArr)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)