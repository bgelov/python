class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alien_alph_dict = {}
        for i, ch in enumerate(list(order)):
            alien_alph_dict[ch] = i

        for j in range(0, len(words)-1):
            first_word, second_word = words[j], words[j+1]
            min_len = min(len(first_word), len(second_word))

            for k in range(min_len):
                if first_word[k] != second_word[k]:
                    if alien_alph_dict.get(first_word[k],None) > alien_alph_dict.get(second_word[k],None):
                        return False
                    else:
                        break
            if len(first_word) > len(second_word) and second_word == first_word[0:len(second_word)]:
                return False
        return True