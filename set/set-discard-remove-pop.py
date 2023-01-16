n = int(input())
s = set(map(int, input().split()))
operationsCount = int(input())

for i in range(operationsCount):
    arg = input().split()
    if arg[0] == 'pop':
        s.pop()
    elif arg[0] == 'remove':
        s.remove(int(arg[1]))
    elif arg[0] == 'discard':
        s.discard(int(arg[1]))
          
print(sum(s))
