# https://leetcode.com/problems/kth-missing-positive-number/description/

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        num = 1
        num_count = 0
        while num_count < k:
            if num not in arr:
                num_count += 1
                if num_count == k:
                    return num
            num += 1