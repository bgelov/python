# https://leetcode.com/problems/sort-an-array/description/
# Oleg Belov

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        min_num = min(nums)
        max_num = max(nums)

        counting_dict = {}
        for num in nums:
            if num not in counting_dict:
                counting_dict[num] = 0
            counting_dict[num] += 1

        result = []
        for i in range(min_num, max_num+1):
            if i in counting_dict:
                for j in range(counting_dict[i]):
                    result.append(i)

        return result