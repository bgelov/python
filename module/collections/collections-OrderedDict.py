#https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
from collections import OrderedDict

N = int(input())

orderDict = OrderedDict()

for i in range(N):
    item_name, net_price = input().rsplit(" ", maxsplit=1)
    if item_name not in orderDict:
        orderDict[item_name] = int(net_price)
    else:
        orderDict[item_name] += int(net_price)
        
for key, val in orderDict.items():
    print(key, val)