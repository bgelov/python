class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        import re
        regex_pattern = re.compile(r"^(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$")	
        romanNum = re.findall(regex_pattern, s)
        for num in romanNum[0]:

            if num=="I" : result +=1
            elif num=="II" : result +=2
            elif num=="III" : result +=3
            elif num=="IV" : result +=4
            elif num=="V" : result +=5
            elif num=="VI" : result +=6
            elif num=="VII" : result +=7
            elif num=="VIII" : result +=8
            elif num=="IX" : result +=9

            if num=="X" : result +=10
            elif num=="XX" : result +=20
            elif num=="XXX" : result +=30
            elif num=="XL" : result +=40
            elif num=="L" : result +=50
            elif num=="LX" : result +=60
            elif num=="LXX" : result +=70
            elif num=="LXXX" : result +=80
            elif num=="XC" : result +=90

            if num=="C" : result +=100
            elif num=="CC" : result +=200
            elif num=="CCC" : result +=300
            elif num=="CD" : result +=400
            elif num=="D" : result +=500
            elif num=="DC" : result +=600
            elif num=="DCC" : result +=700
            elif num=="DCCC" : result +=800
            elif num=="CM" : result +=900

            if num=="M" : result +=1000
            elif num=="MM" : result +=2000
            elif num=="MMM" : result +=3000

        return result