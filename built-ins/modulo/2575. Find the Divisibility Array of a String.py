class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        result = []
        num = 0
        for ch in word:
            num = num*10+int(ch)
            num = num % m
            if num == 0:
                result.append(1)
            else:
                result.append(0)
        return result