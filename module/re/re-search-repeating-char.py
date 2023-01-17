import re

S = str(input())
resultSearch = re.search(r"([a-zA-Z0-9])\1",S)
print(resultSearch.group()[0]) if resultSearch else print(-1)
