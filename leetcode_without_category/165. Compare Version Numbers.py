# https://leetcode.com/problems/compare-version-numbers
# Oleg Belov

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split(".")))
        v2 = list(map(int, version2.split(".")))
        v1_len, v2_len = len(v1),len(v2)
        if v1_len < v2_len:
            v1.extend([0] * (v2_len - v1_len))
        elif v1_len > v2_len:
            v2.extend([0] * (v1_len - v2_len))

        for i in range(len(v1)):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1
        return 0 
