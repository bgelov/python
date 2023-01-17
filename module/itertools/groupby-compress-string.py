from itertools import groupby

s = str(input())

for k,c in groupby(s):
    print(f"({len(list(c))}, {k})", end = " ")
