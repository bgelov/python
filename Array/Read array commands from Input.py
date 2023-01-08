if __name__ == '__main__':
    N = int(input())
    myList = []
    
    
for i in range(N):
    inputString = input()
    arg = inputString.split(' ')
    if arg[0] == 'insert':
        myList.insert(int(arg[1]),int(arg[2]))
    elif arg[0] == 'print':
        print(myList)
    elif arg[0] == 'remove':
        myList.remove(int(arg[1]))
    elif arg[0] == 'append':
        myList.append(int(arg[1]))
    elif arg[0] == 'sort':
        myList.sort()
    elif arg[0] == 'pop':
        myList.pop()
    elif arg[0] == 'reverse':
        myList.reverse()

        
