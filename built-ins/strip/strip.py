#https://www.hackerrank.com/challenges/re-findall-re-finditer/problem

import re
s = str(input())
s = s.strip("AEIOUaeiou")
result = re.findall(r"[AEIOUaeiou]{2,}",s)
if not result:
    print(-1)
else:
    [print(r) for r in result]