# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/
# Oleg Belov

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) > 2:
            for i in range(len(nums)-1,1,-1):
                if nums[i] == nums[i-1] and nums[i] == nums[i-2]:
                    nums.pop(i)
            return len(nums)
        else:
            return 2