#https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

from collections import namedtuple
n = int(input())
student = namedtuple('student', input())
resultSum = 0
for i in range(n):
    st = input().split()
    studentClass = student(*st)
    resultSum += int(studentClass.MARKS)
result = resultSum/n
print(result)