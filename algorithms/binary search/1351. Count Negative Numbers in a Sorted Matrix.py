# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix
# Oleg Belov

class Solution:
  def countNegatives(self, grid: List[List[int]]) -> int:
    def binary_search(nums):
      low = 0
      high = len(nums)
      while low < high:
        mid = low + (high - low) // 2
        if nums[mid]<0:
          high = mid
        else:
          low = mid + 1
      return len(nums) - low
    neg = 0
    for nums in grid:
      neg += binary_search(nums)
    return neg