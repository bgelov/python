#https://leetcode.com/problems/pass-the-pillow/description/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        #Returns a tuple (quotient, remainder) by calculating (number1 // number2, number1 % number2).
        q, r = divmod(time, n-1)
        if q%2 == 0:
            return r+1
        else:
            return n-r