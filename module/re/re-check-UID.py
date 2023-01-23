#https://www.hackerrank.com/challenges/validating-uid/problem
import re
#https://docs.python.org/3/library/re.html

T = int(input())

for i in range(T):
    uid = str(input())
    checkStatus = "Valid"
    
    #There must be exactly 10 characters in a valid UID.
    #It should only contain alphanumeric characters (a-z,A-Z&0-9).
    #No character should repeat.
    checkAlNum = re.match(r'^(?:([0-9a-zA-Z])(?!.*\1)){10}$', uid)
    if not checkAlNum: checkStatus = "Invalid"
        
    #or use for check alnum and len:
    #checkAlNum = re.match(r'^[0-9a-zA-Z]{10}$', uid)
    #and No character should repeat with Counter (from collections import Counter)
    #checkCharCount = Counter(uid)
    #for char,count  in checkCharCount.items():
    #    if (count > 1): checkStatus = "Invalid"
        
    #It must contain at least  digits (0-9).
    checkNumCount = re.findall('[0-9]', uid)
    if len(checkNumCount) < 3: checkStatus = "Invalid"
    #or
    #checkNumCount = re.match(r'^(.*?[0-9]){3,}.*$', uid)
    #if not checkNumCount: checkStatus = "Invalid"
    
    #It must contain at least 2 uppercase English alphabet characters.
    checkAZCount = re.findall('[A-Z]', uid)
    if len(checkAZCount) < 2: checkStatus = "Invalid"
    #or
    #checkAZCount = re.match(r'^(.*?[A-Z]){2,}.*$', uid)
    #if not checkAZCount: checkStatus = "Invalid"
    
    #in one string all re rules: ^(?=(?:[a-z\d]*[A-Z]){2})(?=(?:\D*\d){3})(?:([a-zA-Z\d])(?!.*\1)){10}$

    print(checkStatus)
    