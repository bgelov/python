# https://leetcode.com/problems/reverse-prefix-of-word/
# Oleg Belov

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
       #def two_p(word,start,end):
        #    while start<end:
         #       word[start],word[end] = word[end],word[start]
          #      start += 1
           #     end -= 1
        start = 0
        end = word.find(ch)
        word = list(word)
        if end != -1:
            while start<end:
                word[start],word[end] = word[end],word[start]
                start += 1
                end -= 1
        return "".join(word)