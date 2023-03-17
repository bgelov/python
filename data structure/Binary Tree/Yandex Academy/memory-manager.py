# https://www.youtube.com/watch?v=lEJzqHgyels
# Тренировки по алгоритмам от Яндекса. Лекция 8: «Деревья»

def initmemory(maxn):
    memory = []
    for i in range(maxn):
        memory.append([0, i+1, 0])
    return [memory, 0]

def newnode(memstruct):
    memory, firstfree = memstruct
    memstruct[1] = memory[firstfree][1]
    return firstfree

def delnode(memstruct, index):
    memory, firstfree = memstruct
    memory[index][1] = firstfree
    memstruct[1] = index


def find(memstruct, root, x):
    key = memstruct[0][root][0]
    if x == key:
        return root
    elif x < key:
        left = memstruct[0][root][1]
        if left == -1:
            return -1
        else:
            return find(memstruct, left, x)
    elif x > key:
        right = memstruct[0][root][2]
        if right == -1:
            return -1
        else:
            return find(memstruct, right, x)
        

def createandfillnode(memstruct, key):
    index = newnode(memstruct)
    memstruct[0][index][0] = key
    memstruct[0][index][1] = -1
    memstruct[0][index][2] = -1
    return index

def add(memstruct, root, x):
    key = memstruct[0][root][0]
    if x < key:
        left = memstruct[0][root][1]
        if left == -1:
            memstruct[0][root][1] = createandfillnode(memstruct, x)
        else:
            add(memstruct, left, x)
    elif x > key:
        right = memstruct[0][root][2]
        if right == -1:
            memstruct[0][root][2] = createandfillnode(memstruct, x)
        else:
            add(memstruct, right, x)
    

memstruct = initmemory(20)
root = createandfillnode(memstruct, 8)
add(memstruct, root, 10)
add(memstruct, root, 9)
add(memstruct, root, 14)
add(memstruct, root, 13)
add(memstruct, root, 3)
add(memstruct, root, 1)
add(memstruct, root, 6)
add(memstruct, root, 4)
add(memstruct, root, 7)