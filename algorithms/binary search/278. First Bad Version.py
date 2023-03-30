# https://leetcode.com/problems/first-bad-version
# Oleg Belov

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 0
        high = n - 1
        bad = n
        while low <= high:
            mid = (low + high) // 2
            print(low,high,mid,bad)
            if isBadVersion(mid) == True:
                if mid < bad or bad == n:
                    bad = mid
                high = mid - 1
            else:
                low = mid + 1
        return bad