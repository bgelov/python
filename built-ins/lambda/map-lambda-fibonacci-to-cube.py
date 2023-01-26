# num to cube
cube = lambda x: pow(x,3)

def fibonacci(n):
    # return a list of fibonacci numbers
    arr = []
    if n == 0 : return arr
    arr.append(0)
    if n == 1 : return arr
    arr.append(1)
    if n == 2 : return arr
    arr.append(1)
    if n == 3 : return arr
    for i in range(len(arr),n):
        arr.append(arr[i-1]+arr[i-2])
    return arr


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))