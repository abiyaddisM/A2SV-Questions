# February 7 2025
# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        freqdic = Counter(chars)
        total = 0
        for word in words:
            temp = freqdic.copy()
            for i in range(len(word)):
                if word[i] not in temp or (word[i] in temp and temp[word[i]] == 0):
                    break
                temp[word[i]] -= 1
            else:
                total += len(word)


        return total