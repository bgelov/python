import re

T = int(input())
for i in range(T):
    S = input()
    try:
        pattern = re.compile(S)
        print("True")
    except:
        print("False")
