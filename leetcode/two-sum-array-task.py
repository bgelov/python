#https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            firstNum = target - nums[i]
            if firstNum in nums:
                if nums.index(firstNum) != i:
                    result.append(i)
                    result.append(nums.index(firstNum))
                    break
        return result 
                