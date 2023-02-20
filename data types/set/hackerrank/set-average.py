def average(array):
    setArray = list(set(array))
    result = sum(setArray) / len(setArray)
    return result


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
