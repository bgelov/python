# https://leetcode.com/problems/climbing-stairs/
# Oleg Belov

class Solution:
    def climbStairs(self, n: int) -> int:
        if n in [1,2]:
            return n
        else:
            dp = [0] * (n + 1)
            dp[1] = 1
            dp[2] = 2
            for i in range(3,n+1):
                dp[i] = dp[i-1] + dp[i-2]
            return dp[n]