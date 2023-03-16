# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
# Oleg Belov

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        n = len(nums1)
        if n == 1:
            return nums1[0]
        elif n == 2:
            return (nums1[0]+nums1[1])/2
        else:
            nums1.sort()
            if n % 2 == 0:
                return (nums1[(n//2)-1]+nums1[(n//2)])/2
            else:
                return nums1[(n//2)]