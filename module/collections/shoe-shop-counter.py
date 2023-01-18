from collections import Counter

x = int(input())
shoeSizes = map(int, input().split())
numCustomers = int(input())

shoeInStore = Counter(shoeSizes)
moneyEarned = 0

for i in range(numCustomers):
    shoePursch,price = map(int, input().split())
    if shoeInStore[shoePursch] > 0:
        shoeInStore[shoePursch] -= 1
        moneyEarned += price
        
print(moneyEarned)