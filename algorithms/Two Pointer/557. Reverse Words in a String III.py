# https://leetcode.com/problems/reverse-words-in-a-string-iii
# Oleg Belov

class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse_two_p(string):
            start = 0
            end = len(string)-1
            string = list(string)
            while start<end:
                string[start], string[end] = string[end], string[start]
                start += 1
                end -= 1
            return "".join(string)
        
        split_s = s.split(" ")
        ans = []
        for string in split_s:
            ans.append(reverse_two_p(string))
        return " ".join(ans)