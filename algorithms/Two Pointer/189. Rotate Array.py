# https://leetcode.com/problems/rotate-array/
# Oleg Belov

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def two_pointer(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        # Get number of steps
        k %= len(nums) 
        start = 0
        end = len(nums)-1
        # Reverse nums
        two_pointer(nums, start, end)
        # Reverse first k elements
        two_pointer(nums, start, k-1)
        # Reverse elements from k+
        two_pointer(nums, k, end)