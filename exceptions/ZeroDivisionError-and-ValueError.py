#https://www.hackerrank.com/challenges/exceptions/problem
T = int(input())
for i in range(T):
    try:
        a,b = map(int, input().split())
        print(a//b)
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as e:
        print("Error Code:",e)