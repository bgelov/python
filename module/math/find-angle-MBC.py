#Task:
#https://www.hackerrank.com/challenges/find-angle/problem

import math

AB = float(input())
BC = float(input())

a = AB
b = BC

#Solution 1, tangentF = a/b
result = round(math.degrees(math.atan(a/b)))

#Other ways
#AC = math.sqrt(pow(AB,2) + pow(BC,2))
AC = math.hypot(AB,BC)
c = AC

#Solution 2, sineF = a/c
result = round(math.degrees(math.asin(a/c)))

#Solution 3, cosineF = b/c
result = round(math.degrees(math.acos(b/c)))

#Solution 4. If we don't know about this:
#"In a right triangle, the length of the median drawn from the vertex of the right angle equals half the length of the triangle's hypotenuse" (MC = AC/2 and BM = MC)
#then solution more difficult:
cosF = b/c
q = math.sqrt(b*b + (c/2)*(c/2) - b*c*cosF)
cosA = (q*q + b*b - (c/2)*(c/2))/(2*q*b)
result = round(math.degrees(math.acos(cosA)))


print(result, end=chr(176))
