#https://www.hackerrank.com/challenges/ginorts/problem

s = str(input())

lowercase = []
uppercase = []
oddDigit = []
evenDigit = []
for i in s:
    if i.islower(): lowercase.append(i)
    if i.isupper(): uppercase.append(i)
    if i.isnumeric():
        if int(i)%2 == 0:
            evenDigit.append(i)
        else:
            oddDigit.append(i)

lowercase.sort()
uppercase.sort()
oddDigit.sort()
evenDigit.sort()

print("".join(lowercase+uppercase+oddDigit+evenDigit))