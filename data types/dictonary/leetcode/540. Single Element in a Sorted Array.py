class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        num_dict = {}
        for num in nums:
            if num not in num_dict.keys():
                num_dict[num] = 1
            else:
                del num_dict[num]
        return [x for x in num_dict.keys()][0]