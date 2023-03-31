# Two pointer rotate array
# Oleg Belov

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        start = 0
        end = len(nums)-1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1