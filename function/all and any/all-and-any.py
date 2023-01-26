#https://www.hackerrank.com/challenges/any-or-all/problem

_ = input()
arr = list(map(int, input().split()))

allPositive = True
isPalindromic = False
for a in arr:
    if a<0: allPositive = False
    if (str(a)==str(a)[::-1]): isPalindromic = True

if allPositive==True and isPalindromic==True:
    print(True)
else:
    print(False)
    
any(a == a[::-1] for a in arr)


#-------

_, arr = input(), input().split()
result1 = all(int(a)>0 for a in arr)
result2 = any(a == a[::-1] for a in arr)
print(all([result1, result2]))


#-------


_, arr = input(), input().split()
result = all([all(int(a)>0 for a in arr), any(a == a[::-1] for a in arr)])
print(result)