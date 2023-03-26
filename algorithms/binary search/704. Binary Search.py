# https://leetcode.com/problems/binary-search
# Oleg Belov

class Solution:
    def search(self, nums: List[int], target: int) -> int:       
        def binary_search(low, high):
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    return binary_search(mid + 1, high)
                else:
                    return binary_search(low, mid - 1)
            return -1

        low = 0
        high = len(nums) - 1
        return binary_search(low, high)
  
# without def  

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1