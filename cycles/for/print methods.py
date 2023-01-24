from collections import OrderedDict

orderDict = OrderedDict([
    ('Test1', '1'),
    ('Test2', '2'),
    ('Test3', '3')
])

#Method 1
for key, val in orderDict.items():
    print(key, val)

#Method 2
[print(key,val) for key,val in orderDict.items()]