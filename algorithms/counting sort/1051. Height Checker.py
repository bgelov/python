# https://leetcode.com/problems/height-checker/
# Oleg Belov

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expectedDict = [0] * 101
        for studentHeight in heights:
            expectedDict[studentHeight] += 1
        
        expectedList = []
        for i in range(101):
            for j in range(expectedDict[i]):
                expectedList.append(i)

        result_count = 0
        for i in range(len(heights)):
            if expectedList[i] != heights[i]:
                result_count += 1

        return result_count
