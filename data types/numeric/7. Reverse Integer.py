# https://leetcode.com/problems/reverse-integer/description/
# Oleg Belov

class Solution:
    def reverse(self, x: int) -> int:
        new_num = 0
        num = abs(x)
        while num > 0:
            new_num += num % 10
            new_num = new_num * 10
            num = num // 10
        new_num = new_num // 10
        if x < 0:
            new_num = -new_num
        if new_num > -2**31 and new_num < 2**31 - 1:
            return new_num
        else:
            return 0