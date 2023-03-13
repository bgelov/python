# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/
# Oleg Belov

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        # 0 <= nums[i] <= 100
        counterSort = [0] * 101
        for num in nums:
            counterSort[num] += 1
        
        result = []
        for num in nums:
            result.append(sum(counterSort[:num]))

        return result