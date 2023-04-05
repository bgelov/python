# https://leetcode.com/problems/merge-strings-alternately
# Oleg Belov

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        start = 0
        end1, end2 = len(word1), len(word2)
        ans = ""
        while start < end1 and start < end2:
            ans += word1[start] + word2[start]
            start += 1
        else:
            if start == end1:
                ans += word2[start::]
            else:
                ans += word1[start::]
        return ans
          
