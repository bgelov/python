# https://leetcode.com/problems/n-th-tribonacci-number
# Oleg Belov

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        elif n == 1 or n == 2: return 1
        dp = [0] * (n+1)
        dp[0],dp[1],dp[2] = 0,1,1
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        return dp[n]