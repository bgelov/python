# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/description/
# Oleg Belov

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return arr[0]
        elif n == 2:
            return arr[0]+arr[1]
        summa = sum(arr)
        if n % 2 != 0:
            summa *= 2
        for i in range(n):
            for j in range(3,n,2):
                if j+i<= n:
                    summa += sum(arr[i:i+j])
        return summa