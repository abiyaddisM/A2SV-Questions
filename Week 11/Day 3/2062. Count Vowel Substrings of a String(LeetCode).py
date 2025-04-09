# April 9 2025
# https://leetcode.com/problems/count-vowel-substrings-of-a-string/description/
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        ms = {'a','e','i','o','u'}
        dic = {}
        res = 0
        total = 0
        l = 0
        for r in range(len(word)):
            if word[r] not in ms:
                total = r + 1
                l = r + 1
                dic = {}
                continue
            dic[word[r]] = dic.get(word[r], 0) + 1
            while len(dic) == 5:
                dic[word[l]] -= 1
                if dic[word[l]] == 0:
                    dic.pop(word[l])
                l += 1
            res += l - total

        return res