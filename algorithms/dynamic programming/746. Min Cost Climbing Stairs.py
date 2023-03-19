# https://leetcode.com/problems/min-cost-climbing-stairs/description/
# Oleg Belov

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost)+1)
        dp[0] = 0
        dp[1] = cost[0]
        for i in range(2,len(cost)+1):
            dp[i] = cost[i-1] + min(dp[i-1],dp[i-2])
        return min(dp[-1],dp[-2])