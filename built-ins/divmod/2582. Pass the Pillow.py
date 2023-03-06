#https://leetcode.com/problems/pass-the-pillow/description/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        #Returns a tuple (quotient, remainder) by calculating (number1 // number2, number1 % number2).
        q, r = divmod(time, n-1)
        if q%2 == 0:
            return r+1
        else:
            return n-r
            
            
# or 

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        result = 1
        trigger = 0 

        for i in range(0,time):
            if trigger == 0:
               result = result + 1
            elif trigger == 1:
                result = result - 1
            if result == n or result == 1:
                if trigger == 1:
                    trigger = 0
                elif trigger == 0:
                    trigger = 1 
        return result