#https://www.hackerrank.com/challenges/zipped/problem

n,x = map(int, input().split())

subjectMarks = []

for i in range(x):
    sMarks = ()
    sMarks = list(map(float, input().split()))
    subjectMarks.append(sMarks)

studentMarks = list(zip(*subjectMarks))
for sMarks in studentMarks:
    print(sum(sMarks)/x)