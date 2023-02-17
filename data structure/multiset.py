# Multiset realization

multiset_size = 10
multiset = [[] for _ in range(multiset_size)]

def add(x):
    # if need set (not multiset), we can add here checker if x already in set
    multiset[x % multiset_size].append(x)

def find(x):
    for now in multiset[x % multiset_size]:
        if now == x:
            return True
    return False

def delete(x):
    list_with_x = multiset[x % multiset_size]
    for i in range(len(list_with_x)):
        if list_with_x[i] == x:
            list_with_x[i] = list_with_x[len(list_with_x-1)]
            list_with_x.pop()
            return True

