#!/bin/python3
from collections import Counter

if __name__ == '__main__':
    s = input()
    
listOfChars = list()
listOfChars.extend(s)
listOfChars.sort()

charCount = Counter(listOfChars).most_common(3)
for char in charCount:
    print(f"{char[0]} {char[1]}")