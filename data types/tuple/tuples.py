#Кортежи
n = int(input())
arr_t = str(input())
t = tuple(list(map(int, arr_t.split())))
print(hash(t))
