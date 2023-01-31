# https://www.hackerrank.com/challenges/hex-color-code/problem

import re

n = int(input())

regex_pattern = re.compile(r"(\#[a-fA-F0-9]{3,6})")
trigger = False

for i in range(n):
    
    string = input()
    
    #check if start css prop
    if re.search(r"\{", string):
        trigger = True
        #if ID { and color on one string
        string = string[re.search(r"\{", string).span()[0]:]
    #check if end css prop
    if re.search(r"\}", string):
        trigger = False
        
    if trigger == True:
        match = re.findall(regex_pattern, string)
        if match:
            for m in match:
                print(m) 