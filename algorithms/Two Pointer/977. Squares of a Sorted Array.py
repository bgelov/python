# https://leetcode.com/problems/squares-of-a-sorted-array
# Oleg Belov

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        low = 0
        high = n-1
        index = n-1
        ans = [None] * n 
        while high > -1 and index > -1:
            if abs(nums[low]) > abs(nums[high]):
                ans[index] = nums[low]*nums[low]
                low += 1
            else:
                ans[index] = nums[high]*nums[high]
                high -= 1
            index -=1
        return ans