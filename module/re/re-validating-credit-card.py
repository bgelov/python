#https://www.hackerrank.com/challenges/validating-credit-card-number/problem
import re
#https://docs.python.org/3/library/re.html

N = int(input())

for i in range(N):
    cardNum = str(input())
    checkStatus = "Valid"
    
#It must start with a 4, 5 or 6.
#It must contain exactly 16 digits.
#It must only consist of digits (0-9).
#It may have digits in groups of 4, separated by one hyphen "-".
#It must NOT use any other separator like ' ' , '_', etc.
    if "-" in cardNum:
        checkCard = re.match(r'^(?:([456]{1}\d{3}-\d{4}-\d{4}-\d{4}))$', cardNum)
#It must NOT have 4 or more consecutive repeated digits.
        cardNumWithoutSpec = cardNum.replace('-','')
        checkRepeatedNum = re.search(r'([0-9])\1\1\1', cardNumWithoutSpec)
        if checkRepeatedNum: checkStatus = "Invalid"
    else:
        checkCard = re.match(r'^(?:([456]{1}\d{15}))$', cardNum)
    if not checkCard: checkStatus = "Invalid"

    
    print(checkStatus)